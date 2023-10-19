# a=input("please enter name:")
# b={}
# for i in a:
#     print(i)
#     if i not in b:
#         b[i]=1
#     else:
#         b[i]=b[i]+1
#         # c=max(b,key=b.get)
#
#
# print(b)
# # print(c)
# c=0
# for i in b:
#     # print(b[i])
#     if b[i]>c:
#       c=b[i]
#       d=[i]
# print(c)
# print(d)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for i in num_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

num_dict = {"even": even, "odd": odd}

print(num_dict)


