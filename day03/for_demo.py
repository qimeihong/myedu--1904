def for_demo():
    for i in range(7):
        print('hell world')
        print(i)

def for_demo1():
    for i in range(4,9):
        print('hello world')
        print(i)

def for_demo2():
    for aaa in range(4,9,3):
        print(aaa)

    for aaa in range(10,6,-4):
        print(aaa)

def for_list():
    jkl = ['7','6','5',4,3,2,1]
    for aaa in jkl:
        print(aaa)

    for aaa in range(len(jkl)):
        print(jkl[aaa])

def for_for():
#end ='xxxx' :让print 以什么内容结尾
    for i in range(3):
        print('nihao')
        for q in range(1):
            print('世界',end=',')
        print('\n')

def break_continue():
    for aaa in range(5):
        print(aaa)
        if aaa ==2 :
            break

    for aaa in range(5):
        if aaa ==2 :
            continue
            print(aaa)

if __name__ == '__main__':
    # for_demo2()
    # for_list()
    # for_for()
    break_continue()
