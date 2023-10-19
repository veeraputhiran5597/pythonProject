alist = [{1,8},{1,9},{4,5},{2,7},{5,6}]
li=set()

for i in alist:
   li.update(i)

print(li)
li=list(li)
a=li[0]
b=0
for i in li:
  if i>a:
    a=i
  else:
    b=i

li={b,a}
print(li)

# for i in range(1,11):
#   print(i,"*",7,"=",i*7)











# disnary python 3.6 versionku approm than order irruku athuku munnadi unorder









