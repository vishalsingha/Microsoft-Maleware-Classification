import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.calibration import calibration_curve
import xgboost as xgb
from sklearn.metrics import log_loss
from sklearn.calibration import CalibratedClassifierCV
from sklearn.model_selection import cross_val_score
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
from catboost import CatBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

df_bytes = pd.read_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\Bytes.csv')


Y = df_bytes['Class']
X = df_bytes.drop(['ID', 'Class'], axis = 1)

# Split the data
x_train, x_val, y_train, y_val = train_test_split(X, Y, test_size = 0.3)


# xgboost model
clf = xgb.XGBClassifier(booster = 'gbtree',
 learning_rate = 0.19970785149378292,
 n_estimators = 180,
 max_depth = 4,
 gamma = 0.025767153406383494)
clf.fit(x_train, y_train)

# calliberartion model
sig_clf = CalibratedClassifierCV(clf, method="sigmoid", )
sig_clf.fit(x_train, y_train)

# find log loss error
loss = log_loss(y_val, clf.predict_proba(x_val) )

loss_c = log_loss(y_val, sig_clf.predict_proba(x_val) )

print('Train error for xgboost is ', log_loss(y_train, clf.predict_proba(x_train)))
print('Cross Validation error for xgboost is ',loss)

print('Train error for xgboost with calliberation is ', log_loss(y_train, sig_clf.predict_proba(x_train)))
print('Cross Validation error for xgboost with calliberation is ',loss_c)

import pickle
pickle.dump(clf, open('bytes_xgboost.pkl', 'wb')) 

from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

y_pred = clf.predict(x_val)
c = confusion_matrix(y_pred, y_val)

plt.figure(figsize = (40, 40), )
plot_confusion_matrix(clf, x_val, y_val, )
plt.show()