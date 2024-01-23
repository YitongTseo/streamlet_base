# ==============================================
# 0. Module imports
# ==============================================

import torch
from torch import nn, optim
import torch.nn.functional as F

import warnings
warnings.filterwarnings("ignore")

device = "cpu"

class PneumoniaCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout_rate = 0.1 # For now hardcode this

        self.conv1 = nn.Conv2d(3, 5, kernel_size=3)
        self.conv2 = nn.Conv2d(5, 1, kernel_size=3)
        self.conv2_drop = nn.Dropout2d(self.dropout_rate)

        self.fc1 = nn.Linear(54*54, 300)
        self.dropout1 = nn.Dropout(self.dropout_rate)
        self.fc2 = nn.Linear(300, 30)
        self.dropout2 = nn.Dropout(self.dropout_rate)
        self.fc3 = nn.Linear(30, 1)


    def forward(self, x):
        x1 = F.relu(F.max_pool2d(self.conv1(x), 2))
        x2 = self.conv2_drop(self.conv2(x1))
        x3 = F.relu(F.max_pool2d(x2, 2))

        # TODO: What is the shape at this point in the model?
        # breakpoint()

        x4 = x3.view(-1, 54*54)

        x5 = self.dropout1(F.relu(self.fc1(x4)))
        x6 = self.dropout2(F.relu(self.fc2(x5)))
        
        print("yitong")
        breakpoint()

        return F.sigmoid(self.fc3(x6))
    
# #Later to restore:
# model.load_state_dict(torch.load(filepath))
# model.eval()
