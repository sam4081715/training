import numpy as np
class LR():
    def __init__(self):
        self.cof = None
        
    def fit(self, x_data, y_data):
        x_array = np.array(x_data)
        y_array = np.array(y_data)
        x_array = np.c_[np.ones(x_array.shape[0]), x_array]
        array_matrix = np.zeros((x_array.shape[1],x_array.shape[1]))
        answer_list = []
        for i in range(x_array.shape[1]):
            for j in range(x_array.shape[1]):
                array_matrix[i,j] = np.dot(x_array[:,j], x_array[:,i])
            answer_list.append(np.dot(x_array[:,i], y_array))
        matrix_M = np.matrix(array_matrix)
        matrix_B = np.matrix(answer_list).T
        matrix_A = np.linalg.inv(matrix_M)*matrix_B
        self.cof = np.array(matrix_A)
        self.cof = self.cof[:,0]
        self.cof = [round(i, 2)for i in self.cof]
        self.cof = np.array(self.cof)

    def predict(self, x_data):
        x_array = np.array(x_data)
        x_array = np.c_[np.ones(x_array.shape[0]), x_array]
        y_list = [round(np.dot(self.cof, x_array[i,:]),2) for i in range(x_array.shape[0])]
        return y_list
    
        