import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import pickle


df=pd.read_csv('diabetes.csv')
df.head()
df.info()
df.describe()
sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')
sns.countplot(x='Outcome',data=df)
sns.distplot(df['Age'].dropna(),kde=True)
df.corr()
sns.heatmap(df.corr())
sns.pairplot(df)
plt.subplots(figsize=(20,15))
sns.boxplot(x='Age', y='BMI', data=df)
x = df.drop('Outcome',axis=1)
y = df['Outcome']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=101)
logmodel = LogisticRegression()
logmodel.fit(x_train,y_train)
predictions = logmodel.predict(x_test)
# print(classification_report(y_test,predictions))
confusion_matrix(y_test,predictions)

# pickle.dump(logmodel,open('model.pkl','wb'))
# print(logmodel.predict([[5,130,78,30,26,30.2,0.988,29]]))