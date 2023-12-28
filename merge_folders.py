import pandas as pd
import os

path1 = "F:\\ChromeDownload\\sahibinden\\istanbul\\cleared_output.csv"
path2 = "F:\\ChromeDownload\\sahibinden\\izmir\\cleared_output.csv"
path3 = "F:\\ChromeDownload\\sahibinden\\ankara\\cleared_output.csv"
path4 = "F:\\ChromeDownload\\sahibinden\\antalya\\cleared_output.csv"
path5 = "F:\\ChromeDownload\\sahibinden\\bursa\\cleared_output.csv"
path6 = "F:\\ChromeDownload\\sahibinden\\gaziantep\\cleared_output.csv"


data1 = pd.read_csv(path1, sep=",")
data2 = pd.read_csv(path2, sep=",")
data3 = pd.read_csv(path3, sep=",")
data4 = pd.read_csv(path4, sep=",")
data5 = pd.read_csv(path5, sep=",")
data6 = pd.read_csv(path6, sep=",")

df_list = [data1, data2, data3, data4, data5, data6]

df = pd.concat(df_list)

output = "F:\\ChromeDownload\\sahibinden\\cleared_merged_output.csv"
df.to_csv(output,index=False, encoding="utf-8")
