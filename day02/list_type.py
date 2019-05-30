
alist =['是打发',2,'你好',6,7,1,3]
def list_sel():
    # 通过索引访问，顺序取值：从0开始数
    print(alist[0])

    print(alist[-3])
    print(alist[2:3])
    print(alist[4:])
    print(alist[:4])

# 删除list的元素
def list_del():
# 删除法，不添加参数，默认删除最后一位
    alist.pop()
    print(alist)
# 删除法，填写参数：索引值，就可以删除指定元素
    alist.pop(3)
    print(alist)

# 增加list中的元素
def list_add():
    blist=[1,2,3,'4']
# 添加元素，添加在末尾
    blist.append('5')
    print(blist)

    clist = [4,5,6]
    #
    blist.extend(clist)
    print(blist)

def list_update():
    qlist = [1,2,6,4,5]
    qlist[0] = 100
    print(qlist)

    qlist[2] =200
    print(qlist)

def list_order_by():
    qlist = [1,2,6,4,5,]
    qlist.sort()
    print(qlist)

    qlist.sort(reverse=True)
    print(qlist)

def list_distinct():
    vlist = [1,2,2,6,6,4,5]
    vlist = list(set(vlist))
    print(vlist)
    print(len(vlist))


def asd1():
    abc = [1, 2, 3, 4, 5.5, ]
    print(abc[2])
    print(abc[1:4])
    abc.pop(3)
    print(abc)
    d=[10,20]
    d.extend(abc)
    print(d)
    abc[0]='5'
    print(len(abc))
    print(abc)

atuple = (1,2,3,4)







if __name__ == '__main__':
    # list_del()
    # list_add()
    # list_add()
    # list_update()
    # list_order_by()
    # list_distinct()
    asd1()
    print(atuple[0])
    print(atuple[0:3])