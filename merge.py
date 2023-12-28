import pandas as pd
import os

path = "F:\\ChromeDownload\\sahibinden\\antalya"
files = os.listdir(path)
files_csv = [f for f in files if f[:2] == 'U1']

df_list = []
for i in files_csv:
    data = pd.read_csv(os.path.join(path, i), encoding="utf-8")
    df_list.append(data)

df = pd.concat(df_list)

output = f"{path}\\output.csv"
df.to_csv(output,index=False, encoding="utf-8")
