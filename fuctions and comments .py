#output functions in python is print()
-------------------------------------------
-------------------------------------------
print ("good morning")
print('good morning')


output:
good morning
good morning



name="karthick"
age=22
#my age is karthick and my age is 22

print("my name is",name,"my age is",age)


output:
my name is karthick my age is 22




#.format functions()
--------------------

name="karthick"
age =22
print("my name is {} and my age is {}".format(name,age))

op:
my name is karthick and my age is 22



#fstring method
----------------
name="karthick"
age =22
print(f"my name is {name} and my age is {age}")

op:
my name is karthick and my age is 22

-------------------------------------------------------------------------------------------------------------------------------------------------------------

 comments
----------
they are the part of programming but they never partof execution.they used
to understand the flow of programming or some critical logics.


types of comments in python
 1) single line comments
 #its single line comment

 2) multiple comment
 '''its multiple commeny'''
 """its multiple comment"""

keywords:
-----------
they are the predefined words to perform a specific task.
         ex: if , for , else , break .....


these keywords are not used as identifiers.
    (variable,function name...)
  

example:

import keyword
print(keyword.kwlist)


op:

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


----------------------------------------------------------------------------------------------------------------------------------------------------
example:


#write a program for addition odf 2 nums
ex:the sum of 5 and 2 is 7


v1=int(input ("enter a value :"))
v2=int(input("enter a value:"))
v3=v1+v2
v3


op:
enter a value : 5
enter a value: 2
7



--------------------------------------------------------------------------------------------------------------------------------------------------

#write a program to calculate area of circle and area triangle

area of circle :0.5r*r
area of triangle:1/2*b*h



r=float(input("enter a radius value:"))
aoc=math.pi*r*r
print ("the area of circle:",aoc)
b=float(input("enter a base value:"))
h=float(input("enter a hight value:"))
aot=0.5*b*h
print(f"the area of triangle is {aot:.4f}")


stu_name=input("stu name:")
stu_id=(input("stu id:"))
s1=int(input("s1:"))
s2=int(input("s2:"))
s3=int(input("s3:"))
total=s1+s2+s3
print("total:",total)
print("per:",(total/300)*100)


print(f"{"*"*10}student details{"*"*10}")
print(f"studentname:{stu_name}\nstudentid:{stu_id}\ns1:{s1}\ns2:{s2}\ns3:{s3}\ntoatal:{total}")
print(f"{"*"*10}all the best{"*"*10}")

op:

**********student details**********
studentname:k
studentid:911
s1:90
s2:89
s3:78
toatal:257
**********all the best**********
              
