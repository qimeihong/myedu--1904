def open_write():
    text_io =open('test.text','w+')
    for i in range(5):
        text_io.write('哇哇哇1234\n')

def open_writel():
    text_io = open('test.text','a+')
    for i in range(5):
        text_io.write('哇哇哇\n')

def open_read():
    text_io = open('test.text','r')
    print(text_io.readline())

if __name__ == '__main__':
    open_write()
    open_writel()
    open_read()
