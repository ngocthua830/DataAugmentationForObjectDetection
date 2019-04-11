from data_aug.data_aug import *
from data_aug.bbox_util import *
import cv2 
import pickle as pkl
import numpy as np 
import matplotlib.pyplot as plt


img = cv2.imread("messi.jpg")[:,:,::-1] #OpenCV uses BGR channels
bboxes = pkl.load(open("messi_ann.pkl", "rb"))



transforms = Sequence([RandomHorizontalFlip(1), RandomScale(0.2, diff = True), RandomRotate(10)])

img, bboxes = transforms(img, bboxes)
for bbox in bboxes:
   print(bbox)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imwrite("user_output/messi_out.jpg", draw_rect(img,bboxes))
#plt.imshow(draw_rect(img, bboxes))
#plt.show()
