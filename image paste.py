#이미지 붙여넣기

import cv2
import face_recognition
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

#face_image_path = 'data/without_mask/0.jpg'
face_image_path = 'Photo/person 1.jpg'
mask_image_path = 'data/mask.png'

person = face_image_path
image = cv2.imread(person, cv2.IMREAD_UNCHANGED)
grayImage = cv2.imread(person, cv2.IMREAD_GRAYSCALE)

face_cascade = cv2.CascadeClassifier(
    'C:/Users/user/PycharmProjects/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
face = face_cascade.detectMultiScale(grayImage, 1.01, 10)
eye_cascade = cv2.CascadeClassifier(
    'C:/Users/user/PycharmProjects/OpenCV/haarcascades/haarcascade_eye.xml')
eye = eye_cascade.detectMultiScale(grayImage, 1.01, 10)

a = {}
cnt = 0

for (x, y, w, h) in face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

    face_image_gray = grayImage[y:y + h, x:x + w]
    face_image_color = image[y:y + h, x:x + w]

    faces_in_body = face_cascade.detectMultiScale(face_image_gray)
    eyes_in_faces = eye_cascade.detectMultiScale(face_image_gray)

    for (xf, yf, wf, hf) in eyes_in_faces:
        a[cnt] = xf
        a[cnt + 1] = yf
        a[cnt + 2] = wf
        a[cnt + 3] = hf
        cv2.rectangle(face_image_color, (xf, yf), (xf + wf, yf + hf), (0, 255, 0), 2)
        cnt += 4

for i in range(0, 8):
    print(a[i])

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_image = Image.fromarray(face_image_np)

draw = ImageDraw.Draw(face_image)

for face_location in face_locations:
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]
    #draw.rectangle(((a[0], a[1]), (a[0] + a[2], a[1] + a[3])), outline=(255, 0, 0), width=4) #(left, top), (right, bottom)

#print(top, right, bottom, left)
width = (right - left)
height = (bottom - top)
a_width = (right + left) / 2
a_height = (bottom + top) / 2

#print(width, height, a_width, a_height)

mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((int(width), int(height)))

#face_image.paste(mask_image, (left, top), mask_image)
#face_image.paste(mask_image, (left, int(top * 1.3)), mask_image)
face_image.paste(mask_image, (left, int(top * 1.7)), mask_image)
#face_image.paste(mask_image, (left, int(a_height)), mask_image)
#face_image.paste(mask_image, (int(a_width), int(a_height)), mask_image)

face_image.show()

#print(type(face_image_np), type(face_image), type(mask_image))