import numpy as np
import neurolab as nl
import matplotlib.pyplot as plt
# 產生資料的函數
def create_waveform(num_points):
    data1 = 1 * np.cos(np.arange(0, num_points))
    data2 = 2 * np.cos(np.arange(0, num_points))
    data3 = 3 * np.cos(np.arange(0, num_points))
    data4 = 4 * np.cos(np.arange(0, num_points))
    amp1 = np.ones(num_points)
    amp2 = 4 * np.ones(num_points)
    amp3 = 2 * np.ones(num_points)
    amp4 = 0.5 * np.ones(num_points)
    data = np.array([data1, data2, data3, data4]).reshape(num_points*4, 1)
    amplitude = np.array([amp1, amp2, amp3, amp4]).reshape(num_points*4, 1)
    return data, amplitude
# 產生資料並丟入模型預測，並畫出結果
def draw_output(net, num_points_test):
    data_test, amplitude_test = create_waveform(num_points_test)
    output_test = net.sim(data_test)
    plt.plot(data_test)
    plt.plot(amplitude_test)
    plt.plot(output_test)
    
# 設定訓練資料長度
num_points = 30
# 產生資料
data, amplitude = create_waveform(num_points)
# newelm為Elman遞迴神經網路，將data以及amplitude丟入訓練，設定激勵函數。
net = nl.net.newelm([[-4, 4]], [10, 1], [nl.trans.TanSig(), nl.trans.PureLin()])
# 設定Loss的計算發方法為MSE
net.trainf.defaults['errorf'] = nl.error.MSE()
# 設定權重(w)、偏移(b)初始化在-1跟1之間的隨機數
net.layers[0].initf = nl.init.InitRand([-1, 1], 'wb')
net.layers[1].initf = nl.init.InitRand([-1, 1], 'wb')
# 初始化神經網路權重
net.init()
# 開始訓練並回傳訓練過程誤差
error = net.train(data, amplitude, epochs=5000, show=100, goal=0.01)
# 測試神經網路
output = net.sim(data)
# 畫訓練過程誤差
plt.subplot(211)
plt.plot(error)
plt.xlabel('Number of epochs')
plt.ylabel('Error')
# 畫實際結果vs預測結果
plt.subplot(212)
plt.plot(amplitude)
plt.plot(output)
plt.legend(['Truth', 'Predicted'])
plt.show()
# 測試不同資料大小的影響
plt.figure()
plt.subplot(211)
draw_output(net, 74)
plt.xlim([0, 300])
plt.subplot(212)
draw_output(net, 54)
plt.xlim([0, 300])
plt.show()





 



