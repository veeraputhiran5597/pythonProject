a=[1,2,3,4,5]

b=[i for i in a if i%2==0]

print(b)

c=[i for i in a if i<=3 if i>=3]

d=[i*i for i in a if i>3]

e=[i if i>3 else "false" for i in a]

f=[i**2 if i%2==0 else i**3 for i in a]

g=["even" if i%2==0 else "odd" for i in a]

for i in a:
    if i%2==0:
        print(i**2)
    else:
        print(i**3)

print(c)

print(d)

print(e)

print(f)

print(g)


x=10
y=20

# x,y=y,x

temp=x
x=y
y=temp

print(x)
print(y)
