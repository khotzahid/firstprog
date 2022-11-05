#write a program to check whether a input number is armstrong or not
'''number = int(input(" Enter any number:"))
sum=0
temp=number
while temp > 0 :
    res = temp%10
    sum = sum+res**3
    temp = temp//10
if number == sum:
    print(number,"is an armstrong number")
else :
    print(number,"is not an armstrong number")'''

number=int(input('enter any number:'))
orig=number
sum=0
while(number>0):
    sum=sum+(number%10)*(number%10)*(number%10)
    number=number//10
if orig==sum:
    print("it is armstrong number")
else:
    print('it is not armstrong number')
