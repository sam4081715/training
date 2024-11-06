import numpy as np
import cv2
# 設定輸入檔案位址
input_file = 'letter/letter.data'
# 設定放大倍率
scaling_factor = 25
# 設定影像開始、結尾位址
start_index = 6
end_index = -1
# 設定影像高、寬
h, w = 16, 8
# 打開檔案並讀取每一行
with open(input_file, 'r') as f:
    for line in f.readlines():
        # 讀取字符資料(標籤)並印出
        letter = line.split('\t')[1]
        print("字符為:"+letter)
        # 讀取影像資料
        data = np.array([255*float(x) for x in line.split('\t')[start_index:end_index]])
        img = np.reshape(data, (h,w))
        # 使用cv2放大影像
        img_scaled = cv2.resize(img, dsize=None, fx = scaling_factor, fy = scaling_factor)
        # 展示影像
        cv2.imshow('image', img_scaled)
        # 等待按鍵
        c = cv2.waitKey()
        # 若按鍵為esc，則跳出迴圈
        if c == 27:
            break
        