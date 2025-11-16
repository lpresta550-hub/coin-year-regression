# model.py
# Modello ResNet18 modificato per doppio input fronte/retro

import torch
import torch.nn as nn
from torchvision.models import resnet18

class DualResNet18(nn.Module):
    def __init__(self):
        super().__init__()

        self.front_model = resnet18(pretrained=True)
        self.back_model = resnet18(pretrained=True)

        # rimuovo l'ultimo layer
        self.front_model.fc = nn.Identity()
        self.back_model.fc = nn.Identity()

        # fully connected finale
        self.fc = nn.Linear(512 * 2, 1)

    def forward(self, front, back):
        f = self.front_model(front)
        b = self.back_model(back)
        out = torch.cat([f, b], dim=1)
        return self.fc(out)
