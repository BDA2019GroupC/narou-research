import os
import time
import numpy as np
import torch
import torch.optim as optim
from narouresearch.networks.char2vec.model import Char2vec
from narouresearch.dataloader.dataloader import DataLoader
from narouresearch.dataloader.dataloader import GeneratorRandomMixer
from narouresearch.dataloader.dataloader import BatchDataGenerator
from narouresearch.dataloader.dataloader import RandomLengthDataGenerator
from narouresearch.conversion.convert import char2ID as char2id, ID2char as id2char

def train(paths, save_dir, max_epoch, steps, sub_steps, validation_steps, early_stopping,
    method, dic_size, bottle_neck_size, embedding_size, device, example):

    BOS, EOS, UNK = 1,2,3
    exampleids = [char2id(c) for c in example]
    def get_generator(DLs, mode="training"):
        max_batch_size = 128
        min_len = 11
        max_len = 70
        generators = [DL.get_generator(mode) for DL in DLs]
        generator = GeneratorRandomMixer(generators)
        generator = BatchDataGenerator(generator, max_batch_size=max_batch_size)
        generator = RandomLengthDataGenerator(generator, min_len=min_len, max_len=max_len)
        return generator()

    def transform(batchData):
        return torch.tensor([[BOS]+[char2id(c) for c in data[-1]]+[EOS] for data in batchData], device=device)

    def dl_w2v_wrap(batch_tensor, window_size=5):
        i = np.random.randint(window_size, batch_tensor.shape[1]-window_size-1)
        center = batch_tensor[:,i]
        context = torch.cat((batch_tensor[:,i-window_size:i], batch_tensor[:,i+1:i+window_size+1]),1)
        return center, context

    def get_ccn(batch):
        batch = transform(batch)
        center, context = dl_w2v_wrap(batch)
        negative = torch.randint(dic_size,(batch.shape[0],5))
        center = center.to(device)
        context = context.to(device)
        negative = negative.to(device)
        return center, context, negative

    writelists = []
    def write_list_to_file(save_dir, filename, writelist):
        with open(os.path.join(save_dir,filename), "a") as f:
            f.write(",".join(writelist)+"\n")

    DLs = [DataLoader(path,validation_split=0.2,shuffle=True) for path in paths]
    
    validation_generator = get_generator(DLs, mode="validation")

    model = Char2vec(method, dic_size, bottle_neck_size, embedding_size)
    model.to(device)
    opt = optim.Adam(model.parameters())

    losses = 0.
    sub_losses = 0.
    min_val_losses = 100000.
    writelist = ["epoch","time_per_epoch","train_loss","validation_loss"]
    write_list_to_file(save_dir,"log.csv",writelist)
    writelist = ["epoch","steps_in_epoch","time_per_sub_steps","sub_steps_loss"]
    write_list_to_file(save_dir,"sub_log.csv",writelist)
    writelist = ["{} to {}".format(e1,e2) for e1 in range(len(example)) for e2 in range(e1, len(example))]
    write_list_to_file(save_dir,"vocab.csv",writelist)
    count = 0
    for epoch in range(max_epoch):
        nowtime = time.time()
        sub_nowtime = time.time()
        losses = 0.
        model.train(True)
        train_generator = get_generator(DLs, mode="training")
        for i, data in enumerate(train_generator,1):
            center, context, negative = get_ccn(data)
            loss = model.forward(center, context, negative)
            loss.backward()
            opt.step()
            opt.zero_grad()
            losses+=loss
            sub_losses+=loss
            if i % sub_steps == 0:
                sub_pretime = sub_nowtime
                sub_nowtime = time.time()
                print('{:3f}s'.format(sub_nowtime - sub_pretime),end="; ")
                print('Step={}; loss={:.7f}'.format(i, sub_losses/sub_steps))
                writelist=[]
                writelist.append("{}".format(epoch))
                writelist.append("{}".format(i))
                writelist.append("{}".format(sub_nowtime - sub_pretime))
                writelist.append("{:.7f}".format(sub_losses/sub_steps))
                write_list_to_file(save_dir,"sub_log.csv",writelist)
                sub_losses=0.
                writelist=[]
                for e1 in range(len(example)):
                    for e2 in range(e1, len(example)):
                        writelist.append("{:.7f}".format(model.cosdistance(exampleids[e1],exampleids[e2])))
                        print("{} to {}: {: 7f}".format(example[e1],example[e2],model.cosdistance(exampleids[e1],exampleids[e2])))
                write_list_to_file(save_dir,"vocab.csv",writelist)
            if steps is not None and i > steps: break
        pretime = nowtime
        nowtime = time.time()
        writelist = []
        writelist.append("{}".format(epoch))
        writelist.append("{}".format(nowtime-pretime))
        writelist.append("{}".format(losses/i))

        losses = 0.
        model.train(False)
        try: validation_generator.__next__()
        except StopIteration: 
            validation_generator = get_generator(DLs, mode="validation")
        for j, val_data in enumerate(validation_generator):
            center, context, negative = get_ccn(val_data)
            loss = model.cbow(center, context, negative)
            losses += loss
            if validation_steps is not None and j > validation_steps: break
        writelist.append("{}".format(losses/validation_steps))
        write_list_to_file(save_dir,"log.csv",writelist)
        print('({: =2}){: =3} epoch, Validation losses:{:.7f}'.format(epoch,count,losses/validation_steps))
        count += 1
        if min_val_losses > losses:
            count = 0
            min_val_losses = losses
            model.save_c2v(save_dir, "{:_=6}_{:.4f}".format(epoch, losses/validation_steps))
            print("model is saved")
        if count >= early_stopping: break