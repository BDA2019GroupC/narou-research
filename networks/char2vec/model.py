import torch
import torch.nn as nn
import torch.nn.functional as F
import os

class Embedding(nn.Module):
    def __init__(self, input_size, output_size):
        super(Embedding, self).__init__()
        self.embedding = nn.Embedding(input_size,128)
        self.embLinear = nn.Linear(128, output_size, bias=False)
        self.embedding.weight.data.uniform_(-0.5 / 128, 0.5 / 128)
        self.embLinear.weight.data.uniform_(-0.5 / output_size, 0.5 / output_size)
 
    def forward(self, seqs):
        embedding = self.embedding(seqs)
        emblinear = self.embLinear(embedding)
        return emblinear

class Char2vec(nn.Module):
    def __init__(self, method, embedding, dic_size, embed_size, normalize=100):
        super(Char2vec, self).__init__()
        self.center_embedding = embedding
        self.context_embedding = nn.Embedding(dic_size, 128)
        self.context_linear = nn.Linear(128, embed_size, bias=False)
        self.context_embedding.weight.data.uniform_(-0.5 / 128, 0.5 / 128)
        self.context_linear.weight.data.uniform_(-0.5 / embed_size, 0.5 / embed_size)
        self.forward = self.cbow if method == "cbow" else self.skipGram
        self.normalize = normalize

    def save_c2v(self,path,post_name):
        torch.save(self.state_dict(), os.path.join(path,"c2v_{}.weight".format(post_name)))

    def context_embed(self, context):
        x = self.context_embedding(context)
        return self.context_linear(x)

    def cbow(self, center, contexts, negatives):
        center_emb = self.center_embedding(center)
        context_emb = self.context_embed(contexts)
        context_vec = torch.sum(context_emb, dim=1)
        negative_emb = self.context_embed(negatives)
        emb = torch.cat((center_emb.unsqueeze(1), -negative_emb), dim=1)
        score = torch.bmm(emb, context_vec.unsqueeze(2)).squeeze(2)
        cosloss = -torch.mean(F.logsigmoid(score))
        normloss = self.normalize*torch.pow((torch.norm(center_emb, dim=1)-1),2).mean()
        normloss+= self.normalize*torch.pow((torch.norm(context_emb,dim=1)-1),2).mean()
        normloss+= self.normalize*torch.pow((torch.norm(negative_emb,dim=1)-1),2).mean()
        return normloss, cosloss

    def skipGram(self, center, contexts, negatives):
        center_emb = self.center_embedding(center)
        context_emb = self.context_embed(contexts)
        negative_emb = self.context_embed(negatives)
        emb = torch.cat((center_emb.unsqueeze(1), -negative_emb), dim=1)
        score = torch.bmm(emb, context_emb.transpose(1, 2))
        cosloss = -torch.mean(F.logsigmoid(score))
        normloss = self.normalize*torch.pow((torch.norm(center_emb, dim=1)-1),2).mean()
        normloss += self.normalize*torch.pow((torch.norm(context_emb,dim=1)-1),2).mean()
        normloss += self.normalize*torch.pow((torch.norm(negative_emb,dim=1)-1),2).mean()
        return normloss, cosloss

    def inference(self, charid):
        return self.center_embedding(charid)

    def cosdistance(self, charid1, charid2):
        c1,c2 = self.inference(charid1), self.inference(charid2)
        c1 = c1/torch.norm(c1)
        c2 = c2/torch.norm(c2)
        return torch.dot(c1,c2)