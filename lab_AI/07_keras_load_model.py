# # 07. keras_load_model.py
# import tensorflow as tf
# import matplotlib.pyplot as plt
#
# # 모델 로드
# model = tf.keras.models.load_model('../models/mymodel')
#
# print(model.summary())

#load model을 했을 때 trainable params가 100개에서 3200000개가 됨

#4번 코드에서 모델을 만드는 부분을 로드 모델로 대체함

# 04. keras_train_model.py
import tensorflow as tf
import matplotlib.pyplot as plt

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    validation_split=0.2,
    subset='training',
    seed=123,
    image_size=(224, 224),
    batch_size=16
)

valid_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    '../data/',
    validation_split=0.2,
    subset='validation',
    seed=123,
    image_size=(224, 224),
    batch_size=16
)

resize_and_crop = tf.keras.Sequential([
    tf.keras.layers.experimental.preprocessing.RandomCrop(height=224, width=224),
    tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
])

rc_train_dataset = train_dataset.map(lambda x, y: (resize_and_crop(x), y))
rc_valid_dataset = valid_dataset.map(lambda x, y: (resize_and_crop(x), y))

# model = tf.keras.applications.MobileNet(
#     input_shape=(224, 224, 3),
#     include_top=False, #마지막 출력 없앰
#     weights='imagenet'
# )
# 모델 로드
model = tf.keras.models.load_model('../models/mymodel')

model.layers[0].trainable = False
model.layers[2].trainable = True

model.trainable = False

print(model.summary())

model = tf.keras.Sequential([
    model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(1)
])

learning_rate = 0.0001
model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.RMSprop(lr=learning_rate),
    metrics=['accuracy'] #부가정보 표현하는 코드 (accuracy -> 정확도 나오게 만듬)
)

print(model.summary())

history = model.fit(rc_train_dataset, epochs=2, validation_data=rc_valid_dataset)
print(history)