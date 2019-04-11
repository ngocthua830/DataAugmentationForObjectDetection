from data_aug.data_aug import *
from data_aug.bbox_util import *
import numpy as np
import cv2
import matplotlib.pyplot as plt
import pickle as pkl
#%matplotlib inline

img = cv2.imread("messi.jpg")[:,:,::-1]
bboxes = pkl.load(open("messi_ann.pkl", "rb"))

print(bboxes)

plotted_img = draw_rect(img, bboxes)
plt.imshow(plotted_img)
plt.show()

img_, bboxes_ = RandomHorizontalFlip(1)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img_, bboxes_)
plt.imshow(plotted_img)
plt.show()

img_, bboxes_ = RandomScale(0.3, diff=True)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img_, bboxes_)
plt.imshow(plotted_img)
plt.show()

img_, bboxes_ = RandomTranslate(0.3, diff=True)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img_, bboxes_)
plt.imshow(plotted_img)
plt.show()

img_, bboxes_ = RandomRotate(20)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img_, bboxes_)
plt.imshow(plotted_img)
plt.show()

img_, bboxes_ = RandomShear(0.2)(img.copy(), bboxes.copy())
ploted_img = draw_rect(img_, bboxes_)
plt.imshow(plotted_img)
plt.show()

img, bboxes_ = Resize(608)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img_, bboxes)
plt.imshow(plotted_img)
plt.show()

img_, bboxes_ = RandomHSV(100, 100, 100)(img.copy(), bboxes.copy())
plotted_img = draw_rect(img_, bboxes_)
plt.imshow(plotted_img)
plt.show()

seq = Sequence([RandomHSV(40, 40, 30), RandomHorizontalFlip(), RandomScale(), RandomTranslate(), RandomRotate(10), RandomShear()])
img_, bboxes_ = seq(img.copy(), bboxes.copy())

plotted_img = draw_rect(img_, bboxes_)
plt.imshow(plotted_img)
plt.show()



