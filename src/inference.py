# inference.py
# Esempio di inferenza con modello salvato

import torch
from PIL import Image
from torchvision import transforms
from model import DualResNet18

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

def predict(front_path, back_path, model_path):
    model = DualResNet18()
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()

    front = Image.open(front_path).convert('RGB')
    back = Image.open(back_path).convert('RGB')

    front = transform(front).unsqueeze(0)
    back = transform(back).unsqueeze(0)

    with torch.no_grad():
        prediction = model(front, back).item()

    return prediction
