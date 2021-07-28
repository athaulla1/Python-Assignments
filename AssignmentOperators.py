a="Annanagar"
b="Annanagar"
print("Equal : ", a==b)
print("Not Equal : ", a!=b)
print("Greater: ", a>b)
print("Greater and Equal : ", a>=b)
print("Less than : ", a<b)
print("Less than and Equal: ", a<=b)
print(10<20<30<40)
print(10>20>30<40)
print(10>20>30>40)
print(10<20<30>40)
print(10<20<30>40)

x=10
y=2
x *= y
print(x)
x+=y
print(x)
x-=y
print(x)

x //= y
print(x)
x %= y
print(x)
x /= y
print(x)


a,b,c=10,20,30
m=a if a<b else b if b<c else c
print(m)
a,b,c=20,10,30
m=a if a<b else b if b<c else c
print(m)

a,b,c=30,20,10
m=a if a<b else b if b<c else c
print(m)

a,b,c=20,30,10
m=a if a<b else b if b<c else c
print(m)

a,b,c=10,20,30
m=a if a<b and a<c else b if b<c else c
print(m)


a,b,c=20,10,30
m=a if a<b and a<c else b if b<c else c
print(m)



a,b,c=30,20,10
m=a if a<b and a<c else b if b<c else c
print(m)


a,b,c=20,30,10
m=a if a>b and a>c else b if b>c else c
print(m)
