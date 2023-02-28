import pandas as pd
import numpy as np

df=pd.read_csv("scraped.csv")
#print(df["dwarf name"])

df=df[df["radius"].notna()]
df=df[df["mass"].notna()]

df["mass"]=np.array(df["mass"], float)

df["radius"]=[element* 0.102763 for element in df["radius"]]
df["mass"]=[element* 0.000954588 for element in df["mass"]]
df.to_csv("scraped-final.csv")