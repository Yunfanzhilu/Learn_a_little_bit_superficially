"""
任务：根据original_data样本，建立模型，对test_data的图片进行苹果/西红柿判断(数据集中包含苹果和西红柿两类，由于两者形状颜色较为接近，区分起来有难度)
1.数据增强，扩充确认为苹果的样本数量（略）
2.特征提取，使用VGG16模型提取图像特征
3.图片批量处理
4.Kmeans模型尝试普通、其他苹果类
5.基于标签数据矫正结果，并可视化
6.Meanshift模型提升模型表现
7.数据降维PCA处理，提升模型表现
"""


"""
#1.数据增强，扩充确认为苹果的样本数量（略）
from keras.preprocessing.image import ImageDataGenerator
path='appleClassify_\\preprocess\\originalData\\apple'
dst_path='appleClassify_\\preprocess\\genData'
datagen=ImageDataGenerator(rotation_range=10,width_shift_range=0.1,height_shift_range=0.02,horizontal_flip=True,vertical_flip=True)#旋转、平移、垂直平移、水平旋转、垂直旋转
gen=datagen.flow_from_directory(path,target_size=(224,224),batch_size=2,save_to_dir=dst_path,save_prefix='gen',save_format='jpg')
for i in range(100):
    gen.next()
"""


from keras.preprocessing.image import ImageDataGenerator
from keras_preprocessing.image import load_img, img_to_array

#加载图片
img_path="appleClassify_/train/apples/img_p1_4.jpeg"
img=load_img(img_path,target_size=(224,224))#224*224是VGG模型的要求
print(type(img))#numpy.ndayyay

"""
#可视化图片
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
fig1=plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()
img=img_to_array(img)
"""

#导入VGG16模型作为特征提取的模型(注意：仅保留VGG模型的卷积特征提取部分，VGG的全连接层和输出层我们自己建立mlp模型)
from keras.applications.vgg16 import VGG16,preprocess_input
import numpy as np
model_vgg=VGG16(weights='imagenet',include_top=False)#include_top=False指不需要VGG后面的全连接层和输出层
X=np.expand_dims(img,axis=0)#添加一个维度，是图片变成224*224*3的维度，这是VGG的模型输入要求
X=preprocess_input(X)
print(X.shape)#(1, 224, 224, 3)

#特征提取
features=model_vgg.predict(X)
print(features.shape)#(1,7*7*512)

#flatten展开
features=features.reshape(1,7*7*512)
print(features.shape)#(1, 25088)


#define a method to extract the features
def modelProcess(img_path,model):
    img=load_img(img_path,target_size=(224,244))
    img=img_to_array(img)
    X=np.expand_dims(img,axis=0)
    X=preprocess_input(X)
    X_VGG=model.predict(X)#特征提取，就这一句话
    X_VGG=X_VGG.reshape(1,7*7*512)
    return X_VGG


#批量处理苹果图片
import os
folder_apples='appleClassify_/train/apples'
dirs=os.listdir(folder_apples)
#名称合并
img_path_apples=[]
for i in dirs:
    if os.path.splitext(i)[1]=='.jpeg':
        img_path_apples.append(i)
img_path_apples=[folder_apples+'//'+i for i in img_path_apples]
print(img_path_apples)
features_apples=np.zeros([len(img_path_apples),7*7*512])#行数、列数 单张图片特征数量
for i in range(len(img_path_apples)):
    feature_i=modelProcess(img_path_apples[i],model_vgg)
    print('preprocessed:',img_path_apples[i])
    features_apples[i]=feature_i
print(features_apples.shape)#(164, 25088)
#给苹果图片打标签
y_apple_label=np.zeros(164)



#批量处理土豆图片
import os
folder_tomatoes='appleClassify_/train/tomatoes'
dirs=os.listdir(folder_tomatoes)
#名称合并
img_path_tomatoes=[]
for i in dirs:
    if os.path.splitext(i)[1]=='.jpeg':
        img_path_tomatoes.append(i)
img_path_tomatoes=[folder_tomatoes+'//'+i for i in img_path_tomatoes]
print(img_path_tomatoes)



#图像批量处理
features_tomatoes=np.zeros([len(img_path_tomatoes),7*7*512])#行数、列数 单张图片特征数量
for i in range(len(img_path_tomatoes)):
    feature_i=modelProcess(img_path_tomatoes[i],model_vgg)
    print('preprocessed:',img_path_tomatoes[i])
    features_tomatoes[i]=feature_i
print(features_tomatoes.shape)#(130, 25088)
#给西红柿图片打标签
y_tomatoes_label=np.ones(130)



#苹果和土豆图片体征提取出来合成一个训练集
X_train=np.concatenate((features_apples,features_tomatoes),axis=0)#(294, 25088)
y_train=np.concatenate((y_apple_label,y_tomatoes_label),axis=0)
y_train=y_train.reshape(-1,1)
print(y_train.shape)#(294, 1)


#建立mlp模型
from keras.models import Sequential
from keras.layers import Dense
model=Sequential()
model.add(Dense(units=10,activation='relu',input_dim=25088))
model.add(Dense(units=5,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
model.summary()
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#训练模型
model.fit(X_train,y_train,epochs=20)

#预测训练集数据准确率
from sklearn.metrics import accuracy_score
y_train_predict_prob=model.predict(X_train)
threshold=0.5
y_train_predict=[]
for i in y_train_predict_prob:
    if i>0.5:
        y_train_predict.append(1)
    else:
        y_train_predict.append(0)
print(y_train_predict)
accuracy_train=accuracy_score(y_train,y_train_predict)
print(accuracy_train)#0.96

#预测测试集准确率










