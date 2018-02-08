#__name__ 属性
#有时候我们想将一个 .py 文件既当作脚本，
#又能当作模块用，这个时候可以使用 __name__ 这个属性。

#只有当文件被当作脚本执行的时候， __name__的值才会是 '__main__'，
#所以我们可以：
PI = 3.1416
def sum(lst):
    """ Sum the values in a list
    """
    tot = 0
    for value in lst:
        tot = tot + value
    return tot

def add(x, y):
    " Add two values."
    a = x + y
    return a

def test():
    w = [0,1,2,3]
    assert(sum(w) == 6)
    print ('test passed.')
    
if __name__ == '__main__':
    test()