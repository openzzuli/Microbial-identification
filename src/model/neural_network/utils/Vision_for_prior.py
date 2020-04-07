#生成及测试先验框

import numpy as np
from utils.config import Config
from math import sqrt as sqrt
import matplotlib.pyplot as plt

mean = []
for k, f in enumerate(Config["feature_maps"]):
    x,y = np.meshgrid(np.arange(f),np.arange(f))# 输入的x，y，就是网格点的横纵坐标列向量（非矩阵） 输出的X，Y，就是坐标矩阵。
    x = x.reshape(-1)# array([ 0,  1,  2, ..., 35, 36, 37])转成1维共1444个
    y = y.reshape(-1)#-1自动计算维度array([ 0,  0,  0, ..., 37, 37, 37])
    for i, j in zip(y,x):
        # zip()组合y和x形成[(0,0)(0,1)···(37,35)(37,36)(37,37)]
        # print(x,y)
        # 300/8 = 37.5
        f_k = Config["min_dim"] / Config["steps"][k]
        # 计算网格的中心
        cx = (j + 0.5) / f_k
        cy = (i + 0.5) / f_k

        # 求短边 小正方形
        s_k =  Config["min_sizes"][k]/Config["min_dim"]
        mean += [cx, cy, s_k, s_k]

        # 求长边 大正方形
        s_k_prime = sqrt(s_k * (Config["max_sizes"][k]/Config["min_dim"]))
        mean += [cx, cy, s_k_prime, s_k_prime]

        # 获得长方形
        for ar in Config["aspect_ratios"][k]:
            mean += [cx, cy, s_k*sqrt(ar), s_k/sqrt(ar)]
            mean += [cx, cy, s_k/sqrt(ar), s_k*sqrt(ar)]

mean = np.clip(mean,0,1) #clip函数裁剪最小值和最大值，防止低于0，超出1
mean = np.reshape(mean,[-1,4])*Config["min_dim"]

linx = np.linspace(0.5 * Config["steps"][4], Config["min_dim"] - 0.5 * Config["steps"][4],
                    Config["feature_maps"][4])
liny = np.linspace(0.5 * Config["steps"][4], Config["min_dim"] - 0.5 * Config["steps"][4],
                    Config["feature_maps"][4])


print("linx:",linx)
print("liny:",liny)
centers_x, centers_y = np.meshgrid(linx, liny)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ylim(-100,500)
plt.xlim(-100,500)
plt.scatter(centers_x,centers_y)

step_start = 8708
step_end = 8712
# step_start = 8728
# step_end = 8732
box_widths = mean[step_start:step_end,2]
box_heights = mean[step_start:step_end,3]

prior_boxes = np.zeros_like(mean[step_start:step_end,:])
prior_boxes[:,0] = mean[step_start:step_end,0]
prior_boxes[:,1] = mean[step_start:step_end,1]
prior_boxes[:,0] = mean[step_start:step_end,0]
prior_boxes[:,1] = mean[step_start:step_end,1]


# 获得先验框的左上角和右下角
prior_boxes[:, 0] -= box_widths/2
prior_boxes[:, 1] -= box_heights/2
prior_boxes[:, 2] += box_widths/2
prior_boxes[:, 3] += box_heights/2

rect1 = plt.Rectangle([prior_boxes[0, 0],prior_boxes[0, 1]],box_widths[0],box_heights[0],color="r",fill=False)
rect2 = plt.Rectangle([prior_boxes[1, 0],prior_boxes[1, 1]],box_widths[1],box_heights[1],color="r",fill=False)
rect3 = plt.Rectangle([prior_boxes[2, 0],prior_boxes[2, 1]],box_widths[2],box_heights[2],color="r",fill=False)
rect4 = plt.Rectangle([prior_boxes[3, 0],prior_boxes[3, 1]],box_widths[3],box_heights[3],color="r",fill=False)

ax.add_patch(rect1)
ax.add_patch(rect2)
ax.add_patch(rect3)
ax.add_patch(rect4)

plt.show()
print(np.shape(mean),mean[0,:])
