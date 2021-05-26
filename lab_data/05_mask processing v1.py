# 얼굴 랜드마크 추출

import face_recognition
from PIL import Image, ImageDraw

#face_image_path = 'data/without_mask/0.jpg'
face_image_path = '../Photo/person 2.jpg'
mask_image_path = '../data/mask.png'

face_image_np = face_recognition.load_image_file(face_image_path)
face_image = Image.fromarray(face_image_np)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

face_landmark_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmark_image)

for face_landmark in face_landmarks:
    for feature_name, points in face_landmark.items():
        print(feature_name, points)
        for point in points:
            draw.point(point)

#face_landmark_image.show()
# draw.point((10, 10))

width = face_landmark['chin'][16][0] - face_landmark['chin'][0][0]

if face_landmark['left_eye'][0][1] < face_landmark['chin'][8][1]:
    height = face_landmark['chin'][8][1] - face_landmark['left_eye'][0][1]

    mask_image = Image.open(mask_image_path)
    mask_image = mask_image.resize((width, height))

    face_image.paste(mask_image, (face_landmark['chin'][0][0], face_landmark['left_eye'][0][1]), mask_image)
    face_image.show()

else:
    height = face_landmark['chin'][8][1] - face_landmark['nose_bridge'][0][1]

    mask_image = Image.open(mask_image_path)
    mask_image = mask_image.resize((width, height))

    face_image.paste(mask_image, (face_landmark['chin'][0][0], face_landmark['chin'][0][1]), mask_image)
    face_image.show()
'''
height = face_landmark['chin'][8][1] - face_landmark['nose_bridge'][0][1]

print(width, height)

mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((width, height))

face_image.paste(mask_image, (face_landmark['chin'][0][0], face_landmark['chin'][0][1]), mask_image)
face_image.show()
'''