import os
import torch
import argparse
from datetime import datetime
from narouresearch.networks.styleEncoder.train import train

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="this program is char2vec train")
    parser.add_argument("--aozora_path", help="source path aozora",required=True)
    parser.add_argument("--narou_path", help="source path narou",required=True)
    parser.add_argument("--save_dir",required=True)

    args = parser.parse_args()
    aozora_path = args.aozora_path
    narou_path = args.narou_path
    save_dir = args.save_dir

    if not torch.cuda.is_available(): 
        print("cuda is not available.")
        if must_cuda: exit()
        device = torch.device("cpu")
    else: device = torch.device("cuda")

    save_dir = os.path.join(save_dir,datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.makedirs(save_dir, exist_ok=True)
    
    paths = (aozora_path, narou_path)

    train(paths=paths, save_dir=save_dir)