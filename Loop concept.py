Loop concept:

a loop is a programming concept used to execute
a block of code repeatedly until certaine condition is met 
or the sequence is completed

types of python
* for loop
1) for loop with sequence
2) for loop with range
*while loop
*nested loop
1)for loop inside for loop
2)for loop inside while loop
3)while loop inside while loop
4)while loop inside for loop
-------------------------------------------------------------------------



for loop with sequence syntax

for ittirative variable(it doesn't hold a constant variable,changing every excution) in sequence_variable:
 statements 


name="karthick"
for char in name:
    print(name)


op:


 karthick
karthick
karthick
karthick
karthick
karthick
karthick
Karthick
----------------------------------------------------------------------------------------


pos=0 and char='p'



name="karthick"
pos=0
for i in name:
    print(f"position:{pos},character:{i}")
    pos=pos+1


op:


position:0,character:k
position:1,character:a
position:2,character:r
position:3,character:t
position:4,character:h
position:5,character:i
position:6,character:c
position:7,character:k
--------------------------------------------------------------------------------------

name="karthick"
for i in enumerate(name):
    print(i)
    print(f"postion:{i[0]},charcter:{i[1]}")

op:


 (0, 'k')
postion:0,charcter:k
(1, 'a')
postion:1,charcter:a
(2, 'r')
postion:2,charcter:r
(3, 't')
postion:3,charcter:t
(4, 'h')
postion:4,charcter:h
(5, 'i')
postion:5,charcter:i
(6, 'c')
postion:6,charcter:c
(7, 'k')
postion:7,charcter:k
-----------------------------------------------------------------------
l1=['priya','karthick','jeeva','mani','kishore']
pos=0
for i in l1 :
    print(f"happy diwali {i} have a bright life")




op:
happy diwali priya have a bright life
happy diwali karthick have a bright life
happy diwali jeeva have a bright life
happy diwali mani have a bright life
happy diwali kishore have a bright life


--------------------------------------------------------------------














