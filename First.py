print("Hello there!!")
a=10
b=20
print(a+b)
print('sum =',a+b)
sum1=a+b
print("sum is %d"%sum1)
c='rohit'
print(c)
print('My name is  %s'%c)
a=10
b='rat'
print("a is %d, b is %s"%(a,b))
c=10.0
print(c)
print('%f'%c)
print('%.02f'%c)
msg="hey there i'm rohit soni,i'm learning Pyhton"
print(len(msg))
#print(msg[48]) Index out of reach
print(msg[0:5]) # 0,1,2,3,4 (Upto five(5))
print(msg.upper())
print(msg.isupper())
print(msg.count('python'))
print(msg.count('Ronny'))
print(msg.find('Ronny')) # when Word is not find in the string
print('New_string',msg.replace('rohit soni','Ronny')) # first old then new word
print(msg)
x='Rohit '
y='Loves Tina'
print(x+y)
print(x+','+y)
print(dir(msg))
print(help(str))
print( "______________________________________________________________________________________________________")
# integer and float
num=3.16
num1=-3.0
print(type(3))
print(type(num1))
print(round(num))
print(abs(num1))
print(round(num,1))

# Boolean operator
print(3==2)
print(3!=2)
print(3>2)
print(3<=1)
print(num+num1)
q='100'
w='200'
print(q+w)
print(int(q)+float(w)) # type casting
print(w)
#_ --------------------------------------------_

Mylist=['hi','this','is']
Mylist.append("Rohit soni")
print(Mylist)
Mylist.insert(0,"Tina, ") # only insert a value didn't overwrite it
print(Mylist)
Mylist1=['and', 'i','love u']
"""Mylist.insert(5,Mylist1)"""
Mylist.append(Mylist1) # takes only one argument
#Mylist.extend(Mylist1) # extend in list indivisual
print(Mylist)
Mylist.remove('hi')
print(Mylist)
print(Mylist.pop()) # popped the last element of List
print(Mylist) # Rest of the  List
 #--------------------------------------------------------------

print(Mylist.reverse())
print(Mylist)
Mylist.sort() # sort according to the first latter's ascii value
print(Mylist)
L=['a','A']
L.sort()
print(L)
print(ord('A')) # for ascii value
Mylist2=[1,2,5,6,7,4,64,66,24,54]
Mylist2.sort(reverse=True)
print(Mylist2)
B=sorted(Mylist2) #  Sorted returns a List not alter it
print(max(Mylist2))
List=[1,2,3,4,5,6,7,8]
print(1 in List)
name='rohit soni'
print(name.capitalize())
print(name.lower())
print(name.upper())
