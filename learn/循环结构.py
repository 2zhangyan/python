#!
import time

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

