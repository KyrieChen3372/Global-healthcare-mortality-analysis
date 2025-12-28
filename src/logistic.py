from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/kyrie/Documents/悉尼及准备/学校资料/data1002/SDG_goal3_clean.csv')

target_col = 'Maternal mortality ratio'
predictor_col = 'Health worker density, by type of occupation (per 10,000 population)::PHARMACIST'
median_value = df[target_col].median()
df['target_binary'] = np.where(df[target_col] > median_value, 1, 0)

df_clean = df.dropna(subset=[predictor_col, 'target_binary'])

X = df_clean[[predictor_col]]
y = df_clean['target_binary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
report = classification_report(y_test, y_pred)
print(report)


