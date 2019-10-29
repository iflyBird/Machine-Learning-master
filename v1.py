
#a.csv is three rows csv
#这个代码是用来统计某一csv文件的某一列数据，对该列数据进行分类并且进行计数



import pandas as pd
import re
import csv
import sys


path='./home/bank-full.csv'#文件路径不能包含中文，否则会报错


df=pd.read_csv(path,'utf-8',engine='python')#编码格式utf-8
df.head()
print(df)


df.describe()

import numpy as np
#公共部分


#统计出行方式
address=pd.read_csv(path,usecols=[0])   #提取想要的数据列，0是列索引

address.to_csv("./home/bank-full.csv")  #文件输出

path2='./home/bank-full.csv'   #文件读取


df2=pd.read_csv(path2,'utf-8',engine='python')

df3=np.unique(address)      #调用unique函数对该列数据分组，返回每一组的组名


print(df3)

ts = pd.Series(address['age'].values, index=address['age'])   #分组后计数返回该组的组名和每一个名称的数量

ts.describe()

ts.value_counts()


wuqu=ts.value_counts()   #格式转换加文件输出，series无法直接输出为csv
wuqu1=pd.DataFrame(ts.value_counts())
wuqu1.to_csv('./home/bank-full.csv')    #输出文件是包含组名以及个数的csv文件
