# a="1001"
# b=""
# for i in a:
#     if i=="1":
#         b+="0"
#     else:
#         b+="1"
#
# print(b)
# print(type(b))

custumer=[{"name":"ram","age":43},{"name":"mani","age":36},{"name":"raja","age":42},{"name":"viki","age":24},{"name":"sundhar","age":48},{"name":"lax","age":46},
          {"name":"logu","age":45},{"name":"selva","age":41},{"name":"kumar","age":27},{"name":"velraj","age":63}]

evenN=[]
oddN=[]
AboveT5age=[]
T5to5T=[]


for i in custumer:
    if i["age"]%2 == 0:
        evenN.append(i["name"])
    else:
        oddN.append(i["name"])
    if i["age"]>35:
        AboveT5age.append(i["name"])
    if i["age"]>=35 and i["age"]<=50:
        T5to5T.append(i["name"])

Age_dict = {"even age Names": evenN, "odd age Names": oddN,"above35age":AboveT5age,"35to50":T5to5T} 

print("even",Age_dict["even age Names"])
print("odd",Age_dict["odd age Names"])
print("Above35",Age_dict["above35age"])
print("35to50",Age_dict["35to50"])