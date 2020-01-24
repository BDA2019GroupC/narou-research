import os
import time
import random
import numpy as np
import torch
import torch.optim as optim
from narouresearch.networks.styleEncoder.model import StyleDisperser
from narouresearch.dataloader.dataloader import DataLoader
from narouresearch.dataloader.dataloader import LengthsDataGenerator
# from narouresearch.networks.char2vec.plot import plot_from_files
from narouresearch.conversion.convert import char2ID as char2id, ID2char as id2char
from narouresearch.dataloader.dataloader import get_random_sentence_in_work
from narouresearch.utils.io_util import get_workpath
from narouresearch.networks.styleEncoder.plot import plot_from_files

def train(paths, save_dir, max_epoch, steps, sub_steps, validation_steps,
        early_stopping, method, device, saved_model_dir):

    BOS, EOS, UNK = 0,1,2
    pathlist = []
    for path in paths: pathlist.extend(get_workpath(path))
    for i in range(len(pathlist)): pathlist[i] = (i, pathlist[i])
    random.seed(0)
    train_pathlist = random.sample(pathlist, int(len(pathlist)*0.9))
    validation_pathlist = [path for path in pathlist if path not in train_pathlist]

    def get_generator(mode="training"):
        def generator(length, samerand=(32,32)):
            if mode == "training": plist = train_pathlist
            if mode == "validation": plist = validation_pathlist
            while True:
                paths = []
                count = 0
                while True:
                    while len(paths) < samerand[1]+1:
                        wid, dirc = random.choice(plist)
                        path = os.path.join(dirc,str(length)+".txt")
                        if os.path.exists(path): paths.append((wid, path))
                    for i in range(samerand[1]+1):
                        try: get_random_sentence_in_work(paths[i][1], samerand[1]); break
                        except ValueError: i += 1
                    try: tmpl = get_random_sentence_in_work(paths[i][1], samerand[1]); break
                    except IndexError: count+=1
                    if count > 10: return
                retlist = list(map(lambda x: (paths[i][0], x), tmpl))
                for path in paths:
                    if path == paths[i]: continue
                    retlist.append((path[0],get_random_sentence_in_work(path[1], 1)[0]))
                yield retlist
        min_len = 11
        max_len = 70
        return LengthsDataGenerator(generator, min_len, max_len)()

    def transform(batchData):
        return torch.tensor([[char2id(c) for c in data[-1]]+[EOS] for data in batchData])

    writelists = []
    def write_list_to_file(save_dir, filename, writelist):
        with open(os.path.join(save_dir,filename), "a") as f:
            f.write(",".join(writelist)+"\n")


    model = StyleDisperser(weights=None, method="RNN", input_size=24498, hidden_size=512, output_size=512)
    # model.to(device)
    opt = optim.Adam(model.parameters())

    train_generator = get_generator(mode="training")
    validation_generator = get_generator(mode="validation")

    losses = 0.
    sub_losses = 0.
    min_val_losses = 100000.
    writelist = ["epoch","time_per_epoch","train_loss","validation_loss"]
    write_list_to_file(save_dir,"log.csv",writelist)
    writelist = ["epoch","steps_in_epoch","time_per_sub_steps","sub_steps_loss"]
    write_list_to_file(save_dir,"sub_log.csv",writelist)
    count = 0
    for epoch in range(max_epoch):
        nowtime = time.time()
        sub_nowtime = time.time()
        step_nowtime = time.time()
        losses = 0.
        model.train()
        try: train_generator.__next__()
        except StopIteration: 
            train_generator = get_generator(mode="training")
        for i, data in enumerate(train_generator,1):
            normloss, stdloss = model.forward(transform(data))
            if i % 10 == 0: loss = normloss + stdloss
            loss = stdloss
            if torch.isnan(loss).any(): print();print(data);print(center);print(context);print(negative);exit()
            loss.backward()
            opt.step()
            opt.zero_grad()
            losses+=loss
            sub_losses+=loss
            step_pretime = step_nowtime
            step_nowtime = time.time()
            print('{:3f}s'.format(step_nowtime - step_pretime),end="; ")
            print('epoch={:<2}; Step={:<4}; normloss={:.7f}; stdloss={:.7f}'.format(epoch, i, normloss, stdloss),end="\r")
            if i % sub_steps == 0:
                sub_pretime = sub_nowtime
                sub_nowtime = time.time()
                writelist=["{}".format(epoch), "{}".format(i)]
                writelist.append("{}".format(sub_nowtime - sub_pretime))
                writelist.append("{:.7f}".format(sub_losses/sub_steps))
                write_list_to_file(save_dir,"sub_log.csv",writelist)
                sub_losses=0.
                torch.save(model.state_dict(), os.path.join(save_dir,"epoch:{}_steps:{}".format(epoch, i)))
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
            validation_generator = get_generator(mode="validation")
        with torch.no_grad():
            for j, val_data in enumerate(validation_generator,1):
                normloss, stdloss = model(transform(val_data))
                loss = normloss+stdloss
                if torch.isnan(loss).any(): print();print(data);print(center);print(context);print(negative);exit()
                losses += loss
                print('validating{} Step={:<4}; normloss={:.7f}; stdloss={:.7f}'.format('.'*(j%10)+' '*(10-j%10), j, normloss, stdloss),end="\r")
                if validation_steps is not None and j >= validation_steps: break
        print()
        writelist.append("{}".format(losses/j))
        write_list_to_file(save_dir,"log.csv",writelist)
        plot_from_files(save_dir,["sub_log.csv","log.csv"],"log_{}_{}.png".format(epoch,i))
        print('({: =2}){: =3} epoch, Validation losses:{:.7f}'.format(count,epoch,losses/j))
        count += 1
        if min_val_losses > losses:
            count = 0
            min_val_losses = losses
            torch.save(model.state_dict(), os.path.join(save_dir,"{:_=3}_{:.4f}".format(epoch, losses/j)))
            print("model is saved")
        if count >= early_stopping: break