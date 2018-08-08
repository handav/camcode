import cv2
import numpy as np
from matplotlib import pyplot as plt

#0 means read in the grayscale image
#pixels in grayscale have 1 number between 0 and 255
#pixels in color have three numbers, usually representing RGB (red green blue)
#cv2 is weird in that it is BGR (blue green red)
img = cv2.imread('insta_pics/3.jpg',0)
pixels_in_a_list = img.ravel()
#print(pixels_in_a_list)
plt.hist(pixels_in_a_list,256,[0,256]) 
plt.show()

print('Mean: ', np.mean(pixels_in_a_list))
print('StDev: ', np.std(pixels_in_a_list))


