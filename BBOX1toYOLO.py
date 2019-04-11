#FROM PASCAL VOC
#<class>
#<xmin> <xmax> <ymin> <ymax>
#<xmin> <xmax> <ymin> <ymax>
#<class>
#<xmin> <xmax> <ymin> <ymax>
#TO YOLO
#<class> <x> <y> <width> <height>
#in
#<class> number of object from 0 to (classes-1)
#<x> = <absolute_x> / <image_widht>
#<y> = <absolute_y> / <image_height>
#<x> <y> center of rectangle
######################################################
import glob

IMG_PATH = "/home/thuan/git/DataAugmentationForObjectDetection/user_output/RandomHorizontalFlip_1/"
LABEL_PATH = "/home/thuan/git/DataAugmentationForObjectDetection/user_output/RandomHorizontalFlip_1_ann/"
LABEL_PATH_OUT = "/home/thuan/git/DataAugmentationForObjectDetection/user_output/RandomHorizontalFlip_1_ann_YOLO/"

class_num = "-1"

#img_filename = IMG_PATH+'COCO_train2014_000000000643_RandomHorizontalFlip_1.jpg'
img_filename = IMG_PATH+'sun_aajmgjyzfecnphxv_RandomHorizontalFlip_1.jpg'

splited_img_filename = img_filename.split('/')
label_filename = LABEL_PATH + splited_img_filename[len(splited_img_filename)-1].split('.')[0] + ".txt"

label_file = open(label_filename, 'r')
label_lines = [i.rstrip() for i in label_file.readlines()]

label_filename_out = LABEL_PATH_OUT + splited_img_filename[len(splited_img_filename)-1].split('.')[0] + ".txt"
label_file_out = open(label_filename_out, 'w')

print(label_lines)
for label_line in label_lines:
   print(label_line)
   if len(label_line) < 3:
      class_num = label_line
   else:
      label_file_out.write(
label_file_out.close()

