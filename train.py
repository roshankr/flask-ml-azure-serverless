from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

data = load_boston()

print(np.shape(data.data))

from sklearn.model_selection import train_test_split

data_df = pd.DataFrame(data.data,columns=data.feature_names)

cols = ['CHAS','RM','TAX','PTRATIO','B','LSTAT']

data_df = data_df[cols]

scaler = StandardScaler().fit_transform(data_df)

X_train, X_test, y_train, y_test = train_test_split(scaler, data.target)

from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train, y_train)

filename = 'finalized_model.sav'
pickle.dump(clf, open(filename, 'wb'))

file_name = "/Users/roramach/Python/Test/flask-ml-azure-serverless/finalized_model.sav"
with open(file_name, 'rb') as pickle_file:
    model = pickle.load(pickle_file)

infernce = np.array([[0,1600.575,2960.0,155.3,3956.9,4.98]])
scaler = StandardScaler().fit(infernce)
scaled_adhoc_predict = scaler.transform(infernce)
print(model.predict(scaled_adhoc_predict))