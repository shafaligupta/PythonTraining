#Q1.
print("Hello My name is \"Shafali\". I love Coding")
print("This is 'my first program'")

x = int(input("Enter first number"))
y = int(input("Enter second number"))
z = int(input("Enter third number"))

#print("User Entered x=",x ,',',"y=",y,',',"z=", z)
print("User Entered x={}, y={}, z={}".format(x,y,z))
print("\"Value1={},Value2={}, Value3={}\"".format(x,y,z))

print(type(x))
print(type(y))
print(type(z))

#Q2

print("Hello! My name is XYZ\n\"Hello I am a candidate\" \n \"234.56\" \n\"34\"\n a+3j")

#Q3.

x=10+20*(45+67.0)
print(x)
print(type(x))

x=(True and False) or False
print(x)
print(type(x))

x=(True and True) and (not False and True)
print(x)
print(type(x))

x=(3>89) or(34>32)
print(x)
print(type(x))

x = not True and False
print(x)
print(type(x))

#Q4.
x = int(input("enter the number"))
if((x%2)==0 or (x%5)==0):
    print("\"Hurray it is what i am looking for")
else:
    print("Wrong input")

#Q5.
x= int(input("enter the number"))
if (10<x<50):
    print("\"Yes I am in the range\"")
else:
    print("Oops")






