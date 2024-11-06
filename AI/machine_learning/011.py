import numpy as np

class Naive_bayes():
    # 初始化
    def __init__(self):
        self.std_data = None
        self.mean_data = None
    # 將數據依照標籤分類
    def classify(self, X_data, y_data):
        # 產生空字典，準備存放分類後的資料
        self.class_data = {}
        # 產生不重複的標籤列表
        self.label_list = list(dict.fromkeys(y_data))
        # 跑不同標籤的迴圈
        for label in self.label_list:
            # 在不同標籤(鍵)底下放空列表
            self.class_data[label] = []
        # 跑迴圈遍歷所有資料
        for i, item in enumerate(y_data):
            # 將y_data裡的標籤抓出來作為字典的鍵，呼叫底下的列表append第i個X數據
            self.class_data[item].append(X_data[i])
        # 跑迴圈將每個標籤底下的列表轉換成陣列
        for label in self.label_list:
            self.class_data[label] = np.array(self.class_data[label])
    # 訓練，計算每個標籤、每個特徵的數據的平均值以及標準差
    def fit(self, X_data, y_data):
        # 將數據依照標籤分類
        self.classify(X_data, y_data)
        # 產生空字典，準備放入平均值以及標準差的數據
        self.mean_data = {}
        self.std_data = {}
        # 跑不同標籤的迴圈
        for label in self.label_list:
            # 以axis=0這個軸來計算平均值、標準差，最後得到不同特徵的平均值、標準差
            self.mean_data[label] = self.class_data[label].mean(axis=0)
            self.std_data[label] = self.class_data[label].std(axis=0)
    # 計算最終機率
    def cal_prob(self, X, std, mean):
        print("X陣列",X)
        print("標準差陣列",std)
        print("平均值陣列",mean)
        # 高斯分布(常態分布)的機率密度函數，陣列的對位運算
        prob_array = np.exp(-((X-mean)**2)/(2*std**2))/(std*np.sqrt(2*np.pi))
        print("機率陣列",prob_array)
        # 初始化最終機率
        prob_final = 1
        # 將不同特徵的機率相乘得到最終機率
        for prob in prob_array:
            prob_final = prob_final*prob
        print("最終機率",prob_final)
        # 輸出最終機率
        return prob_final
    # 做分類
    def predict(self, X_data):
        # 產生空列表放分類結果
        y_pred = []
        # 跑迴圈抓取每一筆數據
        for X in X_data:
            # 將X列表轉成陣列，以方便做機率運算
            X_array = np.array(X)
            # 初始化最大機率
            max_tmp_prob = 0
            # 跑迴圈檢查每一個標籤
            for label in self.label_list:
                # 將X陣列以及對應標籤的標準差以及平均值抓出來運算機率
                tmp_prob = self.cal_prob(X_array, self.std_data[label], self.mean_data[label])
                # 檢查是否大於當前最大機率
                if max_tmp_prob < tmp_prob:
                    # 更新當前最大機率
                    max_tmp_prob = tmp_prob
                    # 更新預測的分類
                    predict_label = label
            # 將預測分類儲存至y_pred列表
            y_pred.append(predict_label)
        return y_pred
    
X_data = [[1,1], [3,4], [3,3], [4,5],[0,0],[2,1],[6,6],[8,4]]
y_data = [1,1, 'apple', 'apple',1,1,'apple','apple']

X_test = [[6,6]]

a = Naive_bayes()
a.fit(X_data, y_data)
print(a.mean_data)
y_pred = a.predict(X_test)
print(y_pred)