# 1. Create a Function with Your Name. the Function Print your Name, Address, Mobile Number and Age.

def Ajoy(na,ad,nu,ag):
    print("My name is:",na)
    print("My address is:",ad)
    print("My mobile number is:",nu)
    print("My age is:",ag)
    
name=(input("enter name:"))
address=(input("enter address:"))
number=(input("enter mobile no:"))
age=int(input("enter age:"))

Ajoy(name,address,number,age)



#or
def Ajoy():
    n=(input("enter name:"))
    a=(input("enter address:"))
    m=(input("enter mobile no:"))
    age=(input("enter age:"))

    print("My name is:"+n)
    print("My address is:"+a)
    print("My mobile number is:"+m)
    print("My age is:" +age)
    
Ajoy()