import torch
import torch.nn as nn
import torch.nn.functional as F
import os

class Char2vec(nn.Module):
    def __init__(self, method, dic_size, bottleneck_size, embed_size, saved_model_dir=None, normalize=100):
        super(Char2vec, self).__init__()
        self.center_embedding = nn.Embedding(dic_size, bottleneck_size)
        self.center_linear = nn.Linear(bottleneck_size, embed_size, bias=False)
        self.context_embedding = nn.Embedding(dic_size, bottleneck_size)
        self.context_linear = nn.Linear(bottleneck_size, embed_size, bias=False)
        weight_path = self.get_model_weight(saved_model_dir)
        if weight_path is not None:
            print("loaded weights from " + weight_path)
            self.load_state_dict(torch.load(weight_path))
        else:
            self.center_embedding.weight.data.uniform_(-0.5 / bottleneck_size, 0.5 / bottleneck_size)
            self.center_linear.weight.data.uniform_(-0.5 / embed_size, 0.5 / embed_size)
            self.context_embedding.weight.data.uniform_(-0.5 / bottleneck_size, 0.5 / bottleneck_size)
            self.context_linear.weight.data.uniform_(-0.5 / embed_size, 0.5 / embed_size)

        self.forward = self.cbow if method == "cbow" else self.skipGram
        self.normalize = normalize

    def get_model_weight(self, saved_model_dir):
        if saved_model_dir is None: return None
        if not os.path.isdir(saved_model_dir): raise Exception("saved_model_dir must be directory path")
        import glob
        weight_paths = glob.glob(os.path.join(saved_model_dir,"c2v_[_0-9][_0-9][0-9]_*.*.weight"))
        if len(weight_paths) == 0: raise Exception("there is no model weight")
        
        weight_paths = list(map(lambda x:(x,float(".".join(x.split("_")[-1].split(".")[:-1]))), weight_paths))
        weight_paths = sorted(weight_paths, key=lambda x:x[1])
        return weight_paths[0][0]

    def save_c2v(self,path,post_name):
        torch.save(self.state_dict(), os.path.join(path,"c2v_{}.weight".format(post_name)))

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
        negative_emb = self.context_embed(negatives)
        emb = torch.cat((center_emb.unsqueeze(1), -negative_emb), dim=1)
        score = torch.bmm(emb, context_vec.unsqueeze(2)).squeeze(2)
        cosloss = -torch.mean(F.logsigmoid(score))
        normloss = self.normalize*torch.pow((torch.norm(center_emb, dim=1)-1),2).mean()
        normloss+= self.normalize*torch.pow((torch.norm(context_emb,dim=1)-1),2).mean()
        normloss+= self.normalize*torch.pow((torch.norm(negative_emb,dim=1)-1),2).mean()
        return normloss, cosloss

    def skipGram(self, center, contexts, negatives):
        center_emb = self.center_embed(center)
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
        return self.center_embed(charid)

    def cosdistance(self, charid1, charid2):
        c1,c2 = self.inference(charid1), self.inference(charid2)
        c1 = c1/torch.norm(c1)
        c2 = c2/torch.norm(c2)
        return torch.dot(c1,c2)