from zipfile import ZipFile
import pandas as pd

zip_file = "CMAPSSData.zip"

with ZipFile(zip_file, "r") as z:
    z.extractall("CMAPSSData")

cols = (
    ["unit_number", "time_cycles"] +
    [f"op_setting_{i}" for i in range(1,4)] +
    [f"sensor_{i}" for i in range(1,22)]
)

f1 = pd.read_csv("CMAPSSData/train_FD001.txt", sep=r"\s+", header=None)
f2 = pd.read_csv("CMAPSSData/train_FD002.txt", sep=r"\s+", header=None)
f3 = pd.read_csv("CMAPSSData/train_FD003.txt", sep=r"\s+", header=None)
f4 = pd.read_csv("CMAPSSData/train_FD004.txt", sep=r"\s+", header=None)

f1 = f1.dropna(axis=1)
f2 = f2.dropna(axis=1)
f3 = f3.dropna(axis=1)
f4 = f4.dropna(axis=1)

f1.columns = cols
f2.columns = cols
f3.columns = cols
f4.columns = cols

f1["dataset"] = "FD001"
f2["dataset"] = "FD002"
f3["dataset"] = "FD003"
f4["dataset"] = "FD004"

data = pd.concat([f1, f2, f3, f4], ignore_index=True)

data["engine_id"] = data["dataset"] + "_" + data["unit_number"].astype(str)

data.to_csv("NASA_CMAPSS_Train_All.csv", index=False)

print(data.shape)

print(data.head())