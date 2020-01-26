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
        output, _ = self.RNN(emblinear)
        return output[:,-1,:]

    def forwardTransformers(self, seqs):
        embedding = self.embedding(seqs)
        emblinear = self.embLinear(embedding)
        output = self.Transformer(emblinear)
        return output.mean(dim=1)


class StyleDisperser(nn.Module):
    def __init__(self, weights, method, input_size, hidden_size, output_size, normalize=100, margin=1):
        super(StyleDisperser, self).__init__()
        self.encoder = StyleEncoder(weights, method, input_size, hidden_size, output_size)
        self.normalize = normalize
        self.margin = margin

    def forward(self, batch, same=32):
        ret_z = self.encoder(batch)
        normloss = self.normalize*torch.pow((torch.norm(ret_z, dim=1)-1),2).mean()

        true_z, random_z = ret_z[:same], ret_z[same:]
        true_mean = torch.mean(true_z, dim=0)
        true_std = torch.std(true_z, dim=0).sum()
        random_std = (torch.mv(random_z,true_mean.T)/torch.norm(random_z,dim=1)/torch.norm(true_mean)).mean()
        return normloss, true_std, random_std

    def inference(self, x):
        return self.encoder(x)
