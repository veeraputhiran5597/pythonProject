# import  collections as col
#
# emp=col.namedtuple("emp_data",["name","city","salary"])
#
# data_list=["veera","chennai",15000]
#
# e1=emp._make(data_list)
#
# print(e1)

# my_dic={"name":"raja","city":"theni","salary":30000}
#
# e2=emp(**my_dic)
#
# print(e2)
#
# from collections import defaultdict
#
# def def_value():
#     return "not present"
#
# d=defaultdict(def_value)
#
# d["a"]=1
# d["b"]=2
#
# print(d)
# print(d["a"])
# print(d["b"])
# print(d["c"])

from collections import UserList,UserDict

# my_list=[1,2,3,4,5]
#
# class mydata1(UserList):
#     def pop(self,s=None):
#         raise RuntimeError("Deletion not allowed")
#
# obj=mydata1(my_list)
#
# obj.append(99)
#
# print(obj)
#
# obj.pop()
#
# print(obj)


my_dict={"x":10,"y":20}
class mydata2(UserDict):
    def pop(self,s=None):
        raise RuntimeError("Deletion not allowed")

obj2=mydata2(my_dict)


obj2.pop()

print(obj2)
