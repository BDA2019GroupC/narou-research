import torch
import torch.nn as nn
import torch.nn.functional as F
import os

class Char2vec(nn.Module):
    def __init__(self, method, dic_size, bottleneck_size, embed_size):
        super(Char2vec, self).__init__()
        self.center_embedding = nn.Embedding(dic_size, bottleneck_size)
        self.center_linear = nn.Linear(bottleneck_size, embed_size, bias=False)
        self.context_embedding = nn.Embedding(dic_size, bottleneck_size)
        self.context_linear = nn.Linear(bottleneck_size, embed_size, bias=False)
        self.center_embedding.weight.data.uniform_(-0.5 / bottleneck_size, 0.5 / bottleneck_size)
        self.center_linear.weight.data.uniform_(-0.5 / embed_size, 0.5 / embed_size)
        self.context_embedding.weight.data.uniform_(-0.5 / bottleneck_size, 0.5 / bottleneck_size)
        self.context_linear.weight.data.uniform_(-0.5 / embed_size, 0.5 / embed_size)
        self.forward = self.cbow if method == "cbow" else self.skipGram

    def save_c2v(self,path,post_name):
        torch.save(self.center_embedding.weight.data, os.path.join(path,"c2v_embedding_{}.weight".format(post_name)))
        torch.save(self.center_linear.weight.data, os.path.join(path,"c2v_linear_{}.weight".format(post_name)))

    def center_embed(self, center):
        x = self.center_embedding(center)
        return self.center_linear(x)

    def context_embed(self, context):
        x = self.context_embedding(context)
        return self.context_linear(x)

    def cbow(self, center, contexts, negatives):
        center_emb = self.center_embed(center)
        context_emb = self.context_embed(contexts)
        context_vec = torch.sum(context_emb, dim=1)
        negative_emb = self.center_embed(negatives)
        emb = torch.cat((center_emb.unsqueeze(1), -negative_emb), dim=1)
        score = torch.bmm(emb, context_vec.unsqueeze(2)).squeeze(2)
        loss = -torch.mean(F.logsigmoid(score))
        return loss

    def skipGram(self, center, contexts, negatives):
        center_emb = self.center_embed(center)
        context_emb = self.context_embed(contexts)
        negative_emb = self.center_embed(negatives)
        # emb: (batchsize, negative + 1, dim)
        emb = torch.cat((center_emb.unsqueeze(1), -negative_emb), dim=1)
        # score: (batchsize, negatives + 1, context_len)
        score = torch.bmm(emb, context_emb.transpose(1, 2))
        # score: (batchsize, negative + 1)
        loss = -torch.mean(F.logsigmoid(score))

        loss += 1000*torch.pow((torch.norm(center_emb, dim=1)-1),2).sum()/center_emb.shape[1]
        loss += 1000*torch.pow((torch.norm(context_emb,dim=1)-1),2).sum()/context_emb.shape[2]/context_emb.shape[1]
        loss += 1000*torch.pow((torch.norm(negative_emb,dim=1)-1),2).sum()/negative_emb.shape[2]/negative_emb.shape[1]
        return loss

    def inference(self, charid):
        return self.center_embed(charid)

    def cosdistance(self, charid1, charid2):
        c1,c2 = self.inference(charid1), self.inference(charid2)
        c1 = c1/torch.norm(c1)
        c2 = c2/torch.norm(c2)
        return torch.dot(c1,c2)