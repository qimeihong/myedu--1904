def jisuan(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)

def duibi(a,b,c):
    print(a > b)
    print(a < b)
    print(a == b)
    print(a <= c)
    print(a >= b)
    print(a != b)

def deng(a):
    a =a+1
    print(a)

    a =a-1
    print(a)

    a*=3
    print(a)

    a/=9
    print(a)

if __name__ == '__main__':
    deng(6)