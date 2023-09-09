#3. Take a list from user, the list contain your Mobile Number and sort the list with ascending order.
mylist=[]
Number=int(input("how many items :"))

for i in range(Number):
    i=int(input("enter {} items :".format(i)))
    mylist.append(i)

print("my list before sorting:",mylist)
#increment loop:
for i in range(len(mylist)-1):
    for j in range(0,len(mylist)-i-1):
        if mylist[j]>mylist[j+1]:
            temp=mylist[j]
            mylist[j]=mylist[j+1]
            mylist[j+1]=temp
print("my list after sorting:",mylist)
