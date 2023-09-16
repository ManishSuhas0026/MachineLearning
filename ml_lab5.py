# -*- coding: utf-8 -*-
"""ML_Lab5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M6TIdc6OUYauMVTV0pIlVDFhUBWbpP3O
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv('/content/WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df.head())
print(df.info())

df.isnull().sum()

from sklearn.preprocessing import LabelEncoder
columns_encoder =['gender','Partner','Dependents']
encoder = LabelEncoder()
df[columns_encoder] = df[columns_encoder].apply(encoder.fit_transform)
df

from sklearn.model_selection import train_test_split
features = ['gender', 'Dependents', 'tenure']
target = 'Churn'
X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()