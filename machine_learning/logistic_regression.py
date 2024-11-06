import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# 寫畫圖的函數
def plot_classifier(classifier, X, y):
    # 設定網格的最大最小值
    x_min, x_max = min(X[:,0])-1.0, max(X[:,0])+1.0
    y_min, y_max = min(X[:,1])-1.0, max(X[:,1])+1.0
    # 網格的解析度
    step_size = 0.1
    # 產生x,y值的網格
    x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))
    # 呼叫分類器做分類，透過np.c_以及ravel()來將資料整理成可以輸入分類器的形狀
    meshoutput = classifier.predict(np.c_[x_values.ravel(), y_values.ravel()])
    # 將預測結果轉成網格形狀
    meshoutput = meshoutput.reshape(x_values.shape)
    # 畫圖
    plt.figure()
    # 將網格著色(預測值)
    plt.pcolormesh(x_values, y_values, meshoutput, cmap = plt.cm.gray)
    # 畫散布圖(實際值)
    plt.scatter(X[:,0], X[:,1], c=y, s=80, edgecolors='black', linewidth=1, cmap=plt.cm.Paired)
    # 指定畫圖的上下限以及x,y的刻度
    plt.xlim(x_values.min(), x_values.max())
    plt.ylim(y_values.min(), y_values.max())
    plt.xticks((np.arange(int(x_min), int(x_max), 2.0)))
    plt.yticks((np.arange(int(y_min), int(y_max), 2.0)))
    # 展示畫好的圖
    plt.show()
    
if __name__ == '__main__':
    # 產生數據
    X = np.array([[3,5], [1,7], [11,2], [-4,6], [-11,3], [-1,2], [4,-5], [2,-10], [6, -7]])
    # 安排分類
    y = np.array([0,0,0, 1,1,1, 2,2,2])
    # 呼叫邏輯斯回歸分類器
    classifier = linear_model.LogisticRegression(solver='liblinear', C=100)
    # 將數據輸入做訓練
    classifier.fit(X, y)
    # 畫圖
    plot_classifier(classifier, X, y)
