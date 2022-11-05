#write a program to generate fibonacci series
'''Terms= int(input("Enter any Terms: "))
f1=0
f2=1
for i in range(0,Terms):
    if(i<=1):
     f3=i
    else:
        f3=f1+f2
        f1=f2
        f2=f3
        print(f3)'''

#write a program to generate fibonacci series
'''Terms=int(input("enter any terms:"))
f1=0
f2=1
for i in range(0,Terms):
    if(i<=1):
        f3=i
    else:
        f3=f1+f2
        f1=f2
        f2=f3
        print(f3)'''

'''no = int(input("enter number:"))
a=0
b=1
c=0
print(a)
print(b)
i=1
while i<no:
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)'''


'''no=int(input("enter fibo number:"))
a=0
b=1
c=0
print(a)
print(b)
i=1
while i<no:
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)'''

n =int(input('enter value of n:'))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
