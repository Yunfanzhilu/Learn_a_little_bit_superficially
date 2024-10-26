"""
任务说明：基于jaychou_lyrics.txt文本数据(里面是周杰伦的歌词)，建立LSTM模型并预测周杰伦的歌词
1.完成数据预处理，将文字序列数据转化为可用于LSTM输入的数据
2.查看文字数据预处理后的数据结构，并进行数据分离操作
3.针对字符串输入("你好，晴天")，预测其对应的后续字符
备注：模型结构，单层LSTM，输出有20个神经元，每次使用前20个汉字预测第21个汉字

"""

#load the data
data=open('test2.txt').read()
#移除换行符
data=data.replace('\n','').replace('\r','')
print(data)

#字符去重处理
letters=list(set(data))
print(letters)
num_letters=len(letters)
print(num_letters)

#建立字典
int_to_char={a:b for a,b in enumerate(letters)}
print(int_to_char)
char_to_int={b:a for a,b in enumerate(letters)}
print(char_to_int)

#字符批量处理转换为one-hot格式
time_step=20
import numpy as np
from keras.utils import to_categorical
def extract_data(data,slide):
    x=[]
    y=[]
    for i in range(len(data)-slide):
        x.append([a for a in data[i:i+slide]])
        y.append(data[i+slide])
    return x,y
    #字符到数字的批量转化
def char_to_int_Data(x,y,char2int):
    x_to_int=[]
    y_to_int=[]
    for i in range(len(x)):
        x_to_int.append([char2int[char] for char in x[i]])
        y_to_int.append([char2int[char] for char in y[i]])
    return x_to_int,y_to_int
#实现输入字符文章的批量处理，出入整个字符，滑动窗口大小，转化字典
def data_preprocessing(data,slide,num_letters,char2int):
    char_Data=extract_data(data,slide)
    int_Data=char_to_int_Data(char_Data[0],char_Data[1],char2int)
    Input=int_Data[0]
    Output=list(np.array(int_Data[1]).flatten())
    Input_RESHAPED=np.array(Input).reshape(len(Input),slide)
    new=np.random.randint(0,10,size=[Input_RESHAPED.shape[0],Input_RESHAPED.shape[1],num_letters])
    for i in range(Input_RESHAPED.shape[0]):
        for j in range(Input_RESHAPED.shape[1]):
            new[i,j,:]=to_categorical(Input_RESHAPED[i,j],num_classes=num_letters)
    return new,Output

#define X and y from data
X,y=data_preprocessing(data,time_step,num_letters,char_to_int)
print(f"X={X},\nsize={X.shape}")
print(f"y={y},\nsize={len(y)}")


#split the data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=10)
print(f"X_train={X_train},\nsize={X_train.shape}")
print(f"y_train={y_train},\nsize={len(y_train)}")
#y也转换成one_hot
y_train_category=to_categorical(y_train,num_letters)
print(f"y_train_category={y_train_category}")

#建立LSTM模型
from keras.models import Sequential
from keras.layers import Dense,LSTM
model=Sequential()
model.add(LSTM(units=20,input_shape=(X_train.shape[1],X_train.shape[2]),activation='relu'))
model.add(Dense(units=num_letters,activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.summary()

#train the model
model.fit(X_train,y_train_category,batch_size=100,epochs=10)

#基于训练数据进行预测
y_train_predict=model.predict_step(X_train)
# 将 Tensor 对象转换为 NumPy 数组
y_train_predict_np = y_train_predict.numpy()
# 转换成字符
y_train_predict_char = [int_to_char[int(i)] if int(i) in int_to_char else None for i in y_train_predict_np.flatten()]
print(y_train_predict_char)


