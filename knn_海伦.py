import pandas as pd
#导入数据集
datetest=pd.read_table("datingTestSet.txt",header=None);
#print('{0} ,{1}'.format(datetest.iloc[:,0],datetest.iloc[:,1]),end=" ")
#print(datetest.iloc[:,0],datetest.iloc[:,1])
#print(datetest);#输出数据集
#print(datetest.head())#输出前五行的数据集
#print(datetest.shape);
#分析t数据（散点图来表示）
#%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt#绘制散点图
#把不同的标签用不同的颜色表示
Color=[]#设置标签的颜色
#datetest.shape[0]表示总共1000行
#-1表示最后一列
for i in range(datetest.shape[0]):
    m=datetest.iloc[i,-1]
    if m=="didntLike":
        Color.append('black')
    if m=="smallDoses":
        Color.append("orange")
    if m=="largeDoses":
        Color.append("red")
#设置将不同心动的人设置不同的颜色
#print(Color);#输出Color颜色
#绘制两两之间的特征值得散点图
#plt.rcParams['font.sans-serif']=['SimHei']#设置图中的字体为黑体
pl=plt.figure(figsize=(12,8));#设置画布的大小
#设置成为俩行俩列中的第一个


fig1=pl.add_subplot(221);

plt.scatter(datetest.iloc[:,1],datetest.iloc[:,2],marker='.',c=Color)
plt.xlabel("玩游戏的时间");
plt.ylabel("每周消费冰激凌的公升数");
#plt.show();
fig2=pl.add_subplot(222);
plt.scatter(datetest.iloc[:,0],datetest.iloc[:,1],marker='.',c=Color)
plt.xlabel("每年飞行里程");
plt.ylabel("玩游戏的时间")

#第三个图
fig3=pl.add_subplot(223);
plt.scatter(datetest.iloc[:,0],datetest.iloc[:,2],marker=".",c=Color);
plt.xlabel("每年飞行的时间");
plt.ylabel("每周消费冰激凌的公升数");
plt.show();
#数据归一化
#由于每年飞行常客的旅程站的比例比较大
#=(x-xmin)/(xmax-xmin)；
def minax(datetest):
    mindf=datetest.min();
    maxdf=datetest.max();
    normset=(datetest-mindf)/(maxdf-mindf)
    return normset;
dating=pd.concat([minax(datetest.iloc[:,:3]),datetest.iloc[:,3]],axis=1)
#pd.concat是合并函数，axis： 需要合并链接的轴，0是行，1是列
#print(dating.head())
#划分训练集和测试集
def randSplit(dateset,rate=0.9):
    #n表示数据集一共多少行
    #m就是训练集的个数
    #选取测试集需要随机选择
    #
    n=datetest.shape[0];
    m=int(n*0.9);
    #前m个位我们的训练集
    #m个之后是我们的测试集
    train=datetest.iloc[:m,:];
    test=datetest.iloc[m:,:];
    #index乱码,进行重置
    test.index=range(test.shape[0]);
    return train,test;
#输出训练集与测试集
# a=randSplit(datetest)
# print(a);
#定义一个分类器函数
def dateClass(train,test,k):
    n=train.shape[1]-1;#除去标签的那一列
    m=test.shape[0];
    result=[];
    for i in range(m):
        dist=list(((train.iloc[:,:n]-test.iloc[i,:n])**2).sum(1)**0.5)
        dist_l=pd.DataFrame({'dist':dist,'labels':(train.iloc[:,n])})
        dr=dist_l.sort_values(by='dist')[:k];
        re=dr.loc[:,'labels'].value_counts();
        result.append(re.index[0])
    result=pd.Series(result);
    #在最后一列添加预测集,方便判断
    test['predict']=result
    acc=(test.iloc[:,-1]==test.iloc[:,-2]).mean();
    print(f"准确率为{acc}");
    return test
#测试
train,test=randSplit(datetest)
print(train.head(5))

dateClass(train,test,5)
