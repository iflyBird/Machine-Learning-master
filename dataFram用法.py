#数据的可视化操作
import pandas as pd
import numpy as np
#index为设置行数,columns为设置列数

df6 = pd.DataFrame(np.arange(36).reshape(6, 6), index=list('abcdef'), columns=list('ABCDEF'))
print(df6)
print(df6.head(2))
#查看行名与列名
print(df6.index)
print(df6.columns)
#使用values可以查看DataFrame里的数据值，返回的是一个数组。
print(df6.values)
#比如说查看某一列所有的数据值。
print(df6['B'].values)
#直接创建
import pandas as pd
import numpy as np
df4 = pd.DataFrame([[1, 2, 3],
					[2, 3, 4],
                    [3, 4, 5]],
                   index=list('abc'), columns=list('ABC'))
print(df4)
# 使用字典创建
import pandas as pd
import numpy as np

dic1 = {
    'name': [
        '张三', '李四', '王二麻子', '小淘气'], 'age': [
            37, 30, 50, 16], 'gender': [
                '男', '男', '男', '女']}
df5 = pd.DataFrame(dic1)
print(df5)
#查看列的数据类型
print(df5.dtypes)
#查看DataFrame的头尾
# 使用head可以查看前几行的数据，默认的是前5行，不过也可以自己设置。
#
# 使用tail可以查看后几行的数据，默认也是5行，参数可以自己设置。
#
# 比如看前5行。
import pandas as pd
import numpy as np

df6 = pd.DataFrame(np.arange(36).reshape(6, 6), index=list('abcdef'), columns=list('ABCDEF'))
print(df6)
#比如只看前2行。
print(df6.head(2))
# 2.3 查看行名与列名
#使用shape查看行列数，参数为0表示查看行数，参数为1表示查看列数
# 使用index查看行名，columns查看列名。
print(df6.shape[0])
print(df6.shape[1])
#2.6 切片
# 使用冒号进行切片。
#切割a行到b行
print(df6['a':'b'])
#索引
# 切片表示的是行切片
# 索引表示的是列索引
print(df6.loc[:,'A':'B'])
# 3 DataFrame操作
# 3.1 转置
# 直接字母T，线性代数上线。
print(df6.T)
# 3.2 描述性统计
# 使用describe可以对数据根据列进行描述性统计。
print(df6.describe())
# 如果有的列是非数值型的，那么就不会进行统计。
#
# 如果想对行进行描述性统计，转置后再进行describe。
#
# 3.3 计算
# 使用sum默认对每列求和，sum(1)为对每行求和。
print(df6.sum(0))
print(df6.sum(1))
#数乘运算使用apply。
print(df6.apply(lambda x: x * 2))
#乘方运算跟matlab类似，直接使用两个*。
print(df6**2)
# 3.4 新增
# 扩充列可以直接像字典一样，列名对应一个list，但是注意list的长度要跟index的长度一致。
df6['G']=['999','999','999','999','999','999']
print(df6)
#还可以使用insert，使用这个方法可以指定把列插入到第几列，其他的列顺延。
df6.insert(0, 'QQ', ['999','999','999','999','999','999'])
print(df6)
#3.5 合并
# 使用join可以将两个DataFrame合并，但只根据行列名合并，并且以作用的那个DataFrame的为基准。
# 也就是以df6为基准。
df7 = pd.DataFrame(['my', 'name', 'is', 'a', 'b', 'c'], index=list('abcdef'), columns=list('m'))
#但是，join这个方法还有how这个参数可以设置，合并两个DataFrame的交集或并集。参数为’inner’表示交集，'outer’表示并集
df8 = df6.join(df7)
print(df8)
#但是，join这个方法还有how这个参数可以设置，合并两个DataFrame的交集或并集。参数为’inner’表示交集，'outer’表示并集




df10 = pd.DataFrame([1, 2, 3, 4, 5, 6],
					index=list('ABCDEF'), columns=['a'])
df11 = pd.DataFrame([10, 20, 30, 40, 50, 60],
                    index=list('ABCDEF'), columns=['b'])
df12 = pd.DataFrame([100, 200, 300, 400, 500, 600],
                    index=list('ABCDEF'), columns=['c'])
list1 = [df10.T, df11.T, df12.T]
df13 = pd.concat(list1)
print(df13)
#3.6 去重
df6.drop_duplicates(subset=None,
                   keep='first',
                   inplace=False
                   )
#参数：
#
# subset：指定是哪些列重复。
# keep：去重后留下第几行，{‘first’, ‘last’, False}, default ‘first’｝，如果是False，则去除全部重复的行。
# inplace：是否作用于原来的df。

df14 = pd.DataFrame(data=[[1, 2, 3],
                          [1, 2, 4],
                          [1, 2, 4],
                          [1, 2, 3],
                          [1, 2, 5],
                          [1, 2, 5]],
                    index=list('ABCDEF'),
                    columns=['a', 'b', 'c'])
print(df14)

df14 = pd.DataFrame(data=[[1, 2, 3],
                          [1, 2, 4],
                          [1, 2, 4],
                          [1, 2, 3],
                          [1, 2, 5],
                          [1, 2, 5]],
                    index=list('ABCDEF'),
                    columns=['a', 'b', 'c'])
print(df14)
#去除重复行,保留重复行中最后一行
df14.drop_duplicates(keep='last')
#去除’c’列中有重复的值所在的行
print(df14.drop_duplicates(subset=('c',)))
#去除’c’列中有重复的值所在的行
print(df14.drop_duplicates(subset=('c',)))