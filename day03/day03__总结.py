import os


def for_demo():
    for q in range(5):
        print('hello world')
        print(q)

def for_demo1():
    for q in range(5,10):
        print('hello world')
        print(q)
def for_demo2():
    for q in range(5,10,2):
        print(q)
    for q in range(15,10,-2):
        print(q)
list
def for_list():
    w = ['1','2','3',4,5,6]
    # for q in w:
    #     print(q)

    for q in range(len(w)):
        print(w[q])
# 嵌套循环
def for_for():
    for q in range(5):
        print('nihao')
        for w in range(2):
            print('shijie',end=',')
            print('\n')
def break_continue():
    for  q in range(5):
        print(q)
        if q ==2 :
            # 终止所以循环
            break
    for q in range(5):
        if q ==2 :
            # 停止本次循环,直接开始下一次循环
            continue
        print(q)


def assert_int():
    try:
        assert 3>2
        assert 3==3
        assert 2<3
    except:
        print('断言失败了')
def assert_str():
    a = '成功'
    b = '操作成功'
    try:
        assert a in b
        assert '成功'=='成功'
        assert a not in b
    except:
        print('断言失败了')



def if_demo():
    a = 3>4
    if a :
        print('a 是True')
    else:
        print('a 是 Flase')

def elif_demo():
    a =4
    if a==1:
        print('a 是1')
    elif a==2:
        print('a是2')
    elif a==3:
        print('a是3')
    elif a==4:
        print('a是4')
    else:
        print('a不是1,2,3,4')



avar ='你好'
def d1():
    print(avar)
    bvar = '一般般'
def d2():
    print(bvar)
def d3():
    global avar
    avar = '世界'


def while_demo():
    a = 0
    while a<5:
        print(a)
        a=a+1



def jisuan(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)

def duibi(a,b,c):
    print(a>b)
    print(a<b)
    print(a == b)
    print(a <= c)
    print(a >= b)
    print(a != b)

def deng(a):
    a=a+1
    print(a)
    a=a-1
    print(a)
    a*=3
    print(a)
    a/=9
    print(a)



# 求1到50之间的奇数和
def sum_demo():
    sum = 0
    for i in range(1, 50):
        k = i % 2
        if k == 1:
            sum =sum+i
    print(sum)

# 打印九九乘法表
def jiujiu():
    for i in range(1,10):
        x=i+1
        for j in range(1,x):
            print('%s * %s =%s'%(j,i,j*i),end='  ')
        print('')

# 求两个数之间的偶数和
def sum_demo1(a,b):
    sum = 0
    if a<b:
        for i in range(a,b):
            if i%2 ==0:
                sum = sum+i
    elif a>b:
        for i in range(b,a):
            if i %2 ==0:
                sum = sum+i
    else:
        print('a和b相等')
        print(sum)

'''
每次拿 4 个 最后剩一个, 
每次拿五个剩四个,
每次拿6个 最后剩3个,
每次拿七个最后剩5个,
每次拿八个最后剩一个,
每次拿九个 刚好拿完, 篮子最多放1000个鸡蛋,求有多少鸡蛋
'''
# 篮子拿鸡蛋：方法一
def jidan():
    for i in range(1,1000):
        if (i % 4 == 1):
            if (i % 5 == 4):
                if (i % 6 == 3):
                    if (i % 7 == 5):
                        if (i % 8 == 1):
                            if (i % 9 == 0):
                                print(i)

# 篮子拿鸡蛋:方法二
def jidan2():
    for i in range(1,1000):
        if i % 4 !=1:
            continue
        if i % 5 !=4:
            continue
        if i % 6 !=3:
            continue
        if i % 7 !=5:
            continue
        if i % 8 !=1:
            continue
        if i % 9 !=0:
            continue
        print(i)




if __name__ == '__main__':
    # for_demo()
    # for_demo1()
    # for_demo2()
    # for_list()
    # for_for()
    # break_continue()
    # assert_int()
    # elif_demo()
    # pwd = os.getcwd()
    # print(pwd)
    # a = os.path.abspath('..')
    # print(a)
    # b = os.path.abspath('../..')
    # print(b)


    # try:
    #     print('错误之前')
    #     a=5/0
    #     print('错误之后')
    # except:
    #     print('报错了')
    # print('123456')
    # d1()
    # d3()
    # d1()
    # while_demo()
    # jisuan(10, 3)
    # sum_demo()
    # jiujiu()
    # sum_demo1
    # jidan()
    jidan2()

