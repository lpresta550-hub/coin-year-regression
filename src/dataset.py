# dataset.py
# Dataset class per gestione immagini fronte/retro

import os
from PIL import Image
from torch.utils.data import Dataset

class CoinDataset(Dataset):
    def __init__(self, dataframe, transform=None):
        self.df = dataframe
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        front_path = self.df.iloc[idx]['front_img']
        back_path = self.df.iloc[idx]['back_img']

        front = Image.open(front_path).convert('RGB')
        back = Image.open(back_path).convert('RGB')

        if self.transform:
            front = self.transform(front)
            back = self.transform(back)

        return front, back, self.df.iloc[idx]['year']
