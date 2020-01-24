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
        if method == "Transformer": pass

    def forwardRNN(self, seqs):
        embedding = self.embedding(seqs)
        emblinear = self.embLinear(embedding)
        # print(emblinear.shape) torch.Size([64, 12, 512])
        output, _ = self.RNN(emblinear)
        return output[:,-1,:]

class StyleDisperser(nn.Module):
    def __init__(self, weights, method, input_size, hidden_size, output_size, normalize=100):
        super(StyleDisperser, self).__init__()
        self.encoder = StyleEncoder(weights, method, input_size, hidden_size, output_size)
        self.normalize = normalize

    def forward(self, batch, same=32):
        ret_z = self.encoder(batch)
        loss = self.normalize*torch.pow((torch.norm(ret_z, dim=1)-1),2).sum()/ret_z.shape[0]

        true_z, random_z = ret_z[:same], ret_z[same:]
        true_mean = torch.mean(true_z)
        true_std = torch.std(true_z)
        loss += true_std - torch.pow((random_z-true_mean),2).sum()
        return loss