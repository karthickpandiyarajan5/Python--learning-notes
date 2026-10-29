conditional statements
-----------------------
1) if condition syntax
            if (condition):
                print()


-----------------------------------------------------------------------------
write a program to check the person is eligilble for voting or not based on age


age=int(input("enter a age:"))
if age>=18:
    print("you are eliglible for vote")


op:
   enter a age: 19
you are eliglible for vote
------------------------------------------------------------------------------


if else statements  syntax
----------------------------

if(condition):
    statements of if
else:
    statements of else
------------------------------------------------------------------------


age=int(input("enter a age:"))
if age>=18:
    print("you are eliglible for vote")
else  :
   print(" not eligible")


OP:

   enter a age: 6
 not eligible
--------------------------------------------------------------------------


a=int(input("enter a number:"))
if a%2==0:
     print("even")
else:
     print("odd")

OP:
  enter a number: 2
even
--------------------------------------------




write a program voter are eliglbe 18 above only when india

age=int(input("enter a age:"))
country=input("enter ur country:")
if age>=18 and country=="india":
    print("you are eliglible for vote")

else:
    print("not eligible")
op:
enter a age: 19
enter ur country: INDia
INDia
INDia
not eligible

---------------------------------------------------------


#write a program a number is positive or not


a=float(input("enter a number:"))
if a>0:
    print("positive")
else:
    print("negative")
op:


enter a number: 2
positive

----------------------------------------------------------



contineous if else
if(cond1):
    statements os cond1
else:
    if(cond2):
        statements of cond2
    else:
        if(cond3):
            statements of cond3
    
        else:
            default statements
-------------------------------------------------------------------


if(cond1):
    statements of cond1
elif(cond2):
    statements of cond2
elif(cond3):
    statements of cond3
else:
    default statements
------------------------------------------------------------------

a=float(input("enter a number:"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
else:
    print("zero")

OP:

enter a number: 0
zero

----------------------------------------------------------------------


based on percentage display results
85 to 100 is distinction
60 to 84 is first calss
50 to 59 is second class
35 to 49 is pass
< 35 is fail

per=float(input("enter a mark:"))
if (per>=85 and per<=100):
    print ("distinction")
elif(per>=60 and per<=84):
    print ("first class")
elif(per>=50 and per<=59):
    print("second class")
elif(per>=35 and per<=49):
    print("pass")
elif(per<35):
    print("fail")
else:
    print("invaild")

OP:
   enter a mark: 98
distinction
-----------------------------------------------------------------
check the given inputs that they form which type of triangle
equilateral
isoscles
scalene



a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


OP:


Enter side 1:  55
Enter side 2:  5
Enter side 3:  55
Isosceles triangle
-------------------------------------------------------------------------
electricity bill calculator
scenerio : An electricity company charges its customers as follows:
first 100 units:$0.5 per unit
next 100 units (101-200):$0.75 per unit
above 200 units:$1 per unit



unit=int(input("enter a unit:"))
if unit<=100:
    print(unit*0.5)
elif unit>=100 and unit<=100:
    print(unit*0.75)
elif unit>=200:
    print(unit*1)

OP:
enter a unit: 237
237
----------------------------------------------------------------------------
unit=int(input("enter a unit:"))
if unit<=100:
    ta=unit*0.5
elif unit>100 and unit<=200:
    ta=(100*0.5)+((unit-100)*0.75)
elif unit>200:
    ta=(100*0.5)+(100*0.75)+((unit-200)*1)
print ("toatal amount:",ta)

op:

enter a unit: 237
toatal amount: 162.0
-------------------------------------------------------


Scenario: An online store offers discounts based on the purchase amount:

10% discount for purchases between $100 and $500

20% discount for purchases above $500

No discount for purchases below $100


if amount < 0:
    print("Invalid amount")
elif amount < 100:
    discount = 0
elif amount <= 500:
    discount = 10
else:
    discount = 20

if amount >= 0:
    discount_amount = (amount * discount) / 100
    final = amount - discount_amount

    print(f"Discount: {discount}%")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Amount: ${amount:.2f}")
    print(f"Final amount: ${final:.2f}")

op:
  Discount: 10%
Discount amount: $50.00
Amount: $500.00
Final amount: $450.00
--------------------------------------------------------------------
if the input is Red, display "Stop."

If the input is Yellow, display "Ready to move."

If the input is Green, display "Go."

For invalid input, display "Invalid color."
-----
c=input("enter a color:")
if c== "red":
    print("stop")
elif c== "green":
    print("go")
elif c== "yellow":
    print("ready to move")
else :
    print("invaild color")
op:
enter a color: red
stop

---------------------------------------------------------------------

Scenario: A school uses the following grading system:

Marks >= 90: Grade A

Marks >= 75 and < 90: Grade B

Marks >= 50 and < 75: Grade C

Marks < 50: Fail


Task: Write a program that accepts the student's marks and displays their grade.


marks=float(input("enter a mark:"))
if marks>=90:
    print("A")
elif marks>=75 and marks<90:
    print("B")
elif marks>=50 and marks<75:
    print("c")
elif marks>50:
    print("fail")
else :
    print("inavalid")

OP:
   enter a mark: 78
B
------------------------------------------------------------------------
Scenario: Write a program that takes an integer as input and checks:

Whether the number is odd or even

Whether the number is divisible by 5



num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


OP:

Enter a number:  7
Odd number
Not divisible by 5
-----------------------------------------------------------------------
Scenario: Write a program that checks the strength of a password based on these rules:

Length >= 8 characters: Strong

Length between 5 and 7 characters: Medium

Length < 5 characters: Weak


password = input("Enter your password: ")

length = len(password)

if length >= 8:
    print("Strong")
elif length >= 5:
    print("Medium")
else:
    print("Weak")


OP:
  Enter your password:  123435355353
Strong
----------------------------------------------------------------------------
Scenario: A bank approves loans based on these conditions:

Age should be between 21 and 60

Monthly income should be greater than or equal to $5000


Task: Write a program to check whether a person is eligible for the loan based on their age and monthly income.


age = int(input("Enter your age: "))
income = float(input("Enter monthly income: $"))

if age >= 21 and age <= 60 and income >= 5000:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

OP:
  Enter your age:  21
Enter monthly income: $ 5000
Eligible for loan
------------------------------------------------------------------
Scenario: A weather monitoring system alerts based on the temperature:

Below 0°C: "Freezing weather"

0°C to 20°C: "Cold weather"

21°C to 30°C: "Warm weather"

Above 30°C: "Hot weather"



temperature = float(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("Freezing weather")
elif temperature <= 20:
    print("Cold weather")
elif temperature <= 30:
    print("Warm weather")
else:
    print("Hot weather")

OP:
Enter temperature in Celsius:  20
Cold weather










