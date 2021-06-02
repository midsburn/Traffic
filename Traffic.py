import pandas as pd
import numpy as np
import glob

all=[]
for f in glob.glob("*.xls"):
    df=pd.read_excel(f)
    all.append(pd.read_excel(f))

df=pd.concat(all,ignore_index=True)
print(df.head(10))
