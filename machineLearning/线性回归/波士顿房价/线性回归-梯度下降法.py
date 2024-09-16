import numpy as np
import matplotlib.pyplot as plt

class LinearRegressionGD:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# 生成数据
np.random.seed(42)
n_samples = 100
X = np.random.randn(n_samples, 1)
y = 2 * X.squeeze() + 3 + np.random.randn(n_samples) * 0.5

# 使用自定义的线性回归梯度下降类
lr_gd = LinearRegressionGD(learning_rate=0.01, n_iterations=1000)
lr_gd.fit(X, y)

# 可视化结果
plt.scatter(X, y, c='blue', marker='o', label='Data')
plt.plot(X, lr_gd.predict(X), color='red', label='Gradient Descent')
plt.title('Linear Regression with Gradient Descent')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()