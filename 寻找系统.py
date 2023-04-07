import time


def peb(x,y):
    a,b=0,1
    print('{}和{}之间的裴波那契数列为：{},{},'.format(x,y,a,b),end='')
    while b<=y:
        a,b=b,a+b
        if b>=x and b<=y: print(b,end=',')
    print()


def zhs(x,y):
    print('{}和{}之间的质数有：'.format(x,y),end='')
    for i in range(x,y+1):
        for j in range(2,i):
            if i%j==0: break
        else:
            if i==2: print(2,end=',')
            elif i>2: print(i,end=',')
    print()


def hsh(x,y):
    print('{}和{}之间的合数有：'.format(x, y), end='')
    for i in range(x,y+1):
        for j in range(2, i):
            if i%j==0:
                print(i,end=',')
                break
    print()


def amu(x,y):
    print('{}和{}之间的阿姆斯特朗数有：'.format(x,y),end='')
    for i in range(x,y+1):
        n,m,sum=len(str(i)),i,0
        while m>0:
            digit=m%10
            sum+=digit**n
            m//=10
        if sum==i: print(i,end=',')
    print()


while True:
    try:
        input('\r按Enter键继续')
        print('''请选择你的操作：
    1.寻找质数
    2.寻找合数
    3.寻找裴波那契数列
    4.寻找阿姆斯特朗数
    5.退出''')
        di=int(input('输入对应序号:'))
        if di==5:
            print('正在退出...')
            time.sleep(1)
            print('感谢您的使用')
            break
        elif di==1:
            x=int(input('请输入范围最小值：'))
            y=int(input('请输入范围最大值：'))
            zhs(x,y)
        elif di==2:
            x=int(input('请输入范围最小值：'))
            y=int(input('请输入范围最大值：'))
            hsh(x,y)
        elif di==3:
            x=int(input('请输入范围最小值：'))
            y=int(input('请输入范围最大值：'))
            peb(x,y)
        elif di==4:
            x=int(input('请输入范围最小值：'))
            y=int(input('请输入范围最大值：'))
            amu(x,y)
        else: print('你输入的序号不正确')
    except: print('你的输入不正确')