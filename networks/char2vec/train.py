import time
import torch.optim as optim
from narouresearch.networks.char2vec.model import Char2vec
from narouresearch.dataloader.dataloader import RandomLengthBatchDataLoaderMultiDomain
from narouresearch.conversion.convert import char2ID as char2id, ID2char as id2char

def train(paths, save_dir, steps_per_epoch, validation_steps, 
    dic_size, bottle_neck_size, embedding_size, device):

    BOS, EOS, UNK = 1,2,3
    dataloader = RandomLengthBatchDataLoaderMultiDomain(
        paths,
        min_len=11,
        max_len=70,
        max_batch_size=512,
        validation_split=0.2,
        shuffle=True
    )

    def transform(batchData):
        return torch.tensor([[BOS]+[char2id(c) for c in data[2]]+[EOS] for data in batchData], device=device)

    def dl_w2v_wrap(batch_tensor, window_size=5):
        i = np.random.randint(window_size, batch_tensor.shape[1]-window_size-1)
        center = batch_tensor[:,i]
        context = torch.cat((batch_tensor[:,i-window_size:i], batch_tensor[:,i+1:i+window_size+1]),1)
        return center, context

    def get_ccn(batch):
        batch = transform(s)
        center, context = dl_w2v_wrap(batch)
        negative = torch.randint(dic_size,(batch.shape[0],5))
        center = center.to(device)
        context = context.to(device)
        negative = negative.to(device)
        return center, context, negative

    train_generator = dataloader.get_generator(mode="training")
    validation_generator = dataloader.get_generator(mode="validation")

    model = Char2vec(dic_size, bottle_neck_size, embedding_size)
    model.to(device)
    opt = optim.Adam(model.parameters())

    losses = 0.
    min_val_losses = 100000.
    nowtime = time.time()
    for i, data in enumerate(train_generator,1):
        center, context, negative = get_cnn(data)
        loss = model.cbow(center, context, negative)
        loss.backward()
        opt.step()
        opt.zero_grad()
        losses+=loss
        if i % steps_per_epoch == 0:
            pretime = nowtime
            nowtime = time.time()
            print('{} s'.format(nowtime - pretime))
            print('Step={}; loss={:.7f}'.format(i, losses))

            losses = 0.
            model.train(False)
            for j, val_data in enumerate(validation_generator):
                center, context, negative = get_cnn(val_data)
                loss = model.cbow(center, context, negative)
                losses += loss
                if j > test_steps: break
            print('Validation losses:{:.7f}'.format(losses/test_steps))
            if min_val_losses > losses:
                min_val_losses = losses
                model.save_c2v(save_dir, losses)
            losses = 0.
            model.train(True)
        