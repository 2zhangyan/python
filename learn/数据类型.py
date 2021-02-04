#! /usr/bin/env python3
# start -- 学习日期 2021-1-15

# 数字 int bool float complex

a = 10
b = 1.7
c = True
d = 4+2j
print(type(a), type(b), type(c), type(d))

x = bin(8) # 二进制
y = oct(8) # 八进制
z = hex(8) # 十六进制
print(x,y,z)


# 字符串

f = 'abc'
g = 'as\'d'
h = 'asd\nsss'
j = r'asd\nsss' # \n 不代表换行
k = 'asd\\nsss'

print(f,g,h,j,k)

name = 'zhangyan'
print(name[0],name[2],name[0:5],name[-1],name[-1:2])

# 列表

a = [10,20,30]
b = [30,50]
print(type(a), a[0], a[1:2], a[2:], a + b)
a[0] = 1
print(a)

# 元祖
# tuple 与列表不同的是这个值不能改变 []  ()

a = (1,2,3)
print(type(a), a[0], a[2:])


# 集合 set
# 交集 差集 不能合并
a = {1,2,3}
b = {3,4,5}
c = a & b
d = a - b
e = a | b
f = b | a

print(type(a), c, d, e, f)


# 字典

a = {'name':'zhangyan', 'sex':'女', 'age':'8'}
print(type(a), a['name'])

a['name'] = 'hh'
print(a,a.keys(),a.values(),type(a.keys()))

# 类型之前的转换
a = str(10)
b = int("10")
c = list({1,2,3})
d = set((1,2,3))
e = dict([('a','aaa'),('b','bbb')])
f = tuple([1,2,3])
h = tuple("aaa")

print(a,b,c,d,e,f,e['a'],h)




