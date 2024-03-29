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

# For loop
selfie_captured = False
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(face_gray, scaleFactor=1.3, minNeighbors=5, minSize=(25, 25))

        # Draw rectangles around the smiles
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(face_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

            # Save selfie when a smile is detected
            if not selfie_captured:
                selfie_filename = 'selfie.png'
                selfie_path = os.path.join(downloads_path, selfie_filename)
                cv2.imwrite(selfie_path, frame)
                selfie_captured = True
                
    cv2.imshow('cam star', frame)
    if cv2.waitKey(10) == ord('q'):
        break

# Release the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
