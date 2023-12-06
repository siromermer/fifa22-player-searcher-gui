import pandas as pd 


data2=pd.read_csv("sources/fifa22.csv")

proplist=[]
for i in data2:
    proplist.append(i)
 