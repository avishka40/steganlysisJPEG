
import timm
# from inplace_abn.abn import InPlaceABN
import torch
from torch import nn
class MobileVNet(nn.Module):
    def __init__(self):
        super().__init__()
          #adding the back bone 
        # self.backbone = backbone
        self.model = timm.create_model('mobilenetv3_rw', pretrained=True)
        self.avg_pool = torch.nn.AdaptiveAvgPool2d(1)
        self.linear= nn.Linear(in_features=1280, out_features=4, bias=True)

        
        print(self.model)

        
      
      
     

    def forward_backbone(self, x):
        return get_feature_of(self.model, x)

    def forward(self, x):
        features = self.model.forward_features(x)
        # x = F.relu(features, inplace=True)
        #x = F.adaptive_avg_pool2d(x, (1, 1))
        x = self.avg_pool(features).reshape(x.shape[0], -1)
        # x = torch.flatten(x, 1)
        # x = self.classifier(x)
        return self.linear(x)
