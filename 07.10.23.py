# oops-
# class-cloctoin of function
# object
# init-consector-orru class run pannum pothu initial la obj create pannum
# ingretions

# class abcd:
#     def __init__(self,a,b):
#         self.e_name=a
#         self.b_name=b
#
#     def emp_name(self):
#         print("emp name",self.e_name)
#     def Branch_name(self):
#         print("branch name",self.b_name)
#
# obj=abcd('veera','chennai')
# obj.emp_name()
# obj.Branch_name()


# class abcd:
#
#     def emp_name(self):
#         print("emp name")
#     def Branch_name(self):
#         print("branch name")
#
# class xyz(abcd):
#     def fun1(self):
#         print("fun1")
#
# class students(xyz):
#     def student_name(self):
#         print("student name")
#
# obj=students()
# obj.Branch_name()


# class cla1:
#     def fun1(self):
#         print("fun 1")
# class cla2(cla1):
#     def fun2(self):
#         print("fun 2")
# class cla3(cla2):
#     def fun3(self):
#         print("fun 3")
#
# obj=cla3()
# obj.fun1()

# class A:
#     def fun1(self):
#         print("fun1")
#     def fun1(self,a):
#         print("fun2",a)
#
# obj=A()
# obj.fun1(10)
#
# class A:
#     def __init__(self):
#         self.value1=10
#     def fun1(self):
#         print(self.value1)
#
# obj=A()
# obj.fun1()
# obj.value1=2000
# obj.fun1()

class A:
    def __init__(self):
        self.__value1=10
    def fun1(self):
        print(self.__value1)
    def fun2(self):
        self.__value1=1000
        print(self.__value1)

obj=A()

obj.fun1()
obj.__value1=500
obj.fun1()
obj.fun2()


