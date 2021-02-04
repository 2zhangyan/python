#! /usr/bin/env python3
# start -- 学习日期 2021-1-15

# 输出hello word --单行注释

'''
 1
 2
 3
-- 多行注释
'''

"""
2
3
-- 多行注释
"""


print(30)
print("="*20) # 输出20个等号

print("hello word")

name = input("请输入你的名字:")  # 输入你的键盘值


# 占位符以及部分含义 start #

one_zhan = "{}:{}".format(10, 20)
print(one_zhan)

two_zhan = "{1}{0}".format(10,20)
print(two_zhan)

three_zhan = "姓名: {}, 年龄: {}".format("zhangyan",18)
print(three_zhan)

four_zhan = "{:.2f}".format(10.107817) # 取 两位小数
print(four_zhan)

five_zhan = "{:o}".format(100) # b 二进制; d 十进制; x 十六进制; o 八进制
print(five_zhan)

six_zhan = "{:8}:{:10}".format(10,20)  # 占位占宽度8
print(six_zhan)

seven_zhan = "{:<8}:{:>8}".format(10,20) # <> 代表靠左靠右
print(seven_zhan)

# 占位符以及部分含义 end #

leixing  = type(123)
print(leixing) # 输出类型


# 赋值
a = b = c = 10
print(a,b,c)

# 顺序赋值
x,y,z = 10,20,30
print(x,y,z)

# python 缩进 属于模块下的内容
if True:
    print(111)
if False:
    print(222)

print(333)
