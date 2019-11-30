import pandas as pd 

otu = pd.read_excel(r'/Users/xuyuanwu/Desktop/Python/test/test.xlsx')

for index,row in otu.iterrows():
    print(index)
    print(row)