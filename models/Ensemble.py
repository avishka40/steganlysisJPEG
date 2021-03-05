# from inplace_abn.abn import InPlaceABN
from efficientnet_pytorch import EfficientNet
import timm
import torch
from torch import nn
class Ensemble(nn.Module):
    def __init__(self):
        super().__init__()
          #adding the back bone 
        # self.backbone = backbone
        # self.mobilenet =timm.create_model('mobilenetv3_rw', pretrained=True)
        self.mixnet =  self.model = timm.create_model('mixnet_s', pretrained=True)
        self.efficientNet = EfficientNet.from_pretrained("efficientnet-b2")
        self.avg_pool = torch.nn.AdaptiveAvgPool2d(1)
        self.linear= nn.Linear(in_features=1280+1536, out_features=4, bias=True)

        

        
      
      
     


    def forward(self, x):
        featuresMixnet = self.mixnet.forward_features(x)
        featuresMixnet = self.avg_pool(featuresMixnet).reshape(x.shape[0], -1)
        featuresEffNet = self.efficientNet.extract_features(x)
        featuresEffNet = self.avg_pool(featuresEffNet).reshape(x.shape[0], -1)
        x =torch.cat((featuresMixnet,featuresEffNet),dim=1)
        # x = F.relu(features, inplace=True)
        #x = F.adaptive_avg_pool2d(x, (1, 1))
       # x = self.avg_pool(features).reshape(x.shape[0], -1)
        # x = torch.flatten(x, 1)
        # x = self.classifier(x)
        return self.linear(x)