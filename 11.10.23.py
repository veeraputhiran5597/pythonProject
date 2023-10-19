
# a=iter([1,2,3])
#
# print(next(a))
# print(next(a))
# print(next(a))
#
# b=iter({1,2,3})
#
# print(next(b))
# print(next(b))
# print(next(b))
#
# c=iter((1,2,3))
#
# print(next(c))
# print(next(c))
# print(next(c))

# oru fun ku oru return tha irrukum multiple irrukathu

# def fun1():
#     a=int(input("v1"))
#     b=int(input("v2"))
#     return a
#     c=a+b
#     return c
# myobj=fun1()
# print(myobj)

# def fun1():
#     a=10
#     b=20
#     yield a
#     yield a+b
#     yield a-b
# a=fun1()
# print(next(a))
# print(next(a))
# print(next(a))

# def fun1():
#     a=10
#     return a
# def fun2(arg):
#     b=arg
#     def innerfun():
#         c=b+100
#         return c
#     return  innerfun()
#
# obj=fun1()
# obj2=fun2(obj)
#
# print(obj2)



def fun2(arg):
    b=arg()
    def innerfun():
        c=b+100
        return c
    return  innerfun
def fun3(arg):
    d=arg()
    def innerfun():
        e=d*d
        return e
    return innerfun
@fun3
@fun2
def fun1():
    a=10
    return a

print(fun1())

# @-decrators -entha functionku use panuromo antha fun oda carctor etuthukum




