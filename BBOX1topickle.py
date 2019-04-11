import pickle as pkl
import numpy as np
import glob

bboxes = np.empty(shape=(5,))
for filename in glob.glob("/home/thuan/CV/DataAugmentation/small_object_dataset/train_annotation/*.txt"):
   bboxes_list = []
   print(filename)
   splited = filename.split('/')
   filename_ex = splited[len(splited)-1].split('.')[0]
   print(filename_ex)
   with open(filename, 'r') as f:
      lines = f.readlines()
   for line in lines:
      line = line.rstrip()
      if line.count(' ') <= 2:
         class_num = int(line)*1.0
      else:
         coor = [int(i)*1.0 for i in line.split()]
         replace_coor = [coor[0], coor[1], coor[2], coor[3], class_num]
         bboxes_list.append(replace_coor)
         #print(coor)
#print(bboxes_list)
   bboxes = np.array(bboxes_list)
#bboxes = np.array([[53, 68, 405, 478], [202, 20, 469, 489, 0], [589, 77, 737, 335, 0], [589, 77, 737, 335, 0], [723, 327, 793, 396, 1]])
#bboxes = np.zeros((3,4))
#bboxes = np.array([[53.,68.,405.,478.], [202.,20.,469.,489.], [589., 77., 737., 335.], [723., 327., 793., 396.]])
   outfile = open("/home/thuan/CV/DataAugmentation/small_object_dataset/converted/"+filename_ex+".pkl", 'wb')
   pkl.dump(bboxes, outfile)
   outfile.close()
   print(bboxes)
#for i in bboxes:
##   print(i[3])
