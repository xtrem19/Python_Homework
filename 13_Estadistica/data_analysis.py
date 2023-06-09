# -*- coding: utf-8 -*-
"""Metabolite_2023_RFE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MQAXgCUAGC5tLA5KsvXgOefGIPkYB3zB
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from collections import Counter
import matplotlib.pyplot as plt
from imblearn.over_sampling import ADASYN
from sklearn import preprocessing

datos = pd.read_csv('BD_Metabolomica_PAPER_2023_SinComorbilidades.csv')
print(datos.shape)
print(pd.value_counts(datos['CLASS'], sort=True))

datos

y=datos['CLASS']
x=datos.drop('CLASS', axis=1)
X_train, X_test, y_train, y_test = train_test_split(x,y, train_size=0.7)

print('Number of train data:', len(X_train))
print('Number of test data:', len(y_train))
X_train
scaler = preprocessing.StandardScaler().fit(X_train)

data_train = pd.concat([X_train, y_train], axis=1)

ETIQUETAS = ['With diabetes', 'Without diabetes']
count_clases = pd.value_counts(data_train['CLASS'], sort=True)
count_clases.plot(kind='bar', rot=0)
plt.bar(ETIQUETAS, count_clases, color=['blue','red'])
plt.xticks(range(2), ETIQUETAS )
plt.title("Frecuency of Observations")
plt.xlabel("Class")
plt.ylabel("Number of Observations")
plt.show()

y_train = data_train['CLASS']
x_train = data_train.drop('CLASS', axis=1)

sampling = ADASYN()
x_train,y_train = sampling.fit_resample(x_train,y_train)

count_clasesR = pd.value_counts(y_train, sort=True)
count_clasesR.plot(kind='bar', rot=0)
plt.bar(ETIQUETAS, count_clasesR, color=['blue','red'])
plt.xticks(range(2), ETIQUETAS)
plt.title("Number of observations using SMOTE")
plt.xlabel("Class")
plt.ylabel("Number of observations")
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(x, y, train_size=0.7)
len(Y_train)
Y_test2 = Y_test
print(Y_test2)

from sklearn.feature_selection import RFE
from sklearn.svm import SVR
from sklearn.neighbors import NearestCentroid
from sklearn.tree import DecisionTreeClassifier

#Se cargan los datos
df = datos

#X son solo los datos
X = df.drop(['CLASS'], axis=1)

y = df['CLASS'].astype(float)

#Se selecciona el arbol de decision como clasificador (pueden seleccionarle varios)
estimator = DecisionTreeClassifier()#
#estimator = SVR(kernel="linear", C=1)

#En el RFE se pueden seleccionar el nùmero max de featyres
selector = RFE(estimator, n_features_to_select=5, step=1)

#Se genera el modelo
selector = selector.fit(X, y)

df = list(df)
# summarize all features

for i in range(X.shape[1]):
  if selector.support_[i] and df[i]!='CLASS':
	  print('Column: %s ' % (df[i])), df.append(df[i])

#Regresión Logistica

datos.head()

#split dataset in features and target variable
feature_cols = df
X = datos[feature_cols] # Features
y = datos.CLASS # Target variable

# split X and y into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=16)

# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression(solver='lbfgs', random_state=16)
logreg.max_iter = 2500
# fit the model with data
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

# import the metrics class
from sklearn import metrics

cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix

# import required modules
import seaborn as sns

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap

sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

from sklearn.metrics import classification_report
target_names = ['without diabetes', 'with diabetes']
print(classification_report(y_test, y_pred, target_names=target_names))

y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()

#Máquinas de soporte Vectorial
#Import svm model
from sklearn import svm

#Create a svm Classifier
msv = svm.SVC(kernel='linear') # Linear Kernel
msv = svm.SVC(probability=True)

#Train the model using the training sets
msv.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = msv.predict(X_test)

# import required modules
import seaborn as sns

class_names=[0,1] # name  of classes
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
# create heatmap

sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')

from sklearn.metrics import classification_report
target_names = ['without diabetes', 'with diabetes']
print(classification_report(y_test, y_pred, target_names=target_names))

y_pred_proba = msv.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()