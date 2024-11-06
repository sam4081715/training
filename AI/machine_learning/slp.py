import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

# 產生資料以及標籤
data = np.array([[0.9, 4.1], [0.8, 3.9], [1.1, 3.8], [4.2, 0.8], [4.3, 0.9], [3.5, 0.7], [4.2, 7.8], [4.1, 6.9], [3.7, 6.8]])
labels = np.array([[0,0], [0,0], [0,0], [1,0], [1,0], [1,0], [0,1], [0,1], [0,1]])
# 畫圖看資料以及標籤
plt.figure()
plt.scatter(data[:,0], data[:,1], c = 2*labels[:,1]+1*labels[:,0])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Input")
plt.show()
# 設定神經網路的輸入上下限
x_min = 0
x_max = 10
y_min = 0
y_max = 10
# 呼叫單層感知器，輸出維度為2
perceptron = nl.net.newp([[x_min, x_max],[y_min, y_max]], 2)
# 訓練單層感知器
error = perceptron.train(data, labels, epochs = 50, show = 10, lr = 0.01)
# 畫圖顯示訓練過程
plt.figure()
plt.plot(error)
plt.xlabel("Number of epochs")
plt.ylabel("Training Error")
plt.grid()
plt.title("Training Error Progress")
plt.show()
# 測試神經網路
test_data = np.array([[1,4], [4,1], [4,7]])
print(perceptron.sim(test_data))