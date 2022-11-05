global s
global n
s=[12,16,20,40,50,70,80,90]
data=26
n=6
def LinearSearch():
    print(s)
    for i in range(n):
        if(s[i]== data):
            print("element found at position:"+str(i+1))
            break

#program for inserting an element at the end of array
def insert(element):
    global s
    global n
    print("before inserting ")
    print(s)
    s[6]=element
    print("after inserting")
    print(s)
    print(n+1)
    n=n+1

#program for inserting an element at particular position in array
def insertAtk(element,k):
    global s
    global n
    print("before inserting ")
    print(s)
    for i in range(n,k-1,-1):
        s[i+1]=s[i]
    s[k]=element
    n=n+1
    print("after inserting:")
    print(s)
    print(n)

print("\n MAIN MENU")
print("1. insert new element")
print("2. insert new element at kth position")
print("3.linear search")
choice= int(input("enter the choice:"))
while True:
    if choice==1:
        insert(30)
    elif choice==2:
        insertAtk(data,3)
    elif choice==3:
        LinearSearch()
    elif choice==4:
        break