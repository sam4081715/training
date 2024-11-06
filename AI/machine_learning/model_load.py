import numpy as np
import pickle
# 指定讀取檔案位置
read_file = "saved_model.pkl"
# 開啟檔案
with open(read_file, "rb") as f:
    # 將pkl檔解壓縮成python的物件
    model_linregr = pickle.load(f)
# 產生測試資料
x_test = np.array([1,2,3,4]).reshape((-1,1))
# 使用模型做預測
y_test_pred_new = model_linregr.predict(x_test)
# 顯示預測結果
print(y_test_pred_new)