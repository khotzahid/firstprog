#practical_no_13
# program to concatenate following dictionaries to create a new dictionary
'''dict1={1:10,2:20}
dict2={3:30,4:40,5:50}
dict3={}
dict4={}
dict3.update(dict1)
dict3.update(dict2)
dict4={**dict1,**dict2}
print(dict1)
print(dict2)
print(dict3)
print("Dictionary 4")
print(dict4)

dic1={1:'Jasbir',2:'kiran'}
dic2={3:30,4:40,5:50}
dic3={}
for d in (dic1,dic2):
    dic3.update(d)
print("The concatenated dictionary is:")
print(dic3)

#practical_no_13.2
#write a program to merge two dictionaries using function
def merge(dict1,dict2):
    res={**dict1,**dict2}
    return res
dict1={'a':10,'b':6}
dict2={'d':6,'c':4}
dict3=merge(dict1,dict2)
print(dict3)'''

#practical_no_13.3
'''dict1={1:10,2:20,3:30,4:40,5:50}
print(dict1)
s=sum(dict1.values())
print("sum=",s)
def returnsum (mydict):
    sum=0
    for i in mydict:
        sum=sum+mydict[i]
    returnsum
dict={"k1":20,"k2":7,"k3":90,"k4":12}
print("sum",returnsum(dict))'''

#practical_no_13.4
#program to sort a dictionary by value/key

'''import operator
dict1={1:22,3:13,4:8,2:11,0:27}
print(dict1)
t=sorted(dict1.items(),key=operator.itemgetter(0))
print("In ascending order by key",t)
t=sorted(dict1.items(),reverse=True)
print("IN descending order by key:",t)'''



'''dict1={1:10,2:20,3:30}
dict2={4:40,5:50,6:60}
dict3={}
dict4={}
dict3.update(dict1)
dict3.update(dict2)
dict4={**dict1,**dict2}
print(dict1)
print(dict2)
print(dict3)
print("dictionary 4")
print(dict4)'''

'''dict1={1:10,2:20,3:30}
dict2={4:40,5:50,6:60}
dict3={}
for d in(dict1,dict2):
    dict3.update(d)
print('the concatenated dictionary is')
print(dict3)'''

'''def merge(dict1,dict2):
    res={**dict1,**dict2}
    return res
dict1={1:10,2:20,3:30}
dict2={4:40,5:50,6:60}
dict3=merge(dict1,dict2)
print(dict3)'''


'''d={1:10,2:20,3:30}
sum=0
for i in d.values():
    sum=sum+i
print(sum)'''

'''dict1={1:10,2:20,3:30,4:40,5:50,6:60}
print(dict1)
s=sum(dict1.keys())
print('sum=',s)'''
import operator
dict1={2:30,5:10,3:40,4:30,1:20}
print(dict1)
t=sorted(dict1.items(),key=operator.itemgetter(0))
print('in ascd order by key:',t)
t=sorted(dict1.items(),reverse=True)
print('in desc order by key:',t)
t=sorted(dict1.items(),key=operator.itemgetter(1))
print('in asc order by value',t)
t=sorted(dict1.items(),reverse=True)
print('in desc order by value',t)