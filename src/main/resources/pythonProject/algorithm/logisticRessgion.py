import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os
# 读取数据
path = 'data' + os.sep + 'LogiReg_data.txt'
pdData = pd.read_csv(path , header=None , names=['Exam 1' , 'Exam 2' , 'Admitted'])
pdData.head()

# %%

pdData.shape

# %%
# s
positive = pdData[pdData['Admitted'] == 1]  # returns the subset of rows such Admitted = 1, i.e. the set of *positive* examples
negative = pdData[pdData['Admitted'] == 0]  # returns the subset of rows such Admitted = 0, i.e. the set of *negative* examples

fig , ax = plt.subplots(figsize=(10 , 5))
# c
ax.scatter(positive['Exam 1'] , positive['Exam 2'] , s=30 , color='b' , marker='o' , label='Admitted')
ax.scatter(negative['Exam 1'] , negative['Exam 2'] , s=30 , c='r' , marker='x' , label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')

# %% md

## The logistic regression

# %% md

目标：建立分类器（求解出三个参数 $\theta_0         \theta_1         \theta_2 $）


设定阈值，根据阈值判断录取结果

### 要完成的模块
-  `sigmoid`: 映射到概率的函数

-  `model`: 返回预测结果值

-  `cost`: 根据参数计算损失

-  `gradient`: 计算每个参数的梯度方向

-  `descent`: 进行参数更新

-  `accuracy`: 计算精度

# %% md

###  `sigmoid` 函数

$$
g(z) = \frac
{1}
{1 + e ^ {-z}}
$$

# %%

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# %%

nums = np.arange(-10 , 10 , step=1)  # creates a vector containing 20 equally spaced values from -10 to 10
fig , ax = plt.subplots(figsize=(12 , 4))
ax.plot(nums , sigmoid(nums) , 'r')

# %% md

### Sigmoid
* $g:\mathbb
{R} \to[0 , 1]$
* $g(0) = 0.5$
* $g(- \infty)=0$
* $g(+ \infty)=1$

# %%

def model(X , theta):
    return sigmoid(np.dot(X , theta.T))

# %% md

$$
\begin
{array}
{ccc}
\begin
{pmatrix}\theta_
{0} & \theta_
{1} & \theta_
{2}\end
{pmatrix} & \times & \begin
{pmatrix}
1\ \
    x_
{1}\ \
    x_
{2}
\end
{pmatrix}\end
{array} =\theta_
{0} +\theta_
{1}
x_
{1} +\theta_
{2}
x_
{2}
$$

# %%


pdData.insert(0 , 'Ones' ,
              1)  # in a try / except structure so as not to return an error if the block si executed several times

# set X (training data) and y (target variable)
orig_data = pdData.as_matrix()  # convert the Pandas representation of the data to an array useful for further computations
cols = orig_data.shape[1]
X = orig_data[: , 0:cols - 1]
y = orig_data[: , cols - 1:cols]

# convert to numpy arrays and initalize the parameter array theta
# X = np.matrix(X.values)
# y = np.matrix(data.iloc[:,3:4].values) #np.array(y.values)
theta = np.zeros([1 , 3])

# %%

X[:5]

# %%

y[:5]

# %%

theta

# %%

X.shape , y.shape , theta.shape

# %% md

### 损失函数
将对数似然函数去负号

$$
D(h_\theta(x) , y) = -y\log(h_\theta(x)) - (1 - y)\log(1 - h_\theta(x))
$$
求平均损失
$$
J(\theta)=\frac
{1}
{n}\sum_
{i = 1} ^ {n}
D(h_\theta(x_i) , y_i)
$$

# %%

def cost(X , y , theta):
    left = np.multiply(-y , np.log(model(X , theta)))
    right = np.multiply(1 - y , np.log(1 - model(X , theta)))
    return np.sum(left - right) / (len(X))


# %%

cost(X , y , theta)

# %% md

### 计算梯度


$$
\frac
{\partial
J}{\partial \theta_j}=-\frac
{1}
{m}\sum_
{i = 1} ^ n(y_i - h_\theta(x_i))x_
{ij}
$$

# %%

def gradient(X , y , theta):
    grad = np.zeros(theta.shape)
    error = (model(X , theta) - y).ravel()
    for j in range(len(theta.ravel())):  # for each parmeter
        term = np.multiply(error , X[: , j])
        grad[0 , j] = np.sum(term) / len(X)

    return grad


# %% md

### Gradient descent

# %% md

比较3中不同梯度下降方法

# %%

STOP_ITER = 0
STOP_COST = 1
STOP_GRAD = 2


def stopCriterion(type , value , threshold):
    # 设定三种不同的停止策略
    if type == STOP_ITER:
        return value > threshold
    elif type == STOP_COST:
        return abs(value[-1] - value[-2]) < threshold
    elif type == STOP_GRAD:
        return np.linalg.norm(value) < threshold


# %%

import numpy.random


# 洗牌
def shuffleData(data):
    np.random.shuffle(data)
    cols = data.shape[1]
    X = data[: , 0:cols - 1]
    y = data[: , cols - 1:]
    return X , y


# %%

import time


def descent(data , theta , batchSize , stopType , thresh , alpha):
    # 梯度下降求解

    init_time = time.time()
    i = 0  # 迭代次数
    k = 0  # batch
    X , y = shuffleData(data)
    grad = np.zeros(theta.shape)  # 计算的梯度
    costs = [cost(X , y , theta)]  # 损失值

    while True:
        grad = gradient(X[k:k + batchSize] , y[k:k + batchSize] , theta)
        k += batchSize  # 取batch数量个数据
        if k >= n:
            k = 0
            X , y = shuffleData(data)  # 重新洗牌
        theta = theta - alpha * grad  # 参数更新
        costs.append(cost(X , y , theta))  # 计算新的损失
        i += 1

        if stopType == STOP_ITER:
            value = i
        elif stopType == STOP_COST:
            value = costs
        elif stopType == STOP_GRAD:
            value = grad
        if stopCriterion(stopType , value , thresh): break

    return theta , i - 1 , costs , grad , time.time() - init_time


# %%

def runExpe(data , theta , batchSize , stopType , thresh , alpha):
    # import pdb; pdb.set_trace();
    theta , iter , costs , grad , dur = descent(data , theta , batchSize , stopType , thresh , alpha)
    name = "Original" if (data[: , 1] > 2).sum() > 1 else "Scaled"
    name += " data - learning rate: {} - ".format(alpha)
    if batchSize == n:
        strDescType = "Gradient"
    elif batchSize == 1:
        strDescType = "Stochastic"
    else:
        strDescType = "Mini-batch ({})".format(batchSize)
    name += strDescType + " descent - Stop: "
    if stopType == STOP_ITER:
        strStop = "{} iterations".format(thresh)
    elif stopType == STOP_COST:
        strStop = "costs change < {}".format(thresh)
    else:
        strStop = "gradient norm < {}".format(thresh)
    name += strStop
    print("***{}\nTheta: {} - Iter: {} - Last cost: {:03.2f} - Duration: {:03.2f}s".format(
        name , theta , iter , costs[-1] , dur))
    fig , ax = plt.subplots(figsize=(12 , 4))
    ax.plot(np.arange(len(costs)) , costs , 'r')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cost')
    ax.set_title(name.upper() + ' - Error vs. Iteration')
    return theta


# %% md

### 不同的停止策略

# %% md

#### 设定迭代次数

# %%

# 选择的梯度下降方法是基于所有样本的
n = 100
runExpe(orig_data , theta , n , STOP_ITER , thresh=5000 , alpha=0.000001)

# %% md

#### 根据损失值停止

# %% md

设定阈值
1E-6 , 差不多需要110
000
次迭代

# %%

runExpe(orig_data , theta , n , STOP_COST , thresh=0.000001 , alpha=0.001)

# %% md

#### 根据梯度变化停止

# %% md

设定阈值
0.05 , 差不多需要40
000
次迭代

# %%

runExpe(orig_data , theta , n , STOP_GRAD , thresh=0.05 , alpha=0.001)

# %% md

### 对比不同的梯度下降方法

# %% md

#### Stochastic descent

# %%

runExpe(orig_data , theta , 1 , STOP_ITER , thresh=5000 , alpha=0.001)

# %% md

有点爆炸。。。很不稳定 , 再来试试把学习率调小一些

# %%

runExpe(orig_data , theta , 1 , STOP_ITER , thresh=15000 , alpha=0.000002)

# %% md

速度快，但稳定性差，需要很小的学习率

# %% md

#### Mini-batch descent

# %%

runExpe(orig_data , theta , 16 , STOP_ITER , thresh=15000 , alpha=0.001)

# %% md

浮动仍然比较大，我们来尝试下对数据进行标准化
将数据按其属性(按列进行)
减去其均值，然后除以其方差。最后得到的结果是，对每个属性 / 每列来说所有数据都聚集在0附近，方差值为1

# %%

from sklearn import preprocessing as pp

scaled_data = orig_data.copy()
scaled_data[: , 1:3] = pp.scale(orig_data[: , 1:3])

runExpe(scaled_data , theta , n , STOP_ITER , thresh=5000 , alpha=0.001)

# %% md

它好多了！原始数据，只能达到达到0
.61，而我们得到了0
.38
个在这里！
所以对数据做预处理是非常重要的

# %%

runExpe(scaled_data , theta , n , STOP_GRAD , thresh=0.02 , alpha=0.001)

# %% md

更多的迭代次数会使得损失下降的更多！

# %%

theta = runExpe(scaled_data , theta , 1 , STOP_GRAD , thresh=0.002 / 5 , alpha=0.001)

# %% md

随机梯度下降更快，但是我们需要迭代的次数也需要更多，所以还是用batch的比较合适！！！

# %%

runExpe(scaled_data , theta , 16 , STOP_GRAD , thresh=0.002 * 2 , alpha=0.001)


# %% md

## 精度

# %%

# 设定阈值
def predict(X , theta):
    return [1 if x >= 0.5 else 0 for x in model(X , theta)]


# %%

scaled_X = scaled_data[: , :3]
y = scaled_data[: , 3]
predictions = predict(scaled_X , theta)
correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a , b) in zip(predictions , y)]
accuracy = (sum(map(int , correct)) % len(correct))
print('accuracy = {0}%'.format(accuracy))
