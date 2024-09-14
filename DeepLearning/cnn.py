

#load the data
from keras.preprocessing.image import ImageDataGenerator
from keras_preprocessing.image import load_img, img_to_array

train_datagen=ImageDataGenerator(rescale=1./255) #缩放，归一化
training_set=train_datagen.flow_from_directory('./caltech-101',target_size=(50,50),batch_size=32,class_mode='categorical')



from keras.models import Sequential
from keras.layers import Conv2D,MaxPool2D,Flatten,Dense

model=Sequential()
#卷积层
model.add(Conv2D(32,(3,3),input_shape=(50,50,3),activation='relu'))
#池化层
model.add(MaxPool2D(pool_size=(2,2)))
#卷积层
model.add(Conv2D(32,(3,3),activation='relu'))
#池化层
model.add(MaxPool2D(pool_size=(2,2)))
#展开
model.add(Flatten())
#全连接层
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=102,activation='softmax'))

#configure model
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.summary()

#train the model
model.fit(training_set,epochs=30)


from PIL import Image
import numpy as np
# 加载图像
img = Image.open('image_0011.jpg')
# 调整图像大小为 50x50
img_resized = img.resize((50, 50))
# 将图像转换为 numpy 数组并添加一个维度表示批次大小
pic = np.array(img_resized).reshape(1, 50, 50, 3)
ans=model.predict(pic)
print(ans)







