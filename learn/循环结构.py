#! /usr/bin/env python3
import time

# start -- 学习日期 2021-1-19

# while 循环
# 输出1-10
i = 1
while i <= 10:
    print(i)
    i += 1

# 输出10-1
j = 10
while j >= 1:
    print(j, end=" ")
    j -= 1

# 输出 1-100 的和
k = 1
k_sum = 0
while k <= 100:
    k_sum += k
    print(k, end=" ")
    k += 1
print(k_sum)

# 跳出死循环
while True:
    val = input('请输入一个值:')
    print("内容:",val)
    if  val == 'z':
        break

# for ...in循环

# 遍历字符串
for a in "qw":
    print(a)

for b in [1,2,3,4]:
    print(b)

for c in (5,6,7,8):
    print(c)

# m 取得是键值
d = {'name':'zz','age':'11','sex':'woman'}
for m in d:
    print(m,':',d[m],end="\n")

# 嵌套循环
e = [('a','AAA'),('b','BBB'),('c','CCC')]
for val1,val2 in e:
    print(val1,'===>',val2)

# 输出 0-4
for n in range(5):
    print(n)

for u in range(1, 7):
    print(u)

# 5 每次加5
for y in range(0,51,5):
    print(y)

# 10-1 每次减一
for x in range(10,0,-1):
    print(x)


# 输入 10 - 1 的偶数

for oushu in range(10, 1, -2):
    print(oushu,end=" ")

# 使用range() 和 len() 结合输入列表中的数据
data = ['aaa', 'bbb', 'ccc']
for one in range(len(data)):
    print(one, '=>', data[one])



# 输出乘法口诀表

for one_num in range(1,10):
    for two_num in range(1,one_num+1):
        print('{}*{}={:<4}'.format(one_num, two_num, one_num*two_num), end=" ")
    print("\n")

for one_num in range(9, 1, -1):
    for two_num in range(1, one_num+1):
        print('{}*{}={:<4}'.format(one_num, two_num, one_num*two_num), end=" ")
    print("\n")

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('{}*{}= {:<4}'.format(i, j, i*j), end=" ")
        j += 1
    i += 1
    print("\n")


# break, continue else 和 pass 得用法

# 数据查找

data = (1, 2, 3, 4)
find_data = 3
for one in data:
    if find_data == one:
        print('{}存在'.format(find_data), end=" ")
        break
else:
        print('{}不存在'.format(find_data), end=" ")


print("\n")
for i in data:
    if i == 2:
        pass
        print('pass pass掉了')
    print(i)

now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print('执行完毕,当前时间{}'.format(now_time))

