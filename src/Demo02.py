# AUTHOR lijixin

class Dictclass(object):
   def __init__(self,dict):
        self.dict = dict
   # 删除key值
   def decl_dict(self,key):
        if key in self.dict.keys():
            del self.dict[key]
            return self.dict
        else:
            print('not found')



   # 判断某个key值是否存在
   def get_dict(self,key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return 'not found'

   # 返回键组成的列表
   def get_key(self,key):
        if key in self.dict.keys():
            return self.dict
        else:
            return 'not found'


if __name__ == '__main__':
    # dict([["name", "zh"], ["age", "18"]])
    dic = Dictclass({"name": "张三", "age":"18"})
    key1 = str(input("输入要查找的内容:"))
    print(dic.get_dict(key1))
    key2 = str(input("输入要删除的内容:"))
    print(dic.decl_dict(key2))
    key3 = str(input("输入要查找的整个dict的内容:"))
    print(dic.get_key(key3))
