# AUTHOR lijixin

import json

#创建一个字典
dict = {"name":'图图',"age":'3'}
with open('file.txt', 'w',encoding="utf-8") as file:
     file.write(json.dumps(dict))
     # file.write(json.dumps(dict))


# fr = open(r"file1.txt","a+",encoding="utf-8")
# dict ={"name":'图图',"age":'3'}
# #遍历整个字典，输出key,value值
# for key,value in dict.items():
#     fr.write("输入key值"+str(key))
#     fr.write("输入value值"+str(value)+'\n')