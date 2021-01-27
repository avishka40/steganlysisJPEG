from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

from keras.models import load_model
from PIL import Image
import numpy as np
from skimage import io
import torch
from torch import nn
import os
from datetime import datetime
import time
import random
import cv2
import pandas as pd
import numpy as np
import albumentations as A
import matplotlib.pyplot as plt
from albumentations.pytorch.transforms import ToTensorV2
from torch.utils.data import Dataset,DataLoader
from torch.utils.data.sampler import SequentialSampler, RandomSampler
import sklearn


def get_train_transforms():
    return A.Compose([
            A.HorizontalFlip(p=0.5),
            A.VerticalFlip(p=0.5),
            A.Resize(height=512, width=512, p=1.0),
            ToTensorV2(p=1.0),
        ], p=1.0)

def get_valid_transforms():
    return A.Compose([
            A.Resize(height=512, width=512, p=1.0),
            ToTensorV2(p=1.0),
        ], p=1.0)
#Model as a backbone
from efficientnet_pytorch import EfficientNet
class DatasetSubmissionRetriever(Dataset):

    def __init__(self):
        super().__init__()
     

    def __getitem__(self, index: int):
        transform = get_valid_transforms()
        image = cv2.imread("./00001Juni.jpg", cv2.IMREAD_COLOR)
        print("image",image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
        image /= 255.0
        sample = {'image': image}
        sample = transform(**sample)
        image = sample['image']

        return image

    def __len__(self) -> int:
        return 1;
def predict(): 
    net = EfficientNet.from_pretrained('efficientnet-b2',include_top = True)
    net._fc = nn.Linear(in_features=1408, out_features=4, bias=True)
    checkpoint = torch.load('./best-checkpoint-033epoch.bin')
    net.load_state_dict(checkpoint['model_state_dict']);
    net.eval();
    dataset = DatasetSubmissionRetriever()
    data_loader = DataLoader(
        dataset,
        batch_size=1,
        shuffle=False,
        num_workers=2,
        drop_last=False,
    )

    model = load_model("./model2.hd5")

    
    for step, (image) in enumerate(data_loader):
        print(step, end='\r')
        print(image)
        print("shape",image.shape)

        y_pred = net(image)
        print(1 - nn.functional.softmax(y_pred, dim=1).data.cpu().numpy())
        y_pred = 1 - nn.functional.softmax(y_pred, dim=1).data.cpu().numpy()[:,0]

        print("test")
        print(y_pred)
    return y_pred 

predict()
