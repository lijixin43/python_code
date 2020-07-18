# AUTHOR lijixin

# def transfrom(rat):
#     money = input("请输入金额(输入E退出程序)：")
#     unit = money[-3:]
#     if money != 'E':
#         money_val = eval(money[:-3])
#         if unit == 'USD':
#             print('对应的人民币金额为：', money_val / rat)
#         elif unit != 'RMB':
#             print('对应的人民币金额为：', money_val * rat)
#     elif money == 'E':
#         print('退出程序！')
#
# if __name__ == '__main__':
#     rat = 6.78
#     transfrom(rat)

class Student(object):

    def __init__(self, name,age, chinese_score,math_score,english_score):
        self.name = name
        self.age = age
        self.chinese_score = chinese_score
        self.math_score = math_score
        self.english_score = english_score

def get_name(self):
    print(self.name)
    print(type(self.name))
def get_age(self):
    age = int(self.age)
    # print(int(self.age))
    print(age)
    print(type(age))
def get_score(self):
    c_score =self.chinese_score
    m_score = self.math_score
    e_score = self.english_score
    if c_score < m_score:
        if m_score< e_score:
            score = int(e_score)
            print(score)
        else:
            score = int(m_score)
            print(score)
    else:
        if c_score <  e_score:
            score = int(e_score)
            print(score)
        else:
            score = int(c_score)
            print(score)

if __name__ == '__main__':
    stu = Student('zhangsan','20','80','90','92')
    get_name(stu)
    get_age(stu)
    get_score(stu)