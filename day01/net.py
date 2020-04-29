import torch
from torch import nn

class NetV1(nn.Module):
    def __init__(self):
        super().__init__()

        self.W = nn.Parameter(torch.randn(784,10))

    def forward(self, x):
        h = x@self.W
        h = torch.exp(h)
        z = torch.sum(h,dim=1,keepdim=True)
        return h/z

class NetV2(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784,100)
        self.relu_1 = nn.ReLU()
        self.fc2 = nn.Linear(100,10)
        self.softmax = nn.Softmax(dim=1)

    def forward(self,x):
        h = self.fc1(x)
        h = self.relu_1(h)
        h = self.fc2(h)
        y = self.softmax(h)
        return y

class NetV3(nn.Module):
    def __init__(self):
        super().__init__()
        self.seq = nn.Sequential(
            nn.Linear(784,100),
            nn.ReLU(),
            nn.Linear(100,10),
            nn.Softmax()
        )

    def forward(self,x):
        return self.seq(x)

if __name__ == '__main__':
    net = NetV1()
    x = torch.randn(4,784)
    y = net(x)
    print(y.shape)