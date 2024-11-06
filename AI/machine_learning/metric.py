import sklearn.metrics as sm

def show_metrics(y, y_pred):
    print("平均絕對值誤差(Mean absolute error):", round(sm.mean_absolute_error(y, y_pred), 2))
    print("平均平方誤差(Mean squared error):", round(sm.mean_squared_error(y, y_pred), 2))
    print("中值絕對離差(Median absolute error):", round(sm.median_absolute_error(y, y_pred), 2))
    print("解釋方差分(Explained variance score):", round(sm.explained_variance_score(y, y_pred), 2))
    print("決定係數(R2 score):", round(sm.r2_score(y, y_pred), 2))

    