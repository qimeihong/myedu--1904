# 字典以{}包起来，：前面是key,后面是value;多个键值对用，分隔开
adict ={'username':'admin','password':'123456'}
# 字典是无序的，他没有索引，只能通过key,去访问value,并且key 不能重复
def dict_sel():
    print(adict['username'])

#更新字典里面的value
def dict_updat():
# 通过字典key 去 修改value
    adict['username']='qmh'
    print(adict)
# 删除字典里面的键值对
def dict_del():
    adict.pop('username')
    print(adict)

# 添加字典里面的键值对
def dict_add():
    #如果key 在原本的字典中不存在,则会新加一个键值对
    adict['age'] = 25
    print(adict)
    bdict={'list':[1,2,3],'tuple':(4,5)}
    #合并方法一:将bdict 添加adict
    adict.update(bdict)
    print(adict)
    # 合并方式二:将adict和bdict 合并,新生成一个dict
    cdict = {"password":"77777",'class':'1904'}
    #注意第二个字典参数前 要加**
    ddict = dict(adict,**cdict)
    print(ddict)

# 题: 新建一个字典变量,里面有两个键值对,通过key访问一个值,
# 删除一个键值对,添加一个键值对,更改任意一个值,再新建一个字典,将两个合并
www ={"qwer":"aa1","bb2":"cc3"}
def dd_a():
    print(www)
    print(www["qwer"])
    www.pop("qwer")
    print(www)
    www["zxc"] = 20
    print(www)
    www["qwer"]="qmh"
    print(www)
    jkl = {"a": [1, 2, 3], "o": [7, 8]}
    www.update(jkl)
    print(www)



if __name__ == '__main__':
    # dict_sel()
    # dict_updat()
    # dict_del()
    # dict_add()
    dd_a()

