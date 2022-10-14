# print(int('123456'))
# base参数

# print('转换为二进制', int('11110', base=2))
# print('转换为八进制', int('123456', base=8))
# print('转换为十六进制', int('123456', base=16))

# def int2(x, base=2):
#     return int(x, base)
#
#
# print(int2('1111100'))
# print(int2('11011000'))
import functools

int2 = functools.partial(int, base=2)
print(int2('10010011'))
print(int2('11111111'))


