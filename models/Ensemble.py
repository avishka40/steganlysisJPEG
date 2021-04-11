# from inplace_abn.abn import InPlaceABN
from efficientnet_pytorch import EfficientNet
import timm
# from inplace_abn.abn import InPlaceABN
import torch
from torch import nn
class Ensemble(torch.nn.Module):
    def __init__(self,out_features):
        super().__init__()
          #adding the back bone 
        # self.backbone = backbone
        self.out_features = out_features
        self.mobilenet =timm.create_model('mobilenetv3_rw', pretrained=True)
        self.mixnet =  self.model = timm.create_model('mixnet_s', pretrained=True)
        self.efficientNet = EfficientNet.from_pretrained("efficientnet-b2")
        self.avg_pool = torch.nn.AdaptiveAvgPool2d(1)
        self.linear= nn.Linear(in_features=1408+1280, out_features=self.out_features, bias=True)
        # self.dropout1 = nn.Dropout(0.5)
        # self.linear2= nn.Linear(in_features=1280, out_features=512, bias=True)
        # self.dropout2 = nn.Dropout(0.3)

        # self.linear3= nn.Linear(in_features=512, out_features=256, bias=True)
        # self.dropout3 = nn.Dropout(0.1)
        # self.linear4= nn.Linear(in_features=256, out_features=3, bias=True)

          

        

        
      
      
     

    def forward_backbone(self, x):
        return get_feature_of(self.model, x)

    def forward(self, x):
        featuresMixnet = self.mobilenet.forward_features(x)
        featuresMixnet = self.avg_pool(featuresMixnet).reshape(x.shape[0], -1)
        featuresEffNet = self.efficientNet.extract_features(x)
        featuresEffNet = self.avg_pool(featuresEffNet).reshape(x.shape[0], -1)
        x =torch.cat((featuresMixnet,featuresEffNet),dim=1)
        #print(x.shape," before")
        # x=self.dropout1(x)
        # #print(x.shape," after")
        # x=self.linear(x)
        # x=self.dropout2(x)
        # x=self.linear2(x)
        # x=self.dropout3(x)
        # x=self.linear3(x)

        # x = F.relu(features, inplace=True)
        #x = F.adaptive_avg_pool2d(x, (1, 1))
       # x = self.avg_pool(features).reshape(x.shape[0], -1)
        # x = torch.flatten(x, 1)
        # x = self.classifier(x)
        return self.linear(x)