import cv2
import numpy as np 
import argparse
import time

# construct argument parse and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")

args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["image"])

