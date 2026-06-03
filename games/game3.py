import pandas as pd
df = pd.DataFrame([['a','b',1,2],['c','d',34,45],['e','f',5,6],['g','h',7,8]],columns=['coli','col2','col3','col4'])
print(df)
df.index = ['r1','r2','r3','r4']
res = df.loc['r1':'r3','coli':'col4']
print(res)