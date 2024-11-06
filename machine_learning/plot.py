import numpy as np
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

# 畫混淆矩陣
def plot_confusion_matrix(confusion_mat):
    # 將混淆矩陣作為影像畫出
    plt.imshow(confusion_mat, interpolation='nearest', cmap='binary')
    # 設定標題
    plt.title("confusion matrix")
    # 設定色階條
    plt.colorbar()
    # 設定刻度
    tick_number = confusion_mat.shape[0]
    tick_marks = np.arange(tick_number)
    plt.xticks(tick_marks, tick_marks)
    plt.yticks(tick_marks, tick_marks)
    # 設定x軸、y軸標題
    plt.xlabel("True label")
    plt.ylabel("Predicted label")
    plt.show()
    
    
    