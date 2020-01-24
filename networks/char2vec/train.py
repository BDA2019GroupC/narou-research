import os
import time
import random
import numpy as np
import torch
import torch.optim as optim
from narouresearch.networks.char2vec.model import Char2vec
from narouresearch.dataloader.dataloader import DataLoader
from narouresearch.dataloader.dataloader import GeneratorRandomMixer
from narouresearch.dataloader.dataloader import BatchDataGenerator
from narouresearch.dataloader.dataloader import LengthsDataGenerator
from narouresearch.conversion.convert import char2ID as char2id, ID2char as id2char
from narouresearch.networks.char2vec.plot import plot_from_files

def train(paths, save_dir, max_epoch, steps, sub_steps, validation_steps, early_stopping,
    method, dic_size, bottle_neck_size, embedding_size, device, example, saved_model_dir):

    BOS, EOS, UNK = 0,1,2
    exampleids = [torch.tensor(char2id(c)) for c in example]
    def get_generator(DLs, mode="training"):
        max_batch_size = 256
        min_len = 11
        max_len = 70
        generators = [DL.get_generator(mode) for DL in DLs]
        generator = GeneratorRandomMixer(generators)
        generator = BatchDataGenerator(generator, max_batch_size=max_batch_size)
        generator = LengthsDataGenerator(generator, min_len=min_len, max_len=max_len)
        return generator()

    def transform(batchData):
        return torch.tensor([([BOS] if len(data[-1])>20 else []) +[char2id(c) for c in data[-1]]+[EOS] for data in batchData])

    def dl_w2v_wrap(batch_tensor, window_size=5):
        if window_size > (batch_tensor.shape[1]-1)//2: window_size = (batch_tensor.shape[1]-1)//2
        i = np.random.randint(window_size, batch_tensor.shape[1]-window_size)
        center = batch_tensor[:,i]
        context = torch.cat((batch_tensor[:,i-window_size:i], batch_tensor[:,i+1:i+window_size+1]),1)
        return center, context

    def get_ccn(batch, window_size=5, negative_size=5):
        batch = transform(batch)
        center, context = dl_w2v_wrap(batch, window_size)
        negative = torch.randint(dic_size,(batch.shape[0],negative_size))
        # center = center.to(device)
        # context = context.to(device)
        # negative = negative.to(device)
        return center, context, negative

    writelists = []
    def write_list_to_file(save_dir, filename, writelist):
        with open(os.path.join(save_dir,filename), "a") as f:
            f.write(",".join(writelist)+"\n")

    DLs = [DataLoader(path,validation_split=0.1,shuffle=True) for path in paths]
    
    train_generator = get_generator(DLs, mode="training")
    validation_generator = get_generator(DLs, mode="validation")

    model = Char2vec(method, dic_size, bottle_neck_size, embedding_size, device, normalize=10., saved_model_dir=saved_model_dir)
    model.to(device)
    opt = optim.Adam(model.parameters())

    losses = 0.
    sub_losses = 0.
    min_val_losses = 100000.
    writelist = ["epoch","time_per_epoch","train_loss","validation_loss"]
    write_list_to_file(save_dir,"log.csv",writelist)
    writelist = ["epoch","steps_in_epoch","time_per_sub_steps","sub_steps_loss"]
    write_list_to_file(save_dir,"sub_log.csv",writelist)
    writelist = ["epoch","steps_in_epoch"]+["{}_to_{}".format(e1,e2) for e1 in range(len(example)) for e2 in range(e1+1, len(example))]
    write_list_to_file(save_dir,"vocab.csv",writelist)
    count = 0
    for epoch in range(max_epoch):
        nowtime = time.time()
        sub_nowtime = time.time()
        step_nowtime = time.time()
        losses = 0.
        model.train()
        try: train_generator.__next__()
        except StopIteration: 
            train_generator = get_generator(DLs, mode="training")
        for i, data in enumerate(train_generator,1):
            center, context, negative = get_ccn(data, window_size=random.randint(5,20), negative_size=random.randint(10,40))
            normloss, cosloss = model.forward(center, context, negative)
            if i % 10 == 0: loss = normloss + cosloss
            else: loss = cosloss
            if torch.isnan(loss).any(): print();print(data);print(center);print(context);print(negative);exit()
            loss.backward()
            opt.step()
            opt.zero_grad()
            losses+=loss
            sub_losses+=loss
            step_pretime = step_nowtime
            step_nowtime = time.time()
            print('{:3f}s'.format(step_nowtime - step_pretime),end="; ")
            print('epoch={:<2}; Step={:<4}; normloss={:.7f}; cosloss={:.7f}'.format(epoch, i, normloss, cosloss),end="\r")
            if i % sub_steps == 0:
                sub_pretime = sub_nowtime
                sub_nowtime = time.time()
                writelist=["{}".format(epoch), "{}".format(i)]
                writelist.append("{}".format(sub_nowtime - sub_pretime))
                writelist.append("{:.7f}".format(sub_losses/sub_steps))
                write_list_to_file(save_dir,"sub_log.csv",writelist)
                sub_losses=0.
                writelist=["{}".format(epoch), "{}".format(i)]
                for e1 in range(len(example)):
                    for e2 in range(e1+1, len(example)):
                        writelist.append("{:.7f}".format(model.cosdistance(exampleids[e1],exampleids[e2])))
                write_list_to_file(save_dir,"vocab.csv",writelist)
                plot_from_files(save_dir,["vocab.csv","sub_log.csv","log.csv"],"log_{}_{}.png".format(epoch,i))
                model.save_c2v(save_dir, "{}epoch_{}steps".format(epoch, i))
            if steps is not None and i >= steps: break
        print()
        pretime = nowtime
        nowtime = time.time()
        writelist = ["{}".format(epoch)]
        writelist.append("{}".format(nowtime-pretime))
        writelist.append("{}".format(losses/i))

        losses = 0.
        model.eval()
        try: validation_generator.__next__()
        except StopIteration: 
            validation_generator = get_generator(DLs, mode="validation")
        with torch.no_grad():
            for j, val_data in enumerate(validation_generator):
                center, context, negative = get_ccn(val_data, window_size=5, negative_size=15)
                normloss, cosloss = model.forward(center, context, negative)
                loss = normloss + cosloss
                if torch.isnan(loss).any(): print();print(data);print(center);print(context);print(negative);exit()
                losses += loss
                print('validating{} Step={:<4}; normloss={:.7f}; cosloss={:.7f}'.format('.'*(j%10)+' '*(10-j%10), j, normloss, cosloss),end="\r")
                if validation_steps is not None and j >= validation_steps: break
        print()
        writelist.append("{}".format(losses/j))
        write_list_to_file(save_dir,"log.csv",writelist)
        plot_from_files(save_dir,["vocab.csv","sub_log.csv","log.csv"],"log_{}_{}.png".format(epoch,i))
        print('({: =2}){: =3} epoch, Validation losses:{:.7f}'.format(count,epoch,losses/j))
        count += 1
        if min_val_losses > losses:
            count = 0
            min_val_losses = losses
            model.save_c2v(save_dir, "{:_=3}_{:.4f}".format(epoch, losses/j))
            print("model is saved")
        if count >= early_stopping: break