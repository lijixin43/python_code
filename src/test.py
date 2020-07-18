# AUTHOR lijixin


# username = 'root'
# pwd1 ='westos'
#
# for i in range(1,4):
#     user = input("请输入用户名:")
#     pwd2 = input("请输入密码:")
#     if  user == username and  pwd1 == pwd2:
#         print('登录成功')
#         break
#     else:
#         if user != username and  pwd1 != pwd2:
#             print("登录失败")
#             print('你还剩余%d次机会' % (3-i))
#         else:
#             print("登录失败")
#             print('你还剩余%d次机会'%(3-i))

def main(hl):
    money = input("请输入带单位的转换金额(输入Q退出程序)：")
    if money != 'Q':
        unit = money[-3:]
        money_val = eval((money[:-3]))
        if unit == 'USD':
            print('对应的人民币金额为：', money_val/hl)
        elif unit == 'RMB':
            print('对应的美元金额为：', money_val * hl)
        main(hl)
    elif money == 'Q':
        print('程序已退出！')


if __name__ == '__main__':
    hl = 6.77
    main(hl)

