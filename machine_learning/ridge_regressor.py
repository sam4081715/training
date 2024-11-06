import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from metric import show_metrics
import pickle
# 抓取cmd輸入的參數
filename = sys.argv[1]
#print(sys.argv)
# 定義x, y空列表
x = []
y = []
# 讀取檔案並把每一行寫入x,y
with open(filename, 'r') as f:
    # 分每一行讀取
    for line in f.readlines():
        #print(line.split(','))
        # 將讀取到的數據以逗號分隔，並轉化成浮點數
        xt, yt = [float(i) for i in line.split(',')]
        # 將資料放入x, y 的列表
        x.append(xt)
        y.append(yt)
# 定義訓練資料集的長度
num_training = int(0.8*len(x))
# 定義測試資料集的長度
num_test = len(x)-num_training
# 將資料分成訓練用以及測試用
x_train = np.array(x[:num_training]).reshape((num_training, 1))
y_train = np.array(y[:num_training])
x_test = np.array(x[num_training:]).reshape((num_test, 1))
y_test = np.array(y[num_training:])
# 呼叫線性回歸模型
linear_regressor = linear_model.Ridge(alpha=20)
# 輸入訓練資料集給回歸模型做訓練
linear_regressor.fit(x_train, y_train)
# 輸入測試資料集做預測
y_test_predict =  linear_regressor.predict(x_test)
# 顯示預測模型的各項指標
show_metrics(y_test, y_test_predict)
# 指定輸出模型檔案位置
output_file = "saved_model.pkl"
# 打開檔案
with open(output_file, 'wb') as f:
    # 將模型壓縮成pkl檔
    pickle.dump(linear_regressor, f)

# 產生空白畫布
plt.figure()
# 畫散布圖
plt.scatter(x_train, y_train, color='green')
plt.plot(x_test, y_test_predict, color='red')
# 設定標題
plt.title('linear_regression')
# 展示數據圖
plt.show()
    