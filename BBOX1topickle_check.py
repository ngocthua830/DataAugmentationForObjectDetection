import pickle as pkl
import sys
bboxes = pkl.load(open(sys.argv[1], "rb"))
print(bboxes)
