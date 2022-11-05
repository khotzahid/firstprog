#program to check palindrome, sum of digit , recursive , and armstrong
def palindrome(num):
    sum=0
    temp=num
    while num!=0:
        rem=num%10
        sum=sum*10+rem
        num=num//10
        if temp==sum:
            print(temp,"is a palindrome number")
        else:
            print(temp,"is not a palindrome number")

def armstrong(num):
    sum=0
    temp=num
    while temp>0:
        rem=temp%10
        sum=sum+rem**3
        temp=temp//10
    if num==temp//10:
        print(num,"is an armstrong number")
    else:
        print(num,"is not an armstrong number")

def sum_of_digits(num):
    sum=0
    while num!=0:
        rem=num%10
        sum=sum+rem
        num=num//10
print("sum of digits of numbers=",sum)

def reverse(num):
    sum=0
    while num!=0:
        rem=num%10
        sum=sum*10
        num=num//10
print("reverse number=",sum)

while True:
    print("\n\n\t\t main menu")
    print("1. find number is palindrome ")
    print("2. find number is armstrong")
    print("3. find number sum of digits of a number")
    print("4. find reverse of a number")
    print("5. Exit")
    print("enter your choice(1_5):")
    choice=int(input())
    if choice>=1 and choice<5:
        n=int(input("enter any number:"))
    if choice==1:
        palindrome(n)
    elif choice==2:
        armstrong(n)
    elif choice==3:
        sum_of_digits(n)
    elif choice==4:
        reverse(n)
    else:
        print("program is terminated")
        break