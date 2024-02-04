import numpy as np
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM
from sklearn.metrics import (make_scorer, accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix)

df=pd.read_csv('C://Users//91987//Downloads//logging file.csv')

print(df)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder ()
df['type'] = le.fit_transform(df['type'])

X=df.drop(['isFraud','nameOrig', 'nameDest'], axis=1)
y = df["isFraud"]


X1_train, X1_test, y1_train, y1_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

#ONECLASS SVM
from sklearn.svm import OneClassSVM

# Create and fit the One-Class SVM model
model2 = OneClassSVM(nu=0.05)
model2.fit(X1_train)

# Predict outliers
y2_pred = model2.predict(X1_test)

# Convert predictions to binary labels
y2_pred = pd.Series(y2_pred).apply(lambda x: 1 if x == -1 else 0)



# Evaluate the model
print("Accuracy Score:", accuracy_score(y1_test, y2_pred))
print("\nClassification Report:\n", classification_report(y1_test, y2_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y1_test, y2_pred))
import pickle

pickle.dump(model2 , open("final_model.pkl" , "wb"))