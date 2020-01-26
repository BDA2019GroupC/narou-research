import os
import time
import random
import gc
import numpy as np
import torch
import torch.optim as optim
from narouresearch.networks.styleEncoder.model import StyleDisperser
from narouresearch.dataloader.dataloader import LengthsDataGenerator
from narouresearch.networks.styleEncoder.plot import plot_from_files
from narouresearch.conversion.convert import char2ID as char2id, ID2char as id2char
from narouresearch.dataloader.dataloader import get_random_sentence_in_work
from narouresearch.utils.io_util import get_workpath
from narouresearch.networks.styleEncoder.plot import plot_from_files

def train(paths, save_dir, max_epoch, steps, sub_steps, validation_steps,
        early_stopping, method, device, saved_model_dir, margin, examples):

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
                quantity = samerand[1]
                while True:
                    while len(paths) < quantity+1:
                        wid, dirc = random.choice(plist)
                        path = os.path.join(dirc,str(length)+".txt")
                        if os.path.exists(path): paths.append((wid, path))
                    for i in range(quantity+1):
                        try: get_random_sentence_in_work(paths[i][1], quantity); break
                        except ValueError: i += 1
                    try: tmpl = get_random_sentence_in_work(paths[i][1], quantity); break
                    except IndexError: count+=1
                    if count > 10: quantity-=1; count = 0
                    if quantity < 10: return
                retlist = list(map(lambda x: (paths[i][0], x), tmpl))
                for path in paths:
                    if path == paths[i]: continue
                    retlist.append((path[0],get_random_sentence_in_work(path[1], 1)[0]))
                yield quantity, retlist
        return LengthsDataGenerator(generator, min_len, max_len)()

    def transform(batchData):
        return torch.tensor([[char2id(c) for c in data[-1]]+[EOS] for data in batchData]).to(device)

    writelists = []
    def write_list_to_file(save_dir, filename, writelist):
        with open(os.path.join(save_dir,filename), "a") as f:
            f.write(",".join(writelist)+"\n")


    model = StyleDisperser(weights=None, method=method, input_size=24498, hidden_size=512, output_size=512, device=device, margin=margin)
    model.to(device)
    opt = optim.Adam(model.parameters())

    train_generator = get_generator(mode="training")
    validation_generator = get_generator(mode="validation")

    losses = [0., 0.]
    sub_losses = [0., 0.]
    min_val_losses = [100000., 100000.]
    writelist = ["epoch","time_per_epoch","train_loss_true","train_loss_random","validation_loss_true","validation_loss_random"]
    write_list_to_file(save_dir,"log.csv",writelist)
    writelist = ["epoch","steps_in_epoch","time_per_sub_steps","sub_steps_loss_true","sub_steps_loss_random","sub_step_loss"]
    write_list_to_file(save_dir,"sub_log.csv",writelist)
    count = 0
    for epoch in range(max_epoch):
        nowtime = time.time()
        sub_nowtime = time.time()
        step_nowtime = time.time()
        losses = [0., 0.]
        model.train()
        try: train_generator.__next__()
        except StopIteration:
            train_generator = get_generator(mode="training")
        for i, (q, data) in enumerate(train_generator,1):
            gc.collect()
            d_tensor = transform(data)
            truestd, randomstd = model.forward(d_tensor, q)
            loss = truestd + randomstd
            if torch.isnan(loss).any(): print();print(d_tensor);print(truestd);print(randomstd);exit()
            opt.zero_grad()
            loss.backward()
            opt.step()
            losses[0]+=truestd; losses[1]+=randomstd
            sub_losses[0]+=truestd; sub_losses[1]+=randomstd
            step_pretime = step_nowtime
            step_nowtime = time.time()
            print('{:3f}s'.format(step_nowtime - step_pretime),end="; ")
            print('epoch={:<2}; Step={:<4}; truestd={:.7f}; randomstd={:.7f}; loss={:.7f}'.format(epoch, i, truestd, randomstd, loss),end="\r")
            if i % sub_steps == 0:
                sub_pretime = sub_nowtime
                sub_nowtime = time.time()
                writelist=["{}".format(epoch), "{}".format(i)]
                writelist.append("{}".format(sub_nowtime - sub_pretime))
                writelist.append("{:.7f}".format(sub_losses[0]/sub_steps))
                writelist.append("{:.7f}".format(sub_losses[1]/sub_steps))
                writelist.append("{:.7f}".format(sum(sub_losses)/sub_steps))
                write_list_to_file(save_dir,"sub_log.csv",writelist)
                sub_losses=[0., 0.]
                # torch.save(model.state_dict(), os.path.join(save_dir,"{}epoch_{}steps".format(epoch, i)))
                plot_from_files(save_dir,["sub_log.csv","log.csv"],"log_{}_{}.png".format(epoch,i))
                print()
                with torch.no_grad():
                    dics = {}
                    for ex in examples:
                        dics[ex] = model.inference(transform([ex]))
                        print(random.sample(list(dics[ex].cpu().numpy()[0]),3), end="\t")
                        print(ex)
                    for pp in range(len(dics)):
                        for qq in range(pp+1, len(dics)):
                            print("{:.7f}".format(float(torch.dot(list(dics.values())[pp][0],list(dics.values())[qq][0]))), end="\t")
                            print(list(dics.keys())[pp] + " to " + list(dics.keys())[qq])
            if steps is not None and i >= steps: break
        print()
        pretime = nowtime
        nowtime = time.time()
        writelist = ["{}".format(epoch)]
        writelist.append("{}".format(nowtime-pretime))
        writelist.append("{}".format(losses[0]/i))
        writelist.append("{}".format(losses[1]/i))

        losses = [0.,0.]
        model.eval()
        try: validation_generator.__next__()
        except StopIteration: 
            validation_generator = get_generator(mode="validation")
        with torch.no_grad():
            for j, (q, data) in enumerate(validation_generator,1):
                gc.collect()
                d_tensor = transform(data)
                truestd, randomstd = model.forward(d_tensor, q)
                loss = truestd + randomstd
                if torch.isnan(loss).any(): print();print(d_tensor);print(truestd);print(randomstd);exit()
                losses[0]+= truestd
                losses[1]+= randomstd
                print('validating{} Step={:<4}; truestd={:.7f}; randomstd={:.7f}'.format('.'*(j%10)+' '*(10-j%10), j, truestd, randomstd),end="\r")
                if validation_steps is not None and j >= validation_steps: break
        print()
        writelist.append("{}".format(losses[0]/j))
        writelist.append("{}".format(losses[1]/j))
        write_list_to_file(save_dir,"log.csv",writelist)
        print('({: =2}){: =3} epoch, Validation truestd:{:.7f}; randomstd:{:.7f}'.format(count,epoch,losses[0]/j,losses[1]/j))
        count += 1
        if sum(min_val_losses) > sum(losses):
            count = 0
            min_val_losses[0] = losses[0]
            min_val_losses[1] = losses[1]
            torch.save(model.state_dict(), os.path.join(save_dir,"{:_=3}_{:.4f}_{:.4f}".format(epoch, losses[0]/j, losses[1]/j)))
            print("model is saved")
        if count >= early_stopping: 
            plot_from_files(save_dir,["sub_log.csv","log.csv"],"log_{}_{}.png".format(epoch,i))
            break