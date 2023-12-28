import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=70)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


knn_reg = KNeighborsRegressor(n_neighbors=4)  
knn_reg.fit(X_train_scaled, y_train)

y_pred = knn_reg.predict(X_test_scaled)

r2 = r2_score(y_test, y_pred)
print("başarı oranı:  ", r2)
mse = mean_squared_error(y_test, y_pred)
print("Ortalama Kare Hata (MSE):", mse)

new_data = pd.DataFrame({'1': [4], '2': [2], '3': [2], '4': [165], '6': [34]})
new_data_scaled = scaler.transform(new_data)
predictions = knn_reg.predict(new_data_scaled)
print("Tahmin:", predictions)
