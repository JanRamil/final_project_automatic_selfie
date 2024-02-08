# Final Project
# Create a code that will automatically take selfie 
# Create a code that will save the selfie in your files

# Creating pseudocode

# Import necessary modules
import cv2
import os

# Path to Downloads folder
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# For capture
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')