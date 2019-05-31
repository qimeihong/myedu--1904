def assert_int():
    try:
        assert 3>2
        assert 3==3
        assert 2<3
    except:
        print('dysbl')

def assert_str():
    a = 'cg'
    b = 'czcg'
    try:
        assert a in b
        assert 'cg'=='cg'
        assert a not in b
        print('断言成功')
    except:
        print('dysbl')

if __name__ == '__main__':
    # assert_int()
    assert_str()