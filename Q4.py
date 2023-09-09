#4. Take a list from user, the list contain your Mobile Number and find out the Even Numbers List and Odd Number List.
mylist=[]
Number=int(input("how many items :"))

for i in range(Number):
    i=int(input("enter {} items :".format(i)))
    mylist.append(i)

def even_odd(m1):
    evenlist=[]
    oddlist=[]
    for i in m1:
        if i%2==0:
            evenlist.append(i)
        elif i%2!=0:
            oddlist.append(i)
    print("newlist is:", mylist)
    print("even list is:",evenlist)
    print("odd list is:",oddlist)
    return evenlist,oddlist,mylist

even_odd(mylist)