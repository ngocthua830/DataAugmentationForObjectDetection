from data_aug.data_aug import *
from data_aug.bbox_util import *
import cv2 
import pickle as pkl
import numpy as np 
import matplotlib.pyplot as plt
import glob

DATASET_PATH = "/home/thuan/CV/DataAugmentation/small_object_dataset/"
EFFECT = "Sequence_1"

for filename in glob.glob(DATASET_PATH+"Train_image/*.jpg"):
   splited_filename = filename.split('/')
   filename = splited_filename[len(splited_filename)-1].split('.')[0]
   print(filename)
   img = cv2.imread(DATASET_PATH+"Train_image/"+filename+".jpg")[:,:,::-1] #OpenCV uses BGR channels
   #bboxes = pkl.load(open("checkpickle.pkl", "rb"))
   bboxes = pkl.load(open(DATASET_PATH+"converted/"+filename+".pkl", "rb"))
   print(bboxes)
   #print(type(bboxes))

#   transforms = Sequence([RandomHorizontalFlip(1), RandomScale(0.2, diff = True), RandomRotate(10)])

#   img, bboxes = transforms(img, bboxes)
   #transforms = Sequence([RandomHorizontalFlip(1), RandomRotate(10)])
   #img, bboxes = transforms(img, bboxes)
   img, bboxes = RandomHorizontalFlip(1)(img, bboxes)
   img, bboxes = RandomScale(0.3, diff=True)(img, bboxes)
   img, bboxes = RandomTranslate(0.3, diff=True)(img, bboxes)
   img, bboxes = RandomRotate(20)(img, bboxes)
   img, bboxes = RandomShear(0.2)(img, bboxes)
   img, bboxes = Resize(608)(img, bboxes)
   img, bboxes = RandomHSV(100, 100, 100)(img, bboxes)
   #for bbox in bboxes:
   #   print(bbox)
   print("Effected bboxes")
   print(bboxes)

   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   #cv2.imwrite("user_output/"+EFFECT+"/"+filename+"_"+EFFECT+".jpg", draw_rect(img,bboxes))
   cv2.imwrite("user_output/"+EFFECT+"/"+filename+"_"+EFFECT+".jpg", img)
   ann_file = open("user_output/"+EFFECT+"_ann/"+filename+"_"+EFFECT+".txt", "w")
   class_num = -1
   for bbox in bboxes:
      if int(bbox[4]) != class_num:
         class_num = int(bbox[4])
         ann_file.write(str(class_num)+" \n")
      ann_file.write(str(int(bbox[0]))+" "+str(int(bbox[1]))+" "+str(int(bbox[2]))+" "+str(int(bbox[3]))+" \n")
   ann_file.close()
      
     
   print("successed")
   #plt.imshow(draw_rect(img, bboxes))
   #plt.show()
print("done")
