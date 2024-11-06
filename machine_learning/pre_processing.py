from sklearn import preprocessing
import numpy as np

data = np.array([[1,2,3,4],[2,3,2,1],[3,8,9,10]])
b = data.mean(axis=0)
a = data.std(axis=0)
c = (data - b)/a
#print(c)
data_standardized = preprocessing.scale(data, axis=0)
print("標準化數據:\n", data_standardized)
print("平均值:\n", data_standardized.mean(axis=0))
print("標準差:\n", data_standardized.std(axis=0))

data_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled = data_scaler.fit_transform(data)
print("數據縮放\n", data_scaled)

data_normalized = preprocessing.normalize(data, norm='l1', axis = 0)
print("歸一化數據\n", data_normalized)

data_binarized = preprocessing.Binarizer(threshold=4).transform(data)
print("二元化數據\n", data_binarized)

input_classes = ['apple', 'banana', 'grape', 'orange', 'apple']
label_encoder = preprocessing.LabelEncoder()
label_encoder.fit(input_classes)
print("標籤分類:\n", label_encoder.classes_)
labels = ['grape', 'apple']
#encoded_labels = label_encoder.transform(labels)
encoded_labels = [1,2,1,2]
print("標籤編碼:\n", encoded_labels)
decoded_labels = label_encoder.inverse_transform(encoded_labels)
print("標籤解碼:\n", decoded_labels)