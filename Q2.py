# 2. Take a list from user, the list contain your Mobile Number and find out the Max and Min number from the list.Create separate function to find out Max and Min.

mylist=[]
Number=int(input("how many items :"))

for i in range(Number):
    tem=int(input("enter {} items :".format(i)))
    mylist.append(tem)
print("this list is:",mylist)
#max in list:
def maximum(l):
    max1=l[0]
    for m in l:
        if m>max1:
            max1=m
    print("maximum number of list is:",max1)



#min in list:
def minimum(m):
    min1=m[0]
    for o in m:
        if o<min1:
            min1=o
    print("minmum number of list is:",min1)

maximum(mylist)
minimum(mylist)
