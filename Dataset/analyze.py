import numpy as np 
import pandas as pd 
import time

start=time.time()

df = pd.read_csv("911.csv")
g=0
for a, b in zip(df.lat,df.lng):
	g+=1
	
print(g)
print(time.time()-start)