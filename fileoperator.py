import csv

import numpy as np

data = []
with open("test.csv",encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    data_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        data.append(row)



data = np.array(data)  # 将list数组转化成array数组便于查看数据结构
header = np.array(data_header)
Jobinfo=data[:,10];
Salary=data[:,1];
name=data[:,0];
place=data[:,5];
print(Salary);
print(name);
print(place);
