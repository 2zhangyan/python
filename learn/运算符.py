#! /usr/bin/env python3
# start -- 学习日期 2021-1-15

# 连接符; 运算符; 转换函数 算数运算符
one_str = "aa" + "bb"
print(one_str)

two_str = str(10) + "ab"
print(two_str)

three_str = 2**10 # 2 ** 10 2的 10次方; 10/2 除以; 10%3 取余; 10//3 取整;剩下都是普通的 (+-*/)
print(three_str)

four_str = "abc" * 3
print(four_str)

# 连接符; 运算符; 转换函数 end 逻辑运算符

# 判断 返回布尔值

one_res = 10 == 10
print(one_res)

two_res = 10 == 11
print(two_res)

three_res = 10 == 10 and 1==1
print(three_res)

four_res = 10 == 10 or 1==2
print(four_res)

five_res = not (10 == 10)
print(five_res)



# 判断 end

# 赋值 不存在 a++;a--;

a = 1
one_fuzhi = a + 1
print(one_fuzhi)

one_fuzhi  += 1
print(one_fuzhi)

one_fuzhi  -= 1
print(one_fuzhi)

# 赋值 end

# 位运算符

one_wei = bin(8) # bin 转化为二进制
print(one_wei)

'''
1   1  1  1   1 1 1 1
128 64 32 16  8 4 2 1
'''
two_wei = 2<<2 # 2 往前 移两位 8  --- 二进制1000
print(two_wei)

'''
二进制转换
6 == 110
5 == 101
6 & 5 == 100 
6 | 5 == 111
100 转化 十进制 为 4
111 转化 十进制 为 7
'''
three_wei = 6 & 5
print(three_wei)

four_wei = 6 | 5
print(four_wei)
# 位运算符 end

# in; not in 成员运算符

arr = [1,2,3,4]
five_wei = 1 in arr
print(five_wei)

five_wei = 10 not in arr
print(five_wei)


# 身份运算符 is; is not

a = 20
b = 20
six_wei = (a is b) # 此时, is 相当于 ==

x = y = z = 10
print(six_wei,id(a),id(b))
print(id(x),id(y),id(z))

# is 与 == 的区别 is 比对的内存的id   == 比对的是值的本身
m = [1,2,3]
n = m
p = m[:] # 复制
print(n is m, p is not m, id(p), id(m)) # 复制的内存id值不一样

