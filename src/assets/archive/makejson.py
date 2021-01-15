import json
import pandas as pd

file=pd.read_csv("DBP_wiki2000.csv",header=None)
print(file.head(5))

l1_all=[]
for i in file[1]:
    l1_all.append(i)
l1=sorted(set(l1_all),key=l1_all.index)
print(l1,len(l1))
print("++++++++++++++")
dic={}
for i in l1:
    dic[i]={}
# print(dic)
index=0
for index, row in file.iterrows():
    dic[row[1]][row[2]]={}

for index, row in file.iterrows():
    dic[row[1]][row[2]][row[3]]=[]

for index, row in file.iterrows():
    dic[row[1]][row[2]][row[3]].append({"name":row[4],"value":row[5]})
print(dic)

for i in dic:
    print(i,dic[i])

all_data=[]

print("\n")
for j in dic:
    print(j)
    data1=[]
    for i in dic[j]:
        print(i)
        data2=[]
        for k in dic[j][i]:
            print(k)
            dic_each={}
            dic_each["name"]=k
            dic_each["value"]="null"
            dic_each["children"]=dic[j][i][k]
            data2.append(dic_each)
        dic_each2={}
        dic_each2["name"] = i
        dic_each2["value"] = "null"
        dic_each2["children"] = data2
        data1.append(dic_each2)
    dic_each3 = {}
    dic_each3["name"] = j
    dic_each3["value"] = "null"
    dic_each3["children"] = data1
    all_data.append(dic_each3)

print("\n\n")
print(all_data)
print(all_data[3])

filename="test6.json"
f_obj=open(filename,'w')
json.dump(all_data,f_obj)
f_obj.close()
