import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


df = pd.read_csv("cleared_merged_output.csv", sep=",")

df = df.dropna()

Q1 = df['5'].quantile(0.25)
Q3 = df['5'].quantile(0.75)
IQR = Q3 - Q1
outliers = (df['5'] < Q1 - 1.5 * IQR) | (df['5'] > Q3 + 1.5 * IQR)
df_no_outliers = df[~outliers]
df = df_no_outliers

X = df[['1', '2', '3', '4', '6']]
y = df['5']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

degree = 3 
poly = PolynomialFeatures(degree)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)

y_pred = poly_reg.predict(X_test_poly)

r2 = r2_score(y_test, y_pred)
print("R^2 Skoru:", r2)

new_data = pd.DataFrame({'1': [4], '2': [2], '3': [2], '4': [165], '6': [1]})
new_data_poly = poly.transform(new_data)
predictions = poly_reg.predict(new_data_poly)
print("Tahmin:", predictions)
