
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd


df = pd.read_csv('/Users/kyrie/Documents/悉尼及准备/学校资料/data1002/SDG_goal3_clean.csv')
target_col = 'Maternal mortality ratio'
feature_cols = [
    'Proportion of births attended by skilled health personnel (%)',
    'Health worker density, by type of occupation (per 10,000 population)::PHARMACIST'
]

df = df.dropna(subset=[target_col] + feature_cols)


df['target_class'] = pd.qcut(df[target_col], q=3, labels=[1, 2, 3])

X = df[feature_cols]
y = df['target_class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

nb = GaussianNB()

nb.fit(X_train, y_train)


y_pred = nb.predict(X_test)


print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
