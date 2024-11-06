from plot import plot_classifier, plot_confusion_matrix
from sklearn import datasets, model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

# 讀取鳶尾花資料集
data = datasets.load_iris()
# 將資料分成測試資料、訓練資料
X_train, X_test, y_train, y_test = model_selection.train_test_split(data.data[:,2:4],
                                    data.target, test_size = 0.25, random_state = 1)
# 呼叫單純貝式分類器，假設機率符合常態分布
classifier_gaussiannb = GaussianNB()
# 輸入訓練資料來訓練分類器
classifier_gaussiannb.fit(X_train, y_train)
# 輸入測試資料做預測
y_pred = classifier_gaussiannb.predict(X_test)
# 將測試資料與預測資料輸入，計算混淆矩陣
confusion_mat = confusion_matrix(y_test, y_pred)
# 將混淆矩陣畫成圖
plot_confusion_matrix(confusion_mat)

# 將分類結果畫成著色網格以及散布圖
plot_classifier(classifier_gaussiannb, data.data[:,2:4], data.target)

# 以交叉驗證的方式，計算準確度、精度、召回率
accuracy = model_selection.cross_val_score(classifier_gaussiannb, data.data[:,2:4], data.target,
                                           scoring='accuracy', cv = 5)
precision = model_selection.cross_val_score(classifier_gaussiannb, data.data[:,2:4], data.target,
                                           scoring='precision_weighted', cv = 5)
recall = model_selection.cross_val_score(classifier_gaussiannb, data.data[:,2:4], data.target,
                                           scoring='recall_weighted', cv = 5)
# 顯示準確度、精度、召回率
print("準確度為:", round(100*accuracy.mean(), 2), "%")
print("精度為:", round(100*precision.mean(), 2), "%")
print("召回率為:", round(100*recall.mean(), 2), "%")
