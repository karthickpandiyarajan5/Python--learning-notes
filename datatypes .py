datatypes
----------------------------------------------------
its represent kind of data.


 single value data type:
  int
  float
  bool
  complex
  str

 multi value data type:(inbuild data structure)
  list
  tuple
  set
  dict
  str

--------------------------------------------------
n=5
type(n)

op:

int


-----------------------------------------------------


operaters
----------------------------------------

its special symbol perform certaine operation
b/w two operands.

    add=n1+n2
    operands : n1,n2,add
    operaters:=,+


types of operaters

1)arithemetic operators
   + - * / % ** //
2)assignment operators:
= += -= *= %= /=  **=  //=
3)logical operators
  and or not
4)relational /conditional operaters
 ==  != >  <   >=  <=  
5) membership operaters
   in,not in 
6) identity operator
 is ,is not
7) bitwise operator
   &   |  ~  >>  << 




note:its used only in pandas mainly so it not mandatory to learn full ,basics is enough



#write a  program to calculate simple intrest and  total return value

p = int(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest (%): "))
t = float(input("Enter the time in years: "))

si = (p * r * t) / 100
total = p + si

print(f"Simple Interest: {si:.2f}")
print(f"Total Return Value: {total:.2f}")


op:

Enter the principal amount:  555
Enter the rate of interest (%):  5
Enter the time in years:  5
Simple Interest: 138.75
Total Return Value: 693.75
-------------------------------------------------------------


















