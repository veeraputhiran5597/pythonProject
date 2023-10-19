# def addfun(arg,arg1):
#     a=arg+arg1
#     print(a)
# addfun(1,2)

# a=lambda x,y:x+y
# print(a(1,2))

# a=int(input("enter value:"))

# def addfun(arg):
#     abc=arg*arg
#     print(abc)
# addfun(a)

# anaminos function
#
# abc=lambda x:x*x
# print(abc(a))

# lamda have 3 methood
# filter
# map
# reduce

out1=[1,2,3,4,5]

# out2=[i**3 for i in out1]
#
# print(out2)

# out3=list(map(lambda i:i*i,out1))
# print(out3)

# out4=list(filter(lambda i:i%2==0,out1))
# print(out4)


from functools import reduce

b=reduce(lambda  i,j:i+j,out1)
print(b)

c=reduce(lambda  i,j:i*j,out1)
print(c)

# from functools import reduce
#
# # Step 1: Define a list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # Step 2: Use filter to get even numbers
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#
# # Step 3: Use reduce to multiply even numbers
# result = reduce(lambda x, y: x * y, even_numbers)
#
# # Print the result
# print(result)