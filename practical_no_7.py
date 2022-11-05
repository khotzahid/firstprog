#write a recursive function to print factorial of a given number
def fact(x):
    if x==1 or x==0 :
        return 1
    else :
        return(x* fact(x-1))

number = int(input("Enter any number:"))
print("the factorial of ",number,"is ",fact(number))