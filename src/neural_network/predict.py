from PyQt5.QtCore import pyqtSignal,  QThread
import torch

from utils.config import Config
import numpy as np
import colorsys
import os
# import torch
from nets import ssd
import torch.backends.cudnn as cudnn
from utils.box_utils import letterbox_image,ssd_correct_boxes
from PIL import ImageFont, ImageDraw

# 数据集的RGB平均像素
MEANS = (182, 177, 188)


class SSD(QThread):
    msg = pyqtSignal(str)
    set_image=pyqtSignal(str)
    # ---------------------------------------------------#
    #   初始化RFB
    # ---------------------------------------------------#
    def __init__(self):
        QThread.__init__(self)
        self.Config = Config
        self.class_names = self._get_class()
        self.generate()
        self.image= None
        self.path=""

    # ---------------------------------------------------#
    #   获得所有的分类
    # ---------------------------------------------------#
    def _get_class(self):
        classes_path = os.path.expanduser(self.Config["classes_path"])
        with open(classes_path) as f:
            class_names = f.readlines()
        class_names = [c.strip() for c in class_names]
        return class_names

    # ---------------------------------------------------#
    #   获得所有的分类
    # ---------------------------------------------------#
    def generate(self):
        # 计算总的种类
        self.num_classes = len(self.class_names) + 1

        # 载入模型，如果原来的模型里已经包括了模型结构则直接载入。
        # 否则先构建模型再载入
        model = ssd.get_ssd("test", self.num_classes)
        self.net = model
        # 标签文件中不能有空白行
        model.load_state_dict(torch.load(self.Config["model_path"], map_location=torch.device('cpu')), strict=False)

        self.net = torch.nn.DataParallel(self.net)
        cudnn.benchmark = True
        # self.net = self.net.cuda()

        # print('{} model, anchors, and classes loaded.'.format(self.Config["model_path"]))
        # 画框设置不同的颜色
        hsv_tuples = [(x / len(self.class_names), 1., 1.)
                      for x in range(len(self.class_names))]
        self.colors = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))
        self.colors = list(
            map(lambda x: (int(x[0] * 255), int(x[1] * 255), int(x[2] * 255)),
                self.colors))

    # ---------------------------------------------------#
    #   检测图片
    # ---------------------------------------------------#
    def run(self):
        #计数
        count=0
        # print('{} model, anchors, and classes loaded.'.format(self.Config["model_path"]))
        image_shape = np.array(np.shape(self.image)[0:2])

        # letterbox_image边缘加灰条仿失真，改变总体图片大小为300*300
        crop_img = np.array(
            letterbox_image(self.image, (self.Config["model_image_size"][0], self.Config["model_image_size"][1])))
        # 转化float64
        photo = np.array(crop_img, dtype=np.float64)

        # 图片预处理，归一化
        # photo = Variable(torch.from_numpy(np.expand_dims(np.transpose(crop_img-MEANS,(2,0,1)),0)).type(torch.FloatTensor)) #将通道数从第三维度调整到第一维度 ！cudaGPU加速.cuda().type(torch.FloatTensor))
        # crop_img - MEANS所有像素点-平均值 相当于标准化
        photo = torch.from_numpy(np.expand_dims(np.transpose(crop_img - MEANS, (2, 0, 1)), 0)).type(torch.FloatTensor)
        # preds.shape(1,21,200,5)((这张图片)bacth_size,类别num_class,得分最高200框，参数)
        preds = self.net(photo)

        top_conf = []
        top_label = []
        top_bboxes = []

        # 置信度筛选
        for i in range(preds.size(1)):
            j = 0
            while preds[0, i, j, 0] >= self.Config["confidence"]:
                score = preds[0, i, j, 0]
                label_name = self.class_names[i - 1]
                pt = (preds[0, i, j, 1:]).detach().numpy()
                coords = [pt[0], pt[1], pt[2], pt[3]]
                top_conf.append(score)
                top_label.append(label_name)
                top_bboxes.append(coords)
                j = j + 1

        # 将预测结果进行解码
        if len(top_conf) <= 0:
            self.msg.emit("图中一共有:0 个 目标对象")
            self.set_image.emit("")
            self.msg.emit("预测完成")
        else:
            top_conf = np.array(top_conf)
            top_label = np.array(top_label)
            top_bboxes = np.array(top_bboxes)
            top_xmin, top_ymin, top_xmax, top_ymax = np.expand_dims(top_bboxes[:, 0], -1), np.expand_dims(
                top_bboxes[:, 1],
                -1), np.expand_dims(
                top_bboxes[:, 2], -1), np.expand_dims(top_bboxes[:, 3], -1)

            # 去掉灰条
            boxes = ssd_correct_boxes(top_ymin, top_xmin, top_ymax, top_xmax,
                                      np.array(
                                          [self.Config["model_image_size"][0], self.Config["model_image_size"][1]]),
                                      image_shape)
            # 字体
            font = ImageFont.truetype(font='model_data/simhei.ttf',
                                      size=np.floor(3e-2 * np.shape(self.image)[1] + 0.5).astype('int32'))
            # 厚度
            thickness = (np.shape(self.image)[0] + np.shape(self.image)[1]) // self.Config["model_image_size"][0]

            for i, c in enumerate(top_label):
                count += 1
                predicted_class = c
                score = top_conf[i]

                top, left, bottom, right = boxes[i]
                top = top - 5
                left = left - 5
                bottom = bottom + 5
                right = right + 5

                top = max(0, np.floor(top + 0.5).astype('int32'))
                left = max(0, np.floor(left + 0.5).astype('int32'))
                bottom = min(np.shape(self.image)[0], np.floor(bottom + 0.5).astype('int32'))
                right = min(np.shape(self.image)[1], np.floor(right + 0.5).astype('int32'))

                # 画框框
                label = '{} {:.2f}-{}'.format(predicted_class, score, count)
                draw = ImageDraw.Draw(self.image)
                label_size = draw.textsize(label, font)
                label = label.encode('utf-8')
                self.msg.emit(str(label.decode()))

                if top - label_size[1] >= 0:
                    text_origin = np.array([left, top - label_size[1]])
                else:
                    text_origin = np.array([left, top + 1])

                for i in range(thickness):
                    draw.rectangle(
                        [left + i, top + i, right - i, bottom - i],
                        outline=self.colors[self.class_names.index(predicted_class)])
                draw.rectangle(
                    [tuple(text_origin), tuple(text_origin + label_size)],
                    fill=self.colors[self.class_names.index(predicted_class)])
                draw.text(text_origin, str(label, 'UTF-8'), fill=(0, 0, 0), font=font)
                del draw
            self.msg.emit("图中一共有:" + str(count) + " 个 目标对象")
            # 可更改
            self.path = "neural_network/img/predict_output.png"
            self.image.save(self.path)
            self.set_image.emit(self.path)
            self.msg.emit("预测完成")


