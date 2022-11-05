#program to reverse a user input number using function
def reverse (num):
    sum=0
    while num!= 0:
        rem = num%10
        sum = sum*10+rem
        num = num//10
    return sum
num = int(input("Enter any integer value:"))
s=reverse(num)
print("reverse number=",s)