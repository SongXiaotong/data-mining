import random
import math
import numpy as np
import csv
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('res.xls')
wb = copy(rb)
sheet = wb.get_sheet(0);

time = 20;
N = [20, 50, 100, 200, 300, 500, 1000, 5000];
l = -1;

for num in N:
    pi_list = [];
    l += 1;
    for i in range(time):
        inside = 0;
        for j in range(num):
            x = random.random();
            y = random.random();
            dis = math.sqrt(x**2 + y**2);
            if dis < 1:
                inside += 1;      
        pi = 4*inside/num;
        sheet.write(i+1, l*5+0, num);
        sheet.write(i+1, l*5+1, inside);
        sheet.write(i+1, l*5+2, num-inside);
        sheet.write(i+1, l*5+3, round(pi, 6));
        wb.save('res.xls')
        # print('第'+str(i+1)+'次试验：', inside, outside, round(pi, 3));
        pi_list.append(pi);
    pi_mean = np.mean(pi_list);
    pi_var = np.var(pi_list);
    print('均值为', pi_mean, '方差为', pi_var);

