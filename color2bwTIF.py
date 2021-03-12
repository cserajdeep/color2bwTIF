########################### Original code for RGB to B&W TIF ###############################

import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray

def RGB2BW_TIF(src,dest):
    for file_name in os.listdir(src):
        if file_name.endswith((".jpg",".jpeg",".png",".tiff",".tif")):
            # if it's a jpg file, print its name (or do whatever you want)
            #print(file_name)
            f = file_name.split('.')[0]
            print(f)
            
            img = io.imread(src+'/'+file_name) # Read in Gray Scale
            #gray =  rgb2gray(img)
            
            # Now we put it back in Pillow/PIL land
            bw_img = Image.fromarray(img)
            newsize = (448,448) 
            bw_img = bw_img.resize(newsize)                    # Resize image
            bw_img.save(dest+'/'+f+".tiff", 'TIFF')
            
    return 'Success!!'
            
#### call the conversion function
src='masks'
dest='bw_imgs'

result = 'FAILED!!'
result = RGB2BW_TIF(src,dest)
print(result)