import torch
import torch.nn as nn
import torch.nn.functional as F

class StyleEncoder(nn.Module):
    def __init__(self, weights, method, input_size, hidden_size, output_size):
        super(StyleEncoder, self).__init__()
        self.output_size = output_size
        self.embedding = weights[0] if weights is not None else nn.Embedding(input_size,128)
        self.embLinear = weights[1] if weights is not None else nn.Linear(128, hidden_size)
        if method == "RNN":
            self.forward = self.forwardRNN
            self.RNN   = nn.RNN(hidden_size, hidden_size, num_layers=2, dropout=0.2, batch_first=True, bidirectional=True)
        if method == "Transformer":
            self.forward = self.forwardTransformers
            d_model = 512
            nhead = 8
            num_encoder_layers = 6
            dim_feedforward=2048
            dropout=0.1
            activation="relu"
            encoder_layer = nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout, activation)
            encoder_norm = nn.LayerNorm(d_model)
            self.Transformer = nn.TransformerEncoder(encoder_layer, num_encoder_layers, encoder_norm)

    def forwardRNN(self, seqs):
        embedding = self.embedding(seqs)
        emblinear = self.embLinear(embedding)
        output_, _ = self.RNN(emblinear)
        output = output_[:,-1,:]
        return torch.renorm(output, p=2, dim=0, maxnorm=1)

    def forwardTransformers(self, seqs):
        embedding = self.embedding(seqs)
        emblinear = self.embLinear(embedding)
        output_ = self.Transformer(emblinear)
        output = output_.mean(dim=1)
        return torch.renorm(output, p=2, dim=0, maxnorm=1)


class StyleDisperser(nn.Module):
    def __init__(self, weights, method, input_size, hidden_size, output_size, device, normalize=100, margin=0.7):
        super(StyleDisperser, self).__init__()
        self.encoder = StyleEncoder(weights, method, input_size, hidden_size, output_size)
        self.normalize = normalize
        self.margin = margin
        self.device = device

    def forward(self, batch, same=32):
        ret_z = self.encoder(batch)
        true_z, random_z = ret_z[:same], ret_z[same:]
        true_mean = torch.mean(true_z, dim=0)
        true_std = 1. - (torch.mv(true_z,true_mean.T)/torch.norm(true_z,dim=1)/torch.norm(true_mean)).mean()
        random_std = -self.margin + torch.max(torch.tensor([self.margin]).to(self.device),torch.mv(random_z,true_mean.T)/torch.norm(random_z,dim=1)/torch.norm(true_mean)).mean()
        if true_std < 0 or true_std > 2 or random_std < 0 or random_std > 2:
            print("\nERROR std")
            print(true_std)
            print(random_std)
        return true_std, random_std

    def inference(self, x):
        return self.encoder(x)

    def cosdistance(self, x, y):
        s1 = self.encoder(x)
        s2 = self.encoder(y)
        s1 = s1 / torch.norm(s1)
        s2 = s2 / torch.norm(s2)
        return torch.dot(s1,s2)
