import cv2
from PIL import Image
import numpy as np


image = Image.open('imgs/lot2.jpg')
car_cascade = cv2.CascadeClassifier('cars.xml')

image = image.resize((450,250))
image_arr = np.array(image)

grey = cv2.cvtColor(image_arr,cv2.COLOR_BGR2GRAY)
Image.fromarray(grey)

blur = cv2.GaussianBlur(grey,(5,5),0)
Image.fromarray(blur)

dilated = cv2.dilate(blur,np.ones((3,3)))
Image.fromarray(dilated)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel) 
Image.fromarray(closing)

cars = car_cascade.detectMultiScale(closing, 1.1, 1)

cnt = 0
for (x,y,w,h) in cars:
  cv2.rectangle(image_arr,(x,y),(x+w,y+h),(255,0,0),2)
  cnt += 1
print(cnt, " cars found")
Image.fromarray(image_arr)
