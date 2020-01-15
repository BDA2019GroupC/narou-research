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

def train(paths, save_dir, sub_steps, validation_steps, 
    dic_size, bottle_neck_size, embedding_size, device):

    BOS, EOS, UNK = 1,2,3
    
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
    def write_list_to_file(save_dir, writelist):
        with open(os.path.join(save_dir,"log.csv"), "a") as f:
            f.write(",".join(writelist)+"\n")

    DLs = [DataLoader(path,validation_split=0.2,shuffle=True) for path in paths]
    train_generator = get_generator(DLs, mode="training")
    validation_generator = get_generator(DLs, mode="validation")

    model = Char2vec(dic_size, bottle_neck_size, embedding_size)
    model.to(device)
    opt = optim.Adam(model.parameters())

    losses = 0.
    min_val_losses = 100000.
    writelist = ["" for _ in range(4)]
    nowtime = time.time()
    for i, data in enumerate(train_generator,1):
        center, context, negative = get_ccn(data)
        loss = model.cbow(center, context, negative)
        loss.backward()
        opt.step()
        opt.zero_grad()
        losses+=loss
        if i % sub_steps == 0:
            pretime = nowtime
            nowtime = time.time()
            writelist[0] = str(i)
            writelist[1] = str(nowtime-pretime)
            writelist[2] = str(losses/sub_steps)
            print('{} s'.format(nowtime - pretime))
            print('Step={}; loss={:.7f}'.format(i, losses/sub_steps))

            losses = 0.
            model.train(False)
            for j, val_data in enumerate(validation_generator):
                center, context, negative = get_ccn(val_data)
                loss = model.cbow(center, context, negative)
                losses += loss
                if j > validation_steps: break
            writelist[3] = str(losses/validation_steps)
            write_list_to_file(save_dir,writelist)
            print('Validation losses:{:.7f}'.format(losses/validation_steps))
            if min_val_losses > losses:
                min_val_losses = losses
                model.save_c2v(save_dir, "{}_{:.4f}".format(i, losses/validation_steps))
            losses = 0.
            model.train(True)
        