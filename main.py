"""

1: kat sayısı
2: bir kattaki daire sayısı
3: ısıtma tipi ['Doğalgaz (Kombi)', 'Yok', 'Doğalgaz (Merkezi)', 'VRV', 'Doğalgaz Sobası', 'Klima', 'Soba', 'Yerden Isıtma', 'Kalorifer']
                [0,                   1,        2,                  3,      4,                  5,     6,       7,              8]
4: m2
5: fiyat
6: şehir: ankara: 6, antalya 7,bursa 16, gaziantep 27, istanbul: 34, izmir: 35,
"""
# %%

import pandas as pd
from sklearn import linear_model

df = pd.read_csv("cleared_merged_output.csv", sep=",")


# %%
print(df.shape)

# %%
df = df.dropna()
Q1 = df['5'].quantile(0.25)
Q3 = df['5'].quantile(0.75)
IQR = Q3 - Q1
outliers = (df['5'] < Q1 - 1.5 * IQR) | (df['5'] > Q3 + 1.5 * IQR)

df_no_outliers = df[~outliers]
df = df_no_outliers

print(df.shape)





# %%
reg = linear_model.LinearRegression()
reg.fit(df[['1','2','3','4','6']], df[['5']])
# %%

new_data = pd.DataFrame({'1': [4], '2': [2], '3': [2], '4':[165],'6':[1]})

# Modelden tahmin yapma
predictions = reg.predict(new_data)

# Tahmin sonuçlarını yazdırma
print(predictions)


# %%

score = reg.score(df[['1','2','3','4','6']], df[['5']])

print("başarı oranı: ", score)


# %%



# %%

