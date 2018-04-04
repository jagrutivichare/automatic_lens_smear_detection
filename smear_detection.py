# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 01:31:00 2018

@author: Sabareesh, Jagruti, Naveen
"""
#Including numpy, scipy opencv libraries 
import numpy as npy
import cv2
import sys
import scipy.ndimage as scindi
from glob import glob
from skimage.filters import threshold_adaptive

def smear_detection(path):
    numpy_array = npy.zeros((500,500,3),dtype=float)
    #Loading input images
    img_path = path+'/*.jpg'
    img_data = glob(img_path)
    N = len(img_data)
    #Calculation of average image for the sequence of images
    for i in img_data:    
        image = cv2.imread(i)
        img = cv2.resize(image,(500,500))
        numpy_arrayimage = npy.array(img,dtype=float)   
        numpy_array = numpy_array + (numpy_arrayimage/N)
    numpy_array = npy.array(npy.round( numpy_array), dtype=npy.uint8)  
    #Display average image
    cv2.imshow('AverageImg',numpy_array)
    cv2.waitKey()
    cv2.imwrite('AverageImg.jpg',numpy_array)

    numpy_array=cv2.imread("AverageImg.jpg",0)
    image_mask = numpy_array.astype(npy.uint8)

    #To smoothen,Sharpen and removal of noise in the image
    gaussian_image = scindi.gaussian_filter(image_mask, (10,10))
    cv2.imshow('Gaussian Filter Image',gaussian_image)
    cv2.waitKey()
    cv2.imwrite('GaussianFilterImg.jpg',gaussian_image)
    
    #Perform adaptive threshold on gaussian filtered image
    threshold_image = threshold_adaptive(gaussian_image, 255, offset = 10)
    threshold_average_image = threshold_image.astype(npy.uint8) * 255
    cv2.imshow('Adaptive Threshold image',threshold_average_image) 
    cv2.waitKey()
    cv2.imwrite('AdaptiveThresholdImg.jpg',threshold_average_image)

    #To find the outer edges of the Smear
    edge_detection_image = cv2.Canny(threshold_average_image, 200, 200)
    cv2.imshow("Edge Detection Image",edge_detection_image) 
    cv2.waitKey()
    cv2.imwrite("EdgeDetectionImg.jpg",edge_detection_image)

    #To draw Contours to identify smear in the image
    (_,cnts,_) = cv2.findContours(edge_detection_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    average_image=cv2.imread("AverageImg.jpg");
    cv2.drawContours(average_image,cnts,-1,(0,0,255),2)
    cv2.imshow("Final Output",average_image)
    cv2.imwrite("FinalOutputImg.jpg",average_image)
    cv2.waitKey()         
    cv2.destroyAllWindows()

if __name__ == "__main__":
    arguments = sys.argv[1:]
    #To check the path of image directory
    if len(sys.argv) < 2:
        print("Please provide path to the image folder")
        sys.exit(1)
    print("Processing images from the path provided for smear detection")
    smear_detection(sys.argv[1])