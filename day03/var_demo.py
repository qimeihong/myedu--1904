# 全局变量
avar = '你好'
def d1():
    # 可以使用全局变量
    print(avar)
    # 在方法内部声明的变量，只能在方法内部使用
    bvar ='一般般'

def d2():
    # 无法使用其他方法内
    print(bvar)

def d3():
    global avar
    avar = '世界'
if __name__ == '__main__':
    d1()
    d3()
    d1()
