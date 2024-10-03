import pandas as pd
import numpy as np


# 生成正常苹果的二维数据（横径和纵径）
num_normal_apples = 100

# 正常苹果横径范围假设为6 - 10厘米
normal_diameter_x = np.random.uniform(6, 10, num_normal_apples)
# 正常苹果纵径范围假设为5 - 9厘米
normal_diameter_y = np.random.uniform(5, 9, num_normal_apples)

# 生成异常苹果的二维数据
num_abnormal_apples = 10

# 异常苹果横径（过小或过大）
abnormal_diameter_x = np.append(np.random.uniform(3, 5, num_abnormal_apples // 2), np.random.uniform(11, 13, num_abnormal_apples // 2))
# 异常苹果纵径（过小或过大）
abnormal_diameter_y = np.append(np.random.uniform(2, 4, num_abnormal_apples // 2), np.random.uniform(10, 12, num_abnormal_apples // 2))


# 合并数据
diameter_x = np.append(normal_diameter_x, abnormal_diameter_x)
diameter_y = np.append(normal_diameter_y, abnormal_diameter_y)

# 创建数据框
data = pd.DataFrame({
    'Diameter_X': diameter_x,
    'Diameter_Y': diameter_y
})

# 打乱数据顺序
data = data.sample(frac=1).reset_index(drop=True)

# 保存为CSV文件
data.to_csv('2d_apple_anomaly_detection_data.csv', index=False)