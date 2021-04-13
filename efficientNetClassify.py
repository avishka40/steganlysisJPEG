
from PIL import Image
from six import StringIO
import requests

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
import time

from models.Ensemble import Ensemble
from models.MobileVNet import MobileVNet
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
class PredictReponse():
    def __init__(self,binaryArray,multiClassArray):
        self.binaryArray=binaryArray;
        self.multiClassArray=multiClassArray;
# class DatasetSubmissionRetriever(Dataset):

#     def __init__(self):
#         super().__init__()
     

#     def __getitem__(self, index: int):
#         transform = get_valid_transforms()
#         image = cv2.imread("./00001Juni.jpg", cv2.IMREAD_COLOR)
#         jpeg_struct = jio.read("./00001Juni.jpg")
#         print("DCT")
#         print(np.stack(jpeg_struct.coef_arrays, axis=-1))
#         print("DCT End")
#         image = decompress_structure(jpeg_struct)
#         image = ycbcr2rgb(image).astype(np.float32)
#         print("image",image)
#     #    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
#         image /= 255.0
#         sample = {'image': image}
#         sample = transform(**sample)
#         image = sample['image']

#         return image

#     def __len__(self) -> int:
#         return 1;
import os

# def predict(filename): 
#     net = EfficientNet.from_pretrained('efficientnet-b2')

#     net._fc = nn.Linear(in_features=1408, out_features=3, bias=True)
#     #net = Ensemble(3)
#     # net = MobileVNet()
#     #checkpoint = torch.load('./best-checkpoint-033epoch.bin')
#     #mobile
#     checkpoint = torch.load('./100epoch/best-checkpoint-099epoch.bin')
#     #eff 3 net
#     checkpoint = torch.load('./confusion_matrix/eff3class/best-checkpoint-033epoch.bin')
#     #ensemble
#     #checkpoint = torch.load('./confusion_matrix/3classbalnced93.bin')
#     net.load_state_dict(checkpoint['model_state_dict']);
#     net.eval();
#     # dataset = DatasetSubmissionRetriever()
#     # data_loader = DataLoader(
#     #     dataset,
#     #     batch_size=1,
#     #     shuffle=False,
#     #     num_workers=2,
#     #     drop_last=False,
#     # )

#     # model = load_model("./model2.hd5")

    
#     # for step, (image) in enumerate(data_loader):
#     #     print(step, end='\r')
#     #     print(image)
#     #     print("shape",image.shape)
       

#     #     y_pred = net(image)
#     #     y_pred= 1 - nn.functional.softmax(y_pred, dim=1).data.cpu().numpy()
#     #     y_pred = y_pred * 100
#     #     print(y_pred)
        
#     #     #y_pred = 1 - nn.functional.softmax(y_pred, dim=1).data.cpu().numpy()[:,0]
#     #     y_pred = y_pred.astype(int)
#     #     print("test")
#     #     print(y_pred)
       
#     #     # results[0]=y_pred[0].int()
#     #     # results[1]=y_pred[1].int()
#     #     # results[2]=y_pred[2].int()
#     #     # results[3]=y_pred[3].int()
#     # print(step, end='\r')
#     # print(image)
#     # print("shape",image.shape)
#     transform = get_valid_transforms()
#     image = cv2.imread(filename, cv2.IMREAD_COLOR)
#     # jpeg_struct = jio.read(filename)
#     # print("DCT")
#     # # print(np.stack(jpeg_struct.coef_arrays, axis=-1))
#     # print("DCT End")
#     # image = decompress_structure(jpeg_struct)
#     # image = ycbcr2rgb(image).astype(np.float32)
#     print("image",image)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
#     image /= 255.0
#     sample = {'image': image}
#     sample = transform(**sample)
#     image = sample['image']
#     print(image.shape)
#     image = image.view(1, 3, 512,512)
#     y_pred = net(image)
#     print(y_pred)
#     print(1 - nn.functional.softmax(y_pred, dim=1).data.cpu().numpy()[:,0])
#     binaryClassification = 1 - nn.functional.softmax(y_pred, dim=1).data.cpu().numpy()[:,0]
#     binaryClassification=binaryClassification*100
#     # binaryClassification=binaryClassification.astype(int)
#     y_pred= nn.functional.softmax(y_pred, dim=1).data.cpu().numpy()
#     y_pred = y_pred * 100

#     print(y_pred)
    
    

#     # y_pred = y_pred.astype(int)
#     multi=y_pred[0]
#     print(np.argmax(multi,axis=0))
  
   
#     if(np.argmax(multi,axis=0)==0):
#         binaryClassification[0]=0

