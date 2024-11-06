import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt
# 設定資料集的參數
min_value = -12
max_value = 12
num_datapoints = 121
# 產生資料集
x = np.linspace(min_value, max_value, num_datapoints)
y = 2*np.square(x)+7
y /= np.linalg.norm(y)
# 將資料集轉化成適合輸入神經網路的形狀
data = x.reshape(num_datapoints, 1)
labels = y.reshape(num_datapoints, 1)
# 畫圖看資料以及標籤
plt.figure()
plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Input")
plt.show()
# 定義每一層激勵函數
transfun = [nl.trans.TanSig(), nl.trans.TanSig(), nl.trans.LogSig()]
# 呼叫多層感知器，第二個變數決定神經網路的結構、形狀
multilayer_net = nl.net.newff([[min_value, max_value]], [20, 20, 1], transf = transfun)
# 指定權重更新的演算法
multilayer_net.trainf = nl.train.train_gd
# 訓練神經網路
error = multilayer_net.train(data, labels, epochs = 100000, show=100, goal=0.0001)
# 計算預測數值
predicted_output = multilayer_net.sim(data)
# 畫圖顯示訓練過程
plt.figure()
plt.plot(error)
plt.xlabel("Number of epochs")
plt.ylabel("Training Error")
plt.yscale("log")
plt.grid()
plt.title("Training Error Progress")
plt.show()
# 畫圖顯示實際值、預測值對比
y3 = predicted_output.reshape(num_datapoints)
plt.figure()
plt.plot(x, y, '-', x, y3, 'p')
plt.title("Truth vs Predict")
plt.show()

