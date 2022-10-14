def test():
    print("test function run")


def test2(func):
    print("test2 function run")


a = test  # 函数赋值给a
test2(a)
a()
