'''print("Hello world")
print(5*7-(2*6)/(3+4))
print(4*6-(3*4)/(6+3))'''



i=1
while (i<=5):
    j=1
    while j<=i:
        print(i, end='')
        j=j+1
    i=i+1
print()

n=5
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()