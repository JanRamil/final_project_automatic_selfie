# Final Project
# Create a code that will automatically take selfie 
# Create a code that will save the selfie in your files

# Creating pseudocode

# Import necessary modules
import cv2
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Path to Downloads folder
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')