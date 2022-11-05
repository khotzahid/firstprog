#program to find sum of digits of user input number
'''number= int(input("Enter any positive integer value:"))
sum = 0
while number!= 0:
    rem = number%10
    sum= sum+rem
    number= number//10
print("sum of digits of number =",sum)'''

'''no=int(input("enter number:"))
sum=0
while(no>0):
    sum=sum+no%10
    no=no//10
print("sod=",sum)'''

i=int(input('enter number:'))
sum=0
while(i>0):
    sum=sum+i%10
    i=i//10
print('sum of the number is',sum)
