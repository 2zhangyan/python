#!
# start -- 学习日期 2021-1-15

'''
流程控制介绍
1 顺序结构
2 分支结构/选择结构
3 循环结构
'''

# 单项分支
if True:
    print('真的')

print('end')


# 双项分支

s_tr = str(input('小张张是好人吗'))

if s_tr == 'yes':
    print('恭喜,你答对了')

else :
    print('很遗憾,你错的离谱')

print('奥利给')


# 多项分支 -- 没有switch
# 巣状分支
pig = str(input('小坤坤是猪嘛'))

if pig == 'yes':
    print('你真的太聪明了')
elif pig == 'no':
    ture_pig = str(input('再给你一次机会哦'))
    if ture_pig == 'yes':
            print('可以可以 脑袋在线了')
else:
    print('真是傻的可爱')

print('嗯哼')