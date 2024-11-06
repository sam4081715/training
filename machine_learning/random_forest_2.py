import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, validation_curve, learning_curve
import matplotlib.pyplot as plt
# 輸入資料檔案位址
input_file = 'car/car.data'
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
# 產生空列表來放編碼器
label_encoder = []
# 產生空陣列來放編碼後的資料
X_encoded = np.empty(X_o.shape)
# 根據特徵數量跑回圈
for i, item in enumerate(X_o[0]):
    # 呼叫新的編碼器，並放入列表
    label_encoder.append(preprocessing.LabelEncoder())
    # 呼叫最新的編碼器做編碼訓練
    X_encoded[:,i] = label_encoder[-1].fit_transform(X_o[:,i])
# 將資料分成輸入特徵、輸出分類
X = X_encoded[:, :-1].astype(int)
y = X_encoded[:,-1].astype(int)
# 定義分類器參數
params = {'n_estimators': 200, 'max_depth': 8, 'random_state': 7}
# 呼叫隨機森林分類器
classifier = RandomForestClassifier(**params)
# 訓練分類器
classifier.fit(X, y)
# 交叉驗證分類器準確度
accuracy = cross_val_score(classifier, X, y, scoring = 'accuracy', cv = 3)
print("準確度為:", round(100*accuracy.mean(), 2),"%")
# 手動產生測試資料
input_data = ["low","low","5more","4","med","low"]
input_data_encoded = [-1]*len(input_data)
# 跑回圈對每個特徵都做編碼
for i, item in enumerate(input_data):
    input_data_encoded[i] = int(label_encoder[i].transform([input_data[i]])[0])
    
print("輸入資料:", input_data)
# 轉成陣列以輸入分類器
input_data_encoded = np.array([input_data_encoded])
# 分類器做預測
output_class = classifier.predict(input_data_encoded)
# 將輸出結果解碼
output_class_decoded = label_encoder[-1].inverse_transform(output_class)[0]
print("判斷車子為:", output_class_decoded)
# 呼叫分類器
classifier = RandomForestClassifier(**params)
# 定義訓練數據的大小
parameter_grid = np.array([200, 500, 800, 1100])
# 呼叫學習曲線，輸入分類器、X數據, y數據,訓練資料大小
train_sizes, train_score, validation_score = learning_curve(classifier, X, y,
                                                            train_sizes = parameter_grid, cv=5)
# 展示不同訓練資料大小下的驗證分數
print("\n####學習曲線####")
print("\n訓練分數:\n", train_score)
print("\n驗證分數:\n", validation_score)
# 畫圖
plt.figure()
plt.plot(parameter_grid, 100*train_score.mean(axis=1), color = "red")
plt.plot(parameter_grid, 100*validation_score.mean(axis=1), color = "blue")
plt.title('learning curve')
plt.xlabel('train sizes')
plt.ylabel('accuracy')
plt.show()






        