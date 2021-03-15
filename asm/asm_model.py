# import library 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle 
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import log_loss
from sklearn.calibration import CalibratedClassifierCV


# load asm features 
df_asm = pd.read_csv('C:\\Users\\Vipul Singh\\Desktop\\train (1)\\ASM.csv')


Y = df_asm['Class']
X = df_asm.drop(['ID', 'Class'], axis = 1)

# Split the data into train and validation set
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