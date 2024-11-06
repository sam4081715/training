import numpy as np
import neurolab as nl

# 設定輸入資料位址
input_file = 'letter/letter.data'
# 設定擷取資料長度
num_points = 40
# 設定擷取字符種類
orig_labels = 'omandig'
# 設定輸出數量
num_output = len(orig_labels)
# 設定訓練資料大小
num_train = int(0.9*num_points)
# 設定測試資料大小
num_test = num_points - num_train
# 設定影像起始、結尾序號
start_index = 6
end_index = -1
# 設定空列表放資料、標籤
data = []
labels = []
# 打開檔案並檢查每一行
with open(input_file, 'r') as f:
    for line in f.readlines():
        # 將該行以tab符號分隔並轉化成list
        list_vals = line.split('\t')
        # 檢查letter是否有在orig_labels裡面，若沒有就跳過此次迴圈
        if list_vals[1] not in orig_labels:
            continue
        # 將標籤轉化為獨熱編碼
        label = np.zeros(num_output)
        label[orig_labels.index(list_vals[1])] = 1
        # 將標籤存入標籤列表
        labels.append(label)
        # 抓取影像資料
        cur_char = np.array([float(x) for x in list_vals[start_index:end_index]])
        # 將資料存入資料列表
        data.append(cur_char)
        # 如果資料長度足夠，就跳出迴圈
        if len(data) >= num_points:
            break
# 將資料、標籤轉化為陣列
data = np.array(data)
labels = np.array(labels)
# 擷取輸入特徵數量
num_dims = len(data[0])
# 呼叫類神經網路
net = nl.net.newff([[0,1] for _ in range(num_dims)], [128, 16, num_output])
# 設定權重更新方式
net.trainf = nl.train.train_gd
# 訓練模型並回傳誤差
error = net.train(data[:num_train,:], labels[:num_train,:], epochs=10000, show=100, goal=0.01)
# 測試神經網路
predicted_ouput = net.sim(data[num_train:,:])
# 將預測結果與實際結果印出
for i in range(num_test):
    print(orig_labels[np.argmax(labels[num_train+i])])
    print(orig_labels[np.argmax(predicted_ouput[i])])