import numpy as np

# 设置随机数生成器的种子，以确保结果的可重复性
np.random.seed(0)

# 定义特征的数量
num_features = 5

# 定义每组数据的大小
num_data_points = 20


# 定义特征的合理范围
feature_ranges = {
    'feature1': (0, 40),
    'feature2': (0, 20),
    'feature3': (0, 20),
    'feature4': (0, 10),
    'feature5': (0, 5)
}
classdict1={'feature1':'points',
            'feature2':'rebounds',
            'feature3':'assists',
            'feature4':'steals',
            'feature5':'blocks'}
# 生成数据
X = np.zeros((num_data_points, num_features))
for i in range(num_data_points):
    for j in range(num_features):
        # 从均匀分布中随机选择一个值
        X[i][j] = np.random.uniform(feature_ranges[f'feature{j+1}'][0], feature_ranges[f'feature{j+1}'][1])



# 打开一个文件用于写入，如果文件不存在则创建它
with open('NBAPlayers.txt', 'w') as file:
    # 遍历数组的每个元素
    for i in range(num_data_points):
        # 对于每行，将特征值用逗号分隔开来，并保留两位小数
        line = ' '.join(format(x, '.2f') for x in X[i])
        # 写入文件
        file.write(line + '\n')


