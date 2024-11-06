import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn import datasets
from sklearn.utils import shuffle
from metric import show_metrics

# 抓取加州的房價資料
housing_data = datasets.fetch_california_housing()
# 打亂資料順序
X, y = shuffle(housing_data.data, housing_data.target, random_state = 7)
# 設定訓練資料佔80%
num_training = int(0.8*len(X))
# 分成訓練用、測試用的資料集
X_train, y_train = X[:num_training], y[:num_training]
X_test, y_test = X[num_training:], y[num_training:]
# 呼叫決策樹回歸器，設定最大深度為4
dt_regressor = DecisionTreeRegressor(max_depth=4)
# 將訓練用資料丟入回歸器做擬和
dt_regressor.fit(X_train, y_train)
# 用訓練好的回歸模型做預測
y_pred_dt = dt_regressor.predict(X_test)
# 展示回歸模型指標
show_metrics(y_test, y_pred_dt)
# 計算相對特徵重要性，表示為百分比
feature_importances = 100.0 * dt_regressor.feature_importances_ / max(dt_regressor.feature_importances_)
# 根據特徵重要性從大到小排序特徵名稱
index_sorted = np.flipud(np.argsort(feature_importances))
feature_names = [housing_data.feature_names[index_sorted[i]] for i in range(len(index_sorted))]
# 產生畫長條圖使用的x座標
pos = np.arange(index_sorted.shape[0])+0.5
# 畫圖
plt.figure()
plt.bar(pos, feature_importances[index_sorted], align='center')
# 將x座標換成特徵名稱
plt.xticks(pos, feature_names)
plt.ylabel('relative importance')
plt.title('DT-regressor')
plt.show()
# 畫圖，figsize會決定畫圖的大小與解析度
plt.figure(figsize=(15,5))
# 呼叫plot_tree來繪製樹狀圖
plot_tree(dt_regressor, filled = True, feature_names=housing_data.feature_names)
plt.show()
