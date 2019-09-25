
import re
import jieba
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import  matplotlib.pyplot as plt
import csv
import numpy as np

data = []
with open("51job.csv",encoding='gbk') as csvfile:
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

word="".join(Jobinfo);


font=r'C:\\Windows\\fonts\\msyh.ttf'#显示中文的关键步骤

# 去掉英文，保留中文
resultword=re.sub("[0-9\u4e00-\u9fa5\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\。\@\#\\\&\*\%\-]", "",word)
# 现在去掉了中文和标点符号
wordlist_after_jieba = jieba.cut(resultword)
wl_space_split = " ".join(wordlist_after_jieba)
print(wl_space_split);
# 设置停用词
sw = set(STOPWORDS)
sw.add("，")
sw.add("；")
sw.add("Responsibilities")
sw.add("experience")
sw.add("knowledge")
sw.add("communication")
sw.add("skill")
sw.add("office")
sw.add("support")
# 关键一步
my_wordcloud = WordCloud(font_path=font,scale=4,stopwords=sw,background_color='white',
                         max_words = 100,max_font_size = 60,random_state=20).generate(wl_space_split)

#显示生成的词云
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

#保存生成的图片
my_wordcloud.to_file('Jobinfo.jpg')



