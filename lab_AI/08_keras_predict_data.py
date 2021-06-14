# 08. keras_predict_data
import tensorflow as tf
import matplotlib.pyplot as plt

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    validation_split=0.2,
    subset='training',
    # 학습용으로 사용하는 데이터
    seed=123,
    image_size=(224, 224),
    batch_size=16
    # 원본 데이터보다 작게 만들어 연산량 줄이는 용도, 전체 데이터 학습시키는 것과 비슷한 효과
)

valid_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    validation_split=0.2,
    subset='validation',
    seed=777,
    image_size=(224, 224),
    batch_size=16
)

resize_and_crop = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.RandomCrop(height=224, width=224),
    tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
    # 0 ~ 255값을 가지는 것을 0 ~ 1 사이의 값으로 만들어줌
])

# map 함수 사용
rc_train_dataset = train_dataset.map(lambda x, y: (resize_and_crop(x), y))
rc_valid_dataset = valid_dataset.map(lambda x, y: (resize_and_crop(x), y))

# 모델 로드
model = tf.keras.models.load_model('../models/mymodel')

print(model.summary())

plt.figure(0)
plt.title('Valid Dataset Predict')

for images, labels in valid_dataset.take(1):
    rc_images = resize_and_crop(images)
    # resize_and_crop 함수에 images 를 넣어 이미지 크기 변환
    predict = model.predict(rc_images)
    print(predict)

    for i in range(16):
        plt.subplot(4, 4, i + 1)
        plt.imshow(images[i].numpy().astype('uint8'))
        # numpy 배열로 전환

        if predict[i][0] > 0.5:
            predict_index = 1
        else:
            predict_index = 0

        # 예측 결과가 정답이면 OK 아니면 Wrong
        if labels[i] == predict_index:
            # labels -> 정답값
            result = 'OK'
        else:
            result = 'Wrong'

        plt.title(valid_dataset.class_names[predict_index] + '\n' + result)
        plt.axis('off')

plt.show()