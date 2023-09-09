# 5. Take a number from user and check the number is prime or not prime.

def isPrime(num):
    count=0
    for i in range(2,num):
        if num%i==0:
            count=1
    if count==0:
        print("Prime")
    else:
        print("not Prime")

myNumber=int(input("enter a Number to check isPrime:"))
isPrime(myNumber)