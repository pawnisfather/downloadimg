#定义函数：完成包裹数据
def makeBold(fn):
    print("makebold")
    def wrapped(*args,**kwargs):
        print("----1---")
        return "<b>" + fn(*args,**kwargs) + "</b>"
    return wrapped


@makeBold
def test3(a,b,c):
    print("----3---",a,b,c)
    return "hello world-3"

if __name__ == '__main__':

    ret = test3(1,2,3)
    print(ret)
