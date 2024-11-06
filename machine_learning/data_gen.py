import random
# 產生x的數據列表
x_list = [i*0.01 for i in range(1000)]
# 隨機排序x的數據列表
random.shuffle(x_list)
# 產生y=2x+(-1~1)的數據列表
y_list = [x_list[i]**2-2*x_list[i] + 1 + random.uniform(-5, 5) for i in range(1000)]
# 指定輸出的檔案路徑
path = 'data_square.txt'
# 以寫入模式打開檔案
f = open(path, 'w')
# 跑回圈將x, y的數據分每一行寫入
for i in range(1000):
    print(x_list[i],",",y_list[i], file = f)
# 關閉檔案
f.close()



