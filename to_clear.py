"""
1: isim
2: kat sayısı
3: bir kattaki daire sayısı
4: ısıtma tipi ['Doğalgaz (Kombi)', 'Yok', 'Doğalgaz (Merkezi)', 'VRV', 'Doğalgaz Sobası', 'Klima', 'Soba', 'Yerden Isıtma', 'Kalorifer']
                [0,                   1,        2,                  3,      4,                  5,     6,       7,              8]
5: m2
6: fiyat
"""
import pandas as pd

csv_path = "F:\ChromeDownload\sahibinden\\muğla\output.csv"

df = pd.read_csv(csv_path, sep=',')
df = df.drop(df.columns[6], axis=1)
df = df.drop(df.columns[0], axis=1)
dff = df.copy()

dff = dff.dropna()
satir_sayisi = dff.shape[0]

dff['2'] = dff['2'].str.extract('(\d+)').astype('Int32') # kat sayısı sütunu rakamları koruyarak fazlalıkları attım ve int değerine çevirdim
dff['3'] = pd.to_numeric(dff['3'], errors='coerce').dropna().astype('Int32') # bir kattaki daire sayısı sütununu int değerine çevir

# ısıtma tipi sütununu int değere çevrildi
deneme = []

for i in range(satir_sayisi):
    if dff['4'].iloc[i] not in deneme:
        deneme.append(dff['4'].iloc[i])

for i in range(len(deneme)):
    dff.loc[dff['4'] == deneme[i], '4'] = i


dff['5'] = dff['5'].astype(int) 

dff['6'] = dff['6'].apply(lambda x: int(''.join(filter(str.isdigit, str(x)))) if pd.notna(x) and x != '' else x)
dff['7'] = 48

print(dff.head(15))
print(deneme)

output = "F:/ChromeDownload/sahibinden/muğla/cleared_output.csv"
dff.to_csv(output, index=False, encoding="utf-8")



