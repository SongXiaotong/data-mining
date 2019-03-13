import random
import math
import numpy as np
import csv
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('monto.xls')
wb = copy(rb)
sheet = wb.get_sheet(0);

time = 100;
N = [5, 10, 20, 30, 40, 50, 60, 70, 80, 100];
l = -1;

for num in N:
    s_list1 = [];
    s_list2 = [];
    l += 1;
    for i in range(time):
        cur_row = 1;
        inside = 0;
        x = np.random.uniform(0, 1, num);
        y1 = np.random.uniform(0, 1, num);
        y2 = x*x*x;
        s1 = np.mean(y2)*1;
        s_list1.append(s1);
        for j in range(len(y1)):
            if y1[j]<y2[j]:
                inside += 1;
        s2 = inside / num * 1;
        s_list2.append(s2);
        sheet.write(i+1, l*7+0, i);
        sheet.write(i+1, l*7+1, num);
        sheet.write(i+1, l*7+2, np.mean(x));
        sheet.write(i+1, l*7+3, np.mean(y1));
        sheet.write(i+1, l*7+4, s1);
        sheet.write(i+1, l*7+5, s2);

        wb.save('monto2.xls')
        # print('第'+str(i+1)+'次试验：', inside, outside, round(pi, 3));
    s_mean = np.mean(s_list1);
    s_var = np.var(s_list1);
    print(num, '均值为', s_mean, '方差为', s_var);
    s_mean = np.mean(s_list2);
    s_var = np.var(s_list2);
    print(num, '均值为', s_mean, '方差为', s_var);

