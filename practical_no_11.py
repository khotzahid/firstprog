#practical no 11.1
'''st="vedshree"
print(st)
print("st.find('e')",st.find('e'))
print("st.find('e',4)",st.find('e',7))
print("st.find('e',2,4)",st.find('e',2,4))'''


#practical no 11.2
'''def find(st,a):
    i=0
    while i<len(st):
        if st[i]==a:
            return i
        i=i+1
    return -1
pos=find("tushar",'s')
if pos!=-1:
    print("character is present at index:",str(pos))
else:
    print("character is not present in the string")'''

#practical no 11.3
'''t="TUSHAR SAMBARE"
n=0
for i in t:
    if i=='A':
        n=n+1
print(n)'''

#practical no 11.4
'''st1="madam"
st2=st1[:: -1]
if st1==st2:
    print("string is palindrome")
else:
    print("string is not palindrome")'''

'''st='khot zahid'
print(st)
print('st.find("a") ',st.find('a'))
print('st.find("z")',st.find('z'))
print('st.find("h",7)',st.find('h',7))'''

'''def find(st,a):
    i=0
    while i<len(st):
        if st[i]==a:
            return i
        i=i+1
    return -1
pos=find('tushar','e')
if pos!=-1:
    print('character is present at index',str(pos))
else:
    print('character is not found at present string')'''

'''t='zahid khot aaahhh'
#c=t.count('h')
print(t.count('h'))'''

'''t='zahid khot'
n=0
for i in t:
    if i == 'h':
        n=n+1
    print(n)'''

st1='madam'
st2=st1[:: -1]
if st1==st2:
    print('string is palindrome')
else:
    print('string is not palindrome')