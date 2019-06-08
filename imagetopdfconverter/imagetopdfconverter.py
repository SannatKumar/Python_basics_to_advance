# This program converts image file into pdf

from PIL import Image 
import os

#The below mentioned code is the location, name and opening the image in redaimage variable
filename = "C:\\Users\\Raj\\Documents\\python_learning\\imagetopdfconverter\\my_image.jpg"
readimage  = Image.open(filename)

# the below code is to convert the image mode from RGBA to RGB
if readimage.mode =="RGBA":
    readimage = readimage.convert("RGB")

#The below name is the new name and location
new_filenanme = "C:\\Users\\Raj\\Documents\\python_learning\\imagetopdfconverter\\my_image.pdf"

#The below if checks if the same file name exist and the code below it saves the pdf file with the given parameters
if not os.path.exists(new_filenanme):
    readimage.save(new_filenanme, "PDF", resolution = 100.0)