#     elif(multi[np.argmax(multi,axis=0)]<=50 and  multi[np.argmax(multi,axis=0)]-np.partition(multi.flatten(),-2)[-2]<=10 ):
#         binaryClassification[0]=0.1
#     response = PredictReponse(binaryClassification.astype(int),y_pred[0].astype(int))
#     print("test")
#     print(y_pred)
       
#         # results[0]=y_pred[0].int()
#         # results[1]=y_pred[1].int()
#         # results[2]=y_pred[2].int()
#         # results[3]=y_pred[3].int()



#     return response 

#predict("dad")
 #rgb = cv2.cvtColor(cv2.imdecode(np.frombuffer(buf, np.uint8), cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
 #           dct = _read_with_jio(tmp_jpeg.name, method[4:])
import json

def predictMultiple(path):

    directory = './TEST/UERD/'
    result={}
    for filename in os.listdir(directory):
        print("filename",filename)
        if filename.endswith(".jpeg") or filename.endswith(".jpg"):
           print("filename",directory+filename)
           response=predict(directory+filename)
           result[filename]={"binary":response.binaryArray.tolist(),
           "multi":response.multiClassArray.tolist()}
        else:
           continue
    with open('Resulteffciennet3UERD1024', 'w') as f:
        json.dump(result, f)

# predictMultiple("test")
class Predicter:
    def __init__(self,output=3):
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        

        if(output==3):
            self.net = EfficientNet.from_pretrained('efficientnet-b2').to(device)
            self.net._fc = nn.Linear(in_features=1408, out_features=3, bias=True)
            self.checkpoint = torch.load('./confusion_matrix/eff3class/best-checkpoint-068epoch.bin',map_location=device)
            self.net.load_state_dict(self.checkpoint['model_state_dict'])
        else:
            self.net = EfficientNet.from_pretrained('efficientnet-b2').to(device)
            self.net._fc = nn.Linear(in_features=1408, out_features=4, bias=True)
            self.checkpoint = torch.load('./confusion_matrix/efficientnet2b/best-checkpoint-058epoch.bin',map_location=device)
            self.net.load_state_dict(self.checkpoint['model_state_dict'])
        self.net.eval();
        self.transform = get_valid_transforms()

    def preprocess(self,filename,isByteArray=False):
        image = None
        if(isByteArray):
            image = cv2.imdecode(filename, cv2.IMREAD_COLOR)
        else:
            image = cv2.imread(filename, cv2.IMREAD_COLOR)
        # jpeg_struct = jio.read(filename)
        # print("DCT")
        # # print(np.stack(jpeg_struct.coef_arrays, axis=-1))
        # print("DCT End")
        # image = decompress_structure(jpeg_struct)
        # image = ycbcr2rgb(image).astype(np.float32)
        print("image",image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
        image /= 255.0
        sample = {'image': image}
        sample = self.transform(**sample)
        image = sample['image']
        print(image.shape)
        image = image.view(1, 3, 512,512)
        return image
    
    def predict(self,image):
        # time.sleep(3)
        y_pred = self.net(image)
        print(y_pred)
        print(1 - nn.functional.softmax(y_pred, dim=1).data.cpu().numpy()[:,0])
        binaryClassification = 1 - nn.functional.softmax(y_pred, dim=1).data.cpu().numpy()[:,0]
        binaryClassification=binaryClassification*100
        # binaryClassification=binaryClassification.astype(int)
        y_pred= nn.functional.softmax(y_pred, dim=1).data.cpu().numpy()
        y_pred = y_pred * 100

        print(y_pred)
        # y_pred = y_pred.astype(int)
        multi=y_pred[0]
        print(np.argmax(multi,axis=0))
        if(np.argmax(multi,axis=0)==0):
            binaryClassification[0]=0

        elif(multi[np.argmax(multi,axis=0)]<=50 and  multi[np.argmax(multi,axis=0)]-np.partition(multi.flatten(),-2)[-2]<=10 ):
            binaryClassification[0]=0.1
        response = PredictReponse(binaryClassification.astype(int),y_pred[0].astype(int))
        print("test")
        print(y_pred)

            # results[0]=y_pred[0].int()
            # results[1]=y_pred[1].int()
            # results[2]=y_pred[2].int()
            # results[3]=y_pred[3].int()



        return response
def predictFromWeb(filename):
        # image = cv2.imread(filename, cv2.IMREAD_COLOR)
        # img_str = cv2.imencode('.jpg', img)[1].tostring()
        # pil_im = Image.fromarray(image)
        # stream = StringIO()
        # pil_im.save(stream, format="JPEG")
        # stream.seek(0)
        # img_for_post = stream.read() 
        
        files = {'image':open(filename, 'rb') }
        response = requests.post(
            url='http://localhost:5000/file-upload',
            files=files
        )
        return response