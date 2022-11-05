#program to create a file
'''f=open("t1.txt",'w')
f.write("Good Morning")
f.write("\n prateek singh")
f.close()'''

#practical 14.2
#program to check attributes of the file object
'''f=open("t2.txt",'w+')
print("Name of the file:",f.name)
print("Closed or not:",f.closed)
print("opening mode:",f.mode)
f.close()
print("closed or not:",f.closed)'''

#practical 14.3
#program to read an entire text file
'''f=open("t1.txt",'r')
print(f.read())
f.close()
f.open("t1.txt",'r')
print(f.read(4))'''

#practical 14.4
#program to demonstrate the use of readline function
'''f1=open("t1.txt","r")
print(f1.readline())
f1.close()
f1=open("t1.txt","r")
print(f1.readline())'''

#practical 14.5
#program to demonstrate use of tell() and seek() method
'''f=open("t3.txt","r+")
st=f.read(6)
print("Read string is:",st)
pos=f.tell()
print("current position of of file pointer:",pos)
st=f.read(6)
print("Read string is:",st)
pos=f.tell()
pos1=f.seek(0,0)
st=f.read(8)
print("Again read the string:",st)
f.close()'''

'''f=open('python.txt','w')
f.write('good morning\n zahid')
f.write('\nhello')
f.write('\nhow are you')
f.close()'''

'''f=open('py2.txt','w+')
print('name of the file',f.name)
print('closed or not',f.closed)
print('mode of the file',f.mode)
f.close()
print('closed or not',f.close())'''

'''f=open('python.txt','r')
print(f.read())
f.close()
f=open('python.txt','r')
print(f.read(4))'''

'''f=open('python.txt','r')
print(f.readline())
f.close()'''

f=open('python.txt','r+')
f.read(6)
#st=f.read(6)
print('read string is:',f.read(6))
pos=f.tell()
print('current position of file is:',pos)
#f.read(7)
f.read(7)
print('read string is:',f.read(7))
#print('read string is:',st)

pos=f.tell()
pos1=f.seek(4)
f.read(8)
#st=f.read(8)
print('reading the string is:',f.read(8))
#print('reading the string is:',st)

f.close()

