import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt

# 產生資料
data = np.array([[0.1, 0.2],[0.3, 0.1], [0.4, 0.1], [0.5, 0.9]])
# 產生對應的標籤
labels = np.array([[0],[0],[0],[1]])
# 畫圖看資料以及標籤
plt.figure()
plt.scatter(data[:,0], data[:,1], c = labels[:,0])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Input")
plt.show()
# 呼叫感知器，定義輸入參數的上下限、輸出數量
perceptron = nl.net.newp([[0,1],[0,1]], 1)
# 開始訓練感知器，設定訓練次數epochs、顯示訓練誤差的間隔show、學習率lr
error = perceptron.train(data, labels, epochs = 50, show = 10, lr = 0.01)
# 畫圖顯示訓練過程
plt.figure()
plt.plot(error)
plt.xlabel("Number of epochs")
plt.ylabel("Training Error")
plt.grid()
plt.title("Training Error Progress")
plt.show()
# 測試感知器
test_data = np.array([[0.5, 0.9], [0.3, 0.3]])
print(perceptron.sim(test_data))
