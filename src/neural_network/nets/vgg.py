import torch.nn as nn


base = [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'C', 512, 512, 512, 'M',
            512, 512, 512]
# 300,300,3-> input
# 实际上从0层开始算 输入层不算 整体减1
# Conv1_1 300,300,64 ->1
# ReLU ->2
# Conv1_2 300,300,64 ->3
# ReLU ->4
# Pooling1 150,150,64 ->5

# Conv2_1 150,150,128 ->6
# ReLU ->7
# Conv2_2 150,150,128 ->8
# ReLU ->9
# Pooling2 75,75,128 ->10

# Conv3_1 75,75,256 ->11
# ReLU ->12
# Conv3_2 75,75,256 ->13
# ReLU ->14
# Conv3_3 75,75,256 -> 15    注意75是单数 最大池化默认ceil==false 会省略单数边缘->37
# ReLU ->16
# Pooling3 38,38,256 ->17

# Conv4_1 38,38,512 -> 18
# ReLU -> 19
# Conv4_2 38,38,512 -> 20
# ReLU -> 21
# Conv4_3 38,38,512 -> 22 做分类预测
# ReLU -> 23
# L2Norm -> 24
# Pooling4 19,19,512 -> 25 同上理

# Conv5_1 19,19,512 -> 26
# ReLU -> 27
# Conv5_2 19,19,512 -> 28
# ReLU -> 29
# Conv5_3 19,19,512 -> 30
# ReLU -> 31

# Pools 19,19,512 -> 32
# Conv6 19,19,1024 -> 33 具有膨胀率 模拟全连接
# ReLU -> 34
# Conv7 19,19,1024 -> 35 做分类预测
# ReLU -> 36


def vgg(i):
    layers = []
    # i = 3 三通道
    in_channels = i
    for v in base:
        if v == 'M':
            layers += [nn.MaxPool2d(kernel_size=2, stride=2)]
        elif v == 'C':
            layers += [nn.MaxPool2d(kernel_size=2, stride=2, ceil_mode=True)]
        else:
            conv2d = nn.Conv2d(in_channels, v, kernel_size=3, padding=1)
            layers += [conv2d, nn.ReLU(inplace=True)]
            in_channels = v
    pool5 = nn.MaxPool2d(kernel_size=3, stride=1, padding=1)
    conv6 = nn.Conv2d(512, 1024, kernel_size=3, padding=6, dilation=6) # 具有膨胀率 模拟全连接
    conv7 = nn.Conv2d(1024, 1024, kernel_size=1) # 全连接
    layers += [pool5, conv6,
               nn.ReLU(inplace=True), conv7, nn.ReLU(inplace=True)]
    return layers
