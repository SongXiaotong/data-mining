import numpy as np
import math
import matplotlib.pyplot as plt
import csv
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

def points(x1, x2, y1, y2, sample_size):
    half = math.floor(sample_size/2)
    rnd1 = np.random.random(size = half)
    rnd2 = np.random.random(size = half)
    rnd2 = np.sqrt(rnd2)
    x = (rnd2 * (rnd1 * x1 + (1 - rnd1) * x1) + (1 - rnd2) * x2).tolist()
    y = (rnd2 * (rnd1 * y1 + (1 - rnd1) * y2) + (1 - rnd2) * y1).tolist()
   # plt.plot(x,y,'ro')     
    rnd1 = np.random.random(size = sample_size - half)
    rnd2 = np.random.random(size = sample_size - half)
    rnd2 = np.sqrt(rnd2)
    x1 = ((rnd2 * (rnd1 * x1 + (1 - rnd1) * x2) + (1 - rnd2) * x2)).tolist()
    y1 = ((rnd2 * (rnd1 * y2 + (1 - rnd1) * y1) + (1 - rnd2) * y2)).tolist()
    x = x+x1
    y = y+y1
    return x, y

def image(x, y, n, i):
    x = np.array(x)
    y = np.array(y)
    plt.plot(x,y,'ro') 
    # axes = plt.gca()
    # axes.set_xlim([x1,x2])
    # axes.set_ylim([y1,y2])
    plt.grid(True)
    plt.savefig('dot'+str(len(x))+'_'+str(i)+'.png')
    plt.clf()
    # plt.show()

N = [10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 500]
times = 100
l = -1

rb = open_workbook('monto.xls')
wb = copy(rb)
sheet = wb.get_sheet(0);

for n in N:
    l += 1
    v_list = []
    for j in range(times):
        x, y = points(2, 4, -1, 1, n)
        # if i < 2:
        #     image(x, y, n, i)
        z_list = []
        for i in range(len(x)):
            z = (y[i]*y[i]*math.exp(-y[i]*y[i]) + math.pow(x[i], 4)*math.exp(-x[i]*x[i]))/(x[i]*math.exp(-x[i]*x[i]))
            z_list.append(z)
        v_list.append(np.mean(z_list)*4)
        sheet.write(j+1, l*5, n)
        sheet.write(j+1, l*5+1, np.mean(x))
        sheet.write(j+1, l*5+2, np.mean(y))
        sheet.write(j+1, l*5+3, np.mean(z_list)*4)
        wb.save('monto.xls')
    print(n, np.mean(v_list), np.var(v_list))

