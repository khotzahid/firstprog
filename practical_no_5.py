#write a program to check whether the input number is palindrome or not
'''number = int(input("Enter any number:"))
sum = 0
temp = number
while number!=0:
    res = number%10
    sum = sum*10+res
    number = number//10
if temp == sum:
    print(temp,"is a palindrome number")
else:
    print(temp,"is not a palindrome number")'''


'''num=int(input("enter number:"))
x=num
rev=0
while(num>0):
    rev=rev*10+num%10
    num=num//10
if(x==rev):
    print("number is palindrome")
else:
    print("number is not palindrome")'''

i= int(input('enter any number:'))
x=i
rev=0
while(i>0):
    rev=(rev*10)+i%10
    i=i//10
if(x==rev):
    print('no is palindrome')
else:
    print('no is not palindrome')