class One_hot():
    def __init__(self):
        # 初始化屬性
        self.label_list = None
        self.label_number = None
        self.encode_list = None
        self.decode_list = None
    # 編碼
    def encode(self, label_data):
        # 將標籤資料的重複項去除
        self.label_list = list(dict.fromkeys(label_data))
        # 計算標籤數目
        self.label_number = len(self.label_list)
        # 初始化編碼列表
        self.encode_list = []
        # 跑迴圈將標籤一個一個的轉化成編碼
        for label in label_data:
            # 初始化編碼
            encode = [0 for i in range(self.label_number)]
            # 跑迴圈，確認標籤屬於第幾個
            for j in range(self.label_number):
                if label == self.label_list[j]:
                    encode[j] = 1
            # 將編碼加入編碼列表
            self.encode_list.append(encode)
        return self.encode_list
    # 解碼
    def decode(self, encode_data):
        # 初始化解碼列表
        self.decode_list = []
        # 跑迴圈一個一個的將編碼解碼
        for encode in encode_data:
            # 確認編碼的第幾項為1，轉化成對應標籤
            decode = [self.label_list[i] for i in range(len(encode)) if encode[i] == 1]
            # 將標籤放入解碼的列表
            self.decode_list.append(decode[0])
        return self.decode_list
    
# label_data = ['Setosa', 'Virginica', 'Setosa', 'Versicolour', 'Virginica']
# a = One_hot()
# b = a.encode(label_data)
# c = a.decode(b)
# print(c)