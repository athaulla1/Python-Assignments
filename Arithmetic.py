
#a=True
#b=True
#a=10.2
#b=5.5

#this program demos Arithmetic Operations and this wll be in Repository

a= int(input("Enter first number :"))
b= int(input("Enter second number :"))
print(a,b)
sum=a+b
print("Addition : ", sum)
print("Subtraction : ", a-b)
print("Multiplication : ", a*b)
#a=5,b=2, a=5,b=0
#if b == 0:  # 
#if b == False:
#if not b==0: #
#bool(0) ===False
if b:   # python way of writing program  # if bool(b) #we can use integer
    print("if Division : ", a/b)
    print("if Floor value : ", a//b)   
    print("if Modulus/Reminder : ", a%b)
else:
    print("else Division : ", 0)
    print("else Floor value : ",0)
    print("else Modulus/Reminder : ", 0)

    
pow=a**b
print("Power value : ", pow)

#print("sqrt of addition value : ", sum**0.5)

"""
Input --> Process --> Output
10,10  --> addition --> 20
Temp storage, Permanent Storage (DB, FileHandling)

Memory Allocation....10,10

s="Aheena "   #A-65, a=97, 
s1="aheena"

if s>s1:
    print ("Greater")
else:
    print("LEsser")
"""
