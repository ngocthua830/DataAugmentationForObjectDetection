import os
from os import walk, getcwd
from PIL import Image

#classes = ["mouse", "telephone", "switch", "outlet", "clock", "toilet paper", "tissue box", "faucet", "plate", "jar"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    

#"""-------------------------------------------------------------------""" 

#""" Configure Paths"""   
mypath = "/home/thuan/git/DataAugmentationForObjectDetection/user_output/Original_ann"
outpath = "/home/thuan/git/DataAugmentationForObjectDetection/user_output/Original_ann_YOLO/"

cls = "mouse"
#if cls not in classes:
#    exit(0)
#ls_id = classes.index(cls)
 
wd = getcwd()

list_file = open('%s/%s_list.txt'%(wd, cls), 'w')

#""" Get input text file list """
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)
    break
#print(txt_name_list)

#""" Process """
for txt_name in txt_name_list:
    # txt_file =  open("Labels/stop_sign/001.txt", "r")
        
    #""" Open input text files """
    txt_path = mypath +"/"+ txt_name.replace(".jpg", ".txt")
    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    lines = txt_file.read().splitlines()   #for ubuntu, use "\r\n" instead of "\n"
    
    
    #""" Open output text files """
    txt_outpath = outpath + txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "w")
    
    
    #""" Convert the data to YOLO format """
    ct = 0
    #old = int(lines[0])
    #print(old)
    for line in lines:
        #print('lenth of line is: ')
        #print(len(line))
        #print('\n')
        if(len(line) <= 3):
            cls_id = int(line.strip())
            print(line,cls_id)
        else:
        	print(line)
        	t = line.strip().split(' ')
	        print("xmin: {0}, ymin: {1}, xmax: {2}, ymax:{3}".format(t[0], t[1], t[2], t[3]))
	        xmin = t[0]
	        ymin = t[1]
	        xmax = t[2]
	        ymax = t[3]
	        ct = ct + 1
	        #
	        img_path = str('%s/user_output/Original/%s.jpg'%(wd, os.path.splitext(txt_name)[0]))
	        #t = magic.from_file(img_path)
	        #wh= re.search('(\d+) x (\d+)', t).groups()
	        im=Image.open(img_path)
	        w= int(im.size[0])
	        h= int(im.size[1])
	        #w = int(xmax) - int(xmin)
	        #h = int(ymax) - int(ymin)
	        # print(xmin)
	        print(w, h)
	        b = (float(xmin), float(xmax), float(ymin), float(ymax))
	        bb = convert((w,h), b)
	        print(bb)
	        txt_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
	        #if(len(line) >= 2):
            	

    #""" Save those images with bb into list"""
    if(ct != 0):
        list_file.write('%s/%s.jpg\n'%(wd, os.path.splitext(txt_name)[0]))
                
list_file.close()    
