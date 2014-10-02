import os,sys

import pprint
sys.displayhook = pprint.pprint
import Image
import numpy

print "xx"
def MyWho():
       print [v for v in globals().keys() if not v.startswith('_')]

x= 0
locals()

MyWho()path = "/Users/sephon/Desktop/Research/ReVision/code/ImageSeg/corpus/pm_ee_cat_0_multi/image_8.jpg"
image = Image.open(path)
# image.show();
