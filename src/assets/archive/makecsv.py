import csv
import random

alldata=[]

with open('DBP_wiki_data.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    print("数据1读取结束")
    for i in reader:
        alldata.append(i)

    print("数据2读取结束")

csvFile1 = open("DBP_wiki500.csv", mode="w", encoding='utf-8')
csvFile2 = open("DBP_wiki1000.csv", mode="w", encoding='utf-8')
csvFile3 = open("DBP_wiki2000.csv", mode="w", encoding='utf-8')

writer1 = csv.writer(csvFile1)
writer2 = csv.writer(csvFile2)
writer3 = csv.writer(csvFile3)


writer1.writerows(random.sample(alldata, 500))
print("数据1写入结束")
writer2.writerows(random.sample(alldata, 1000))
print("数据2写入结束")
writer3.writerows(random.sample(alldata, 2000))
print("数据3写入结束")