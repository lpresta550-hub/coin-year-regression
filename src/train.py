# train.py
# Script di training semplificato per il modello

import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from model import DualResNet18
from dataset import CoinDataset

def train_model(train_loader, val_loader, epochs=5):
    model = DualResNet18()
    criterion = nn.L1Loss()  # MAE
    optimizer = optim.Adam(model.parameters(), lr=1e-4)

    for epoch in range(epochs):
        model.train()
        for front, back, y in train_loader:
            optimizer.zero_grad()
            preds = model(front, back).squeeze()
            loss = criterion(preds, y)
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch+1}/{epochs} completato")

    return model
