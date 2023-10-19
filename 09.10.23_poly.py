class fir_class:
    def __init__(self):
        self.__value1=15
    def fun1(self):
        print(self.__value1)
class sec_class(fir_class):
    def __init__(self):
        self.__value1 = 200
    def fun1(self):
        print(self.__value1)

obj=sec_class()

obj.fun1()

