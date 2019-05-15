#-*- coding: utf-8 -*-  
import random
from numpy import *
import matplotlib.pyplot as plt

x_input, x_test = ones((50,3)), ones((10,3))
y_input, y_test = zeros((50,1)), ones((10,1))
s, d, y= [], [], []

# 初始化输入矩阵和输出矩阵 
file = open('dataForTraining.txt', 'r').readlines()
data = file[i].strip('\n').split(' ')
file2 = open('dataForTesting.txt', 'r').readlines()
data2 = file2[i].strip('\n').split(' ')
for i in range(50):
    s.append(float(data[0]))
    d.append(float(data[1]))
saver = mean(s)
daver = mean(d)
svar = std(s)
dvar = std(d)

for i in range(50):
    x_input[i][1] = (float(data[0])-saver)/svar
    x_input[i][2] = (float(data[1])-daver)/dvar
    y_input[i][0] = float(data[2])
    if i < 10:
        x_test[i][1] = (float(data2[0]) - saver)/svar
        x_test[i][2] = (float(data2[1]) - daver)/dvar
        y_test[i][0] = float(data2[2])
# 初始化theta
theta = [[0], [0], [0]]

# 均方误差计算结果
def error(X, theta, Y, m):
    a = X/m
    b = dot(a, theta) - Y/m
    return dot(transpose(b), b) * m / 2

# 微分计算结果
def diff(X, theta, Y, m):
    a = X/m
    b = dot(a, theta) - Y/m
    return dot(transpose(a), b) * m

# 预测值
def pred(X, theta, r):
    y = zeros((r, 1))
    for i in range(r):
        y[i][0] = theta[0][0] + theta[1][0]*X[i][1] + theta[2][0]*X[i][2]
    return y

time = 150000
K = 10000
step = 0.00015
m = 50
axis_x, axis_y_train, axis_y_test = [], [], []
for i in range(1, time+1):
    theta = theta - step*diff(x_input, theta, y_input, m)
    if i % K == 0:
        axis_x.append(i)
        axis_y_train.append(error(x_input, theta, y_input, m)[0][0])
        axis_y_test.append(error(x_test, theta, y_test, 10)[0][0])
        print(theta)
        print(error(x_input, theta, y_input, m)[0][0], error(x_test, theta, y_test, 10)[0][0])
# print(pred(x_input, theta, 50))
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)

ax1.set_title('training data')
ax2.set_title('testing data')
ax1.set_xlabel('time')
ax2.set_xlabel('time')
ax1.set_ylabel('J')
ax2.set_ylabel('J')
ax1.scatter(axis_x, axis_y_train, c='k', marker='.')
ax2.scatter(axis_x, axis_y_test, c='m', marker='.')
plt.show()
