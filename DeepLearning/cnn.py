""""
这是一个基于keras的图像分类任务

数据集：kaggle平台 CIFAR-10
链接：https://www.kaggle.com/datasets/pankrzysiu/cifar10-python?resource=download
简介：
CIFAR-10 数据集：
该数据集包含 10 个不同的类别，如飞机、汽车、鸟、猫、鹿、狗、青蛙、马、船和卡车，共有 60000 张彩色图像，其中 50000 张用于训练，10000 张用于测试。
图像的尺寸较小（32x32 像素），便于快速训练和实验。CIFAR-10 是一个广泛用于研究和教学的基准数据集，对于学习和比较不同的图像分类算法非常有用。
"""
#load the data
import pickle

import numpy as np
from matplotlib import pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras_preprocessing.image import load_img, img_to_array


# 读取 CIFAR-10 训练集数据

def load_cifar10_data(data_path):
    data = []
    labels = []
    for i in range(1, 6):
        with open(f'{data_path}/data_batch_{i}', 'rb') as f:
            batch = pickle.load(f, encoding='bytes')
            data.append(batch[b'data'])
            labels.extend(batch[b'labels'])
    return np.concatenate(data), np.array(labels)



# 加载数据
data_path='./CIFAR-10/cifar-10-batches-py'
X_train, y_train = load_cifar10_data(data_path)

# 转换图像形状
X_train = X_train.reshape(-1, 32, 32, 3)
# 缩放，归一化
X_train = X_train / 255.0




from keras.models import Sequential
from keras.layers import Conv2D,MaxPool2D,Flatten,Dense

model=Sequential()
#卷积层
model.add(Conv2D(32,(6,6),input_shape=(32,32,3),activation='relu'))
#池化层
model.add(MaxPool2D(pool_size=(2,2)))
#卷积层
model.add(Conv2D(32,(6,6),activation='relu'))
#池化层
model.add(MaxPool2D(pool_size=(2,2)))
#展开
model.add(Flatten())
#全连接层
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=102,activation='softmax'))

#configure model
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.summary()

#train the model
model.fit(X_train, y_train, epochs=60)

#save thr model
model.save('CIFAR-10.h5')


# 加载测试集数据
def load_cifar10_test_data(data_path):
    with open(f'{data_path}/test_batch', 'rb') as f:
        batch = pickle.load(f, encoding='bytes')
        return batch[b'data'], np.array(batch[b'labels'])

# 加载模型
from keras.models import load_model
model = load_model('CIFAR-10.h5')



# 加载测试集
X_test, y_test = load_cifar10_test_data(data_path)
X_test = X_test.reshape(-1, 32, 32, 3)
X_test = X_test / 255.0

# 预测测试集
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)

# 计算正确率
accuracy = np.sum(predicted_classes == y_test) / len(y_test)
print(f'Test accuracy: {accuracy}')

# 可视化一些测试集图片及预测
# 展示图片资料
num_images_to_show = 5
plt.figure(figsize=(15, 3))
for i in range(num_images_to_show):
    plt.subplot(1, num_images_to_show, i + 1)
    plt.imshow(X_test[i])
    plt.title(f'Actual: {y_test[i]}, Predicted: {predicted_classes[i]}')
plt.show()