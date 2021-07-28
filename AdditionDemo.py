import random

vowels=['a','e','i','o','u']
finalstr=""
exist=1
for i in range(1,10):
    alphabet=chr(random.randint(98,122))
    print(alphabet,end=" ")
    if alphabet in vowels and (exist==1 or i==1):
        exist=2
        finalstr+= alphabet
        
    if alphabet in vowels and exist==2:
        continue
    finalstr+= alphabet
print("Exist : ", exist)
if exist==1:
    finalstr+= 'a'

    #finalstr+= alphabet if exist else ""
    #if not exist: finalstr+=
print()
print("Final String is : ", finalstr.title())




"""
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
sum=n1+n2
print("Sum value is : ", sum)


l1=[10,20,30,40,50,60,70,80,90,100]
l2=[]
print(l1)

i=2
while i < len(l1):
    l2.append(l1[i])
    i+=3
print(l2)
for j in l2:
    l1.remove(j)
print(l1)
"""




    
    

