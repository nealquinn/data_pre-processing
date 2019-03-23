import glob
import os
import cv2
import concurrent.futures

def load_and_resize(image_filename):
### Read in the image data
  img = cv2.imread(img_filename)
  
### Resize the image
  img = cv2.resize(img, (600, 600))
  
### Create a pool of processes. By default, one created for each CPU in your machine. 
with concurrent.futures.ProcessPoolExecutor() as executor:
  ### Get a list of files to process
    image_files = glob.glob("*.jpg")
    
  ### Process the list of files, but split the work across the process pool to use all CPUs
  ### Loop though all jpg files in the current folder
  ### Resize each one to the size 600x600
    executor.map(load_and_resize, image_files)
