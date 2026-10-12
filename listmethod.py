# list=[]
# print(list)

# number=[1,2,3]
# print(number(0))
# print(number(-2))

# color=["red","blue"]
# color.append("green")
# print("after adding",color)



# list=[1,2,3,4,5,6,7,8,9,10]
# print(list)

# a=list[3]/2
# list.append(a)
# print(list)

# print(sum(list[-4::]))

# list.pop(1)
# list.pop(4)
# print(list)

# difference=max(list)-min(list)
# print("Difference of highest and lowest:",difference)

list=[1,6,5,4,2,3,7,8,9]
b=list.count()
sum=0
for i in b:
    if list[i]//2==0:
        sum=sum+list[i]
print(sum)
    