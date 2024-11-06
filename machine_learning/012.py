import numpy as np
import neurolab as nl
import pickle

# 輸入資料檔案位址
input_file = 'data_012.txt'
# 產生空列表來儲存汽車資料
X_o = []
# 打開檔案讀取資料
with open(input_file, 'r') as f:
    for line in f.readlines():
        # 每一行的最後一位是換行符號，捨去
        data = line[:-1].split(',')
        X_o.append(data)
# 轉成array
X_o = np.array(X_o)
# 將資料與標籤分開
data = X_o[:, :-1].astype(float)
labels = X_o[:,-1].astype(float).reshape(-1,1)

min_value = -6
max_value = 6

# 定義每一層激勵函數
transfun = [nl.trans.TanSig(), nl.trans.LogSig()]
# 呼叫多層感知器，第二個變數決定神經網路的結構、形狀
multilayer_net = nl.net.newff([[min_value, max_value], [min_value, max_value]], [12, 1], transf = transfun)
# 指定權重更新的演算法
multilayer_net.trainf = nl.train.train_gd
# 訓練神經網路
error = multilayer_net.train(data, labels, epochs = 5000, show=100, goal=0.01)

# 指定輸出模型檔案位置
output_file = "AI03_謝閔翔.pkl"
# 打開檔案
with open(output_file, 'wb') as f:
    # 將模型壓縮成pkl檔
    pickle.dump(multilayer_net, f)



