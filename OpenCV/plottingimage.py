import numpy as np
import cv2
from matplotlib import pyplot as plt

#for grayscale image
#img = cv2.imread('lena10.jpg', 0) 
#"lena10.jpg" should be replace by the name of your image and needs to be in the same folder 

#for bgr image
#img = cv2.imread('lena10.jpg', 1)

#the code below works to convert the image into RGB from BGR mode
img2 = cv2.imread('lena10.jpg', 1) 
img = img2[:, :, ::-1]
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])#to hide tick values on x axis and y axis
plt.show()