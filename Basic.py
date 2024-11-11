#Pyhton Basic
print  ("Hello h world");

import sys
print(sys.version);

#If condition
if 5>2:
    print("Five is grater than two")
if 1<2:
    print("1 is less than 2")


# Variable declaration
x=5
y="Hello world"
print(x,y)

x=5
y="Halim"
z=3.1416 

print(f"{x} is type of {type(x)}")
print(f"{y} is type of {type(y)}")
print(f"{z} is type of {type(z)}")

# Multiple Variables

x,y,z='apple','banana','mango'
print(x)

x=y=z="Mangos"
print(x,y,z)

fruits=["apple", "Orange","Lemon"]
x,y,z=fruits

print(f"{fruits} is {type(fruits)}")
print(x)
print(y)
print(z)

# Output Variable
x="Python"
y="is"
z="awesome"
print(x + y + z)

#Global Variable

x="Awesome"
def MyFunc():
    print("Python is " +x)
MyFunc()

#Global and Local Variable

x="Awesome"
def MyFunc():
    x="Fantastic"
    print("Pyhton is "+x)
MyFunc()
print("Python is "+x)

#Use Global Keyowrd
x="Awesome"
def MyFunc():
    global x
    x="Fantastic"
MyFunc()
print("Man is "+x)

#Number

x=1 #int
y=2.1 # float
z=5j #complex

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Convert Complex number to another number
x=1
y=1.21
z=5j

a=complex(x)
print(a)

b=int(y)
print(b)

c=float(x)
print(c)

#Random number
import random
print (random.randrange(1,10))

#Python Casting

a=int(1.0)
print(f"Convert float to integer {a}")

a=float(3)
print(f"Convert int to float {a}")

a=str(3)
b=int("4")
print(f"convert int to str {a} and string to int {b}")

#Multiple string

a="""Bangladesh is a land of river,
almost every year flood visit our country,
so we need carefull."""
print(a)

#string is array
a="Hello, World!"
print(a[1])

#Loop in string
for x in "banana":
    print(x)

#String Length
x="Hello World"
print(len(a))

#Check Word from String
a="The best things life is free"
print("free" in a)

txt="I go to stranger and take their potraits"
if "take" in txt:
    print("Take is in here")

txt="You and i were made for the same purpus"
if "expensive" not in txt:
    print("No, oxpensive not in present")

#Slice string
a="Hello world"
print(a[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

#Modify string
a="    Hello world"
b=a.upper()
print(b)
print(a.lower())
#Remove white space
print(a.strip())
#Replace
c=a.replace("H", "J")
print(c)
#Split String
d=a.split(",")
print(d)

#String Concatenation
a="Hello"
b="world"
c=a+" "+ b
print(c)

#Escape Charater
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#python Boolean
a=10
b=11

if b>a:
    print("B is grater than a")
else:
    print("B is not grater than a")

print(bool("Hello"))
print(bool(15))

print(bool(a))
print(bool(b))

def myFunc():
    return True
if myFunc():
    print("Yes")
else:
    print("No")
