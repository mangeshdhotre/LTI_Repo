# Given no is prime or not
num = int(input("Enter Number : "))
prime=True
for i in range(2,num):
   if(num%i==0):
       prime=False
       break
if prime:
    print("This number is prime")
else:
    print("This number is not prime")
