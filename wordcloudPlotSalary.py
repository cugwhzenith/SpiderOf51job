import re
import matplotlib.pyplot as plt
import csv
import numpy as np

data = []
with open("51job.csv",encoding='gbk') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
    data_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到data中
        data.append(row)

data = np.array(data)  # 将list数组转化成array数组便于查看数据结构
header = np.array(data_header)
Jobinfo=data[:,10];
Salary=data[:,1];
name=data[:,0];
place=data[:,5];


word="".join(Salary);


font=r'C:\\Windows\\fonts\\msyh.ttf'#显示中文的关键步骤

# 去掉英文，保留中文
resultword=re.sub("[A-Za-z\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\<\>\?\~\。\@\#\\\&\*\%]", " ",word)
# 现在去掉了中文和标点符号
wl_space_split = resultword
salary_info=wl_space_split.split();
salary_list=[];

for s in salary_info:
    if(s[-1])=="年":
        ans=re.sub("[\u4e00-\u9fa5A-Za-z\/\-]", " ",s).split()
        sum=0;
        for i in ans:
            sum+=float(i)
        avg=sum/len(ans)/12
    elif (s[-1])=="月":
        ans = re.sub("[\u4e00-\u9fa5A-Za-z\/\-]", " ", s).split()
        sum=0;
        for i in ans:
            sum+=float(i)
        avg=sum/len(ans)
    elif (s[-1])=="天":
        ans = re.sub("[\u4e00-\u9fa5A-Za-z\/\-]", " ", s).split()
        sum=0;
        for i in ans:
            sum+=float(i)
        avg=sum/len(ans)*30
    salary_list.append(avg)

salary_array = np.array(salary_list)
salary_array[salary_array>6]=-0.00001 #剔除大于6的异常数据或者不合实际的数据
plt.rcParams['font.sans-serif']=['SimHei']
plt.hist(salary_array, bins =  [0,1,2,3,4,5,6])

plt.xlabel("工资区间(单位：万/月)") #设置X轴Y轴名称
plt.ylabel("数量")
plt.title("前程无忧大数据岗位工资(N="+str(len(salary_array))+",mean="+ str(round(salary_array.mean(),2))+ "万/月)")
plt.savefig('salaryHist.jpg')
plt.show();




