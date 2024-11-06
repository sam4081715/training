import numpy as np
import matplotlib.pyplot as plt

# 產生資料
X = np.array([[1,2],[4,3],[6,5],[7,8]])
y = [0,1,1,0]
# 依據標籤分成類別0與類別1
class_0 = np.array([X[i] for i in range(len(X)) if y[i] == 0])
class_1 = np.array([X[i] for i in range(len(X)) if y[i] == 1])
# 畫圖
plt.figure()
# 將x,y比例設為一樣
plt.axis('equal')
# 將兩個類別以不同標記畫成散布圖。
plt.scatter(class_0[:,0], class_0[:,1], color = 'black', marker='s')
plt.scatter(class_1[:,0], class_1[:,1], color = 'black', marker='x')
# 畫分隔線
line_x = range(10)
line_y = line_x
plt.plot(line_x, line_y, color='red', linewidth = 3)
# 展示結果
plt.show()