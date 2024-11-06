import numpy as np

def decision(X_data, y_data):
    # 將輸入list轉成array
    X_array = np.array(X_data)
    y_array = np.array(y_data)
    # 初始化最小的MSE
    min_MSE = len(y_array)*y_array.std()**2
    # 遍歷所有的feature
    for i in range(X_array.shape[1]):
        # 將X數據做切片，切成只有一個feature的形式
        X_clip = X_array[:,i]
        # 將X切片從小到大排序，並以同樣方式排序y數據
        X_sorted = np.sort(X_clip)
        y_sorted = y_array[np.argsort(X_clip)]
        # 遍歷所有的分界點
        for j in range(len(X_sorted)-1):
            # 判斷是否小於等於分界點，將資料分成左、右兩個子集合
            y_left = np.array([y_sorted[s] for s in range(len(X_sorted)) if X_sorted[s]<=X_sorted[j]])
            y_right = np.array([y_sorted[s] for s in range(len(X_sorted)) if X_sorted[s]>X_sorted[j]])
            # 計算MSE數值
            MSE_total = len(y_left)*(y_left.std())**2+len(y_right)*(y_right.std())**2
            # 判斷MSE最小值是否有更新
            if min_MSE > MSE_total:
                min_MSE = MSE_total
                feature_index = i
                feature_value = X_sorted[j]
        return feature_index, float(feature_value)
    
x_data = [[1,2,9],[4,4,6],[3,1,2],[1,3,8]]
y_data = [1,3,4,12]
a = decision(x_data, y_data)
print(a)
#print(np.array(x_data).std())
    