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



if __name__ == '__main__':
    # for_demo()
    # for_demo1()
    # for_demo2()
    # for_list()
    for_for()