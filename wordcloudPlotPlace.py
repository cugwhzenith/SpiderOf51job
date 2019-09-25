import numpy as np
from PIL import Image
import re
import jieba
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
# import wordcloud
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
# 打开存放项目名称的txt文件
# with open('content.txt','r',encoding='utf-8') as f:
#    word= (f.read())
#    f.close()
str="";
word=str.join(place);

# 图片模板和字体
# image=np.array(Image.open('ditu.jpg'))#显示中文的关键步骤
font=r'C:\\Windows\\fonts\\msyh.ttf'

# 去掉英文，保留中文
resultword=re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\。\@\#\\\&\*\%\-]", "",word)
#resultword=re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\。\@\#\\\&\*\%]", "",word)
# 现在去掉了中文和标点符号
wordlist_after_jieba = jieba.cut(resultword)
wl_space_split = " ".join(wordlist_after_jieba)
print(wl_space_split);
# 设置停用词
sw = set(STOPWORDS)
sw.add("研发")
sw.add("系列")
sw.add("区")

# 关键一步
my_wordcloud = WordCloud(font_path=font,scale=4,stopwords=sw,background_color='white',
                         max_words = 100,max_font_size = 60,random_state=20).generate(wl_space_split)
#my_wordcloud = WordCloud(background_color='white',
#                         width=800,height=600,margin=2).generate(wl_space_split)
#显示生成的词云
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

#保存生成的图片
my_wordcloud.to_file('place.jpg')



