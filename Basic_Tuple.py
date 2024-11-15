thistuple=("apple",)
print(type(thistuple))

thistuple=("apple")
print(type(thistuple))

"""Convert the tuple into a list and replce item"""
thisTuple=("Ginger", "Garlic", "Bayleaf")
thisList=list(thisTuple)
thisList[1]="Kiwi"
thisTuple=tuple(thisList)
print(thisTuple)

"""Add item in touple"""
x=("A","B","c")
y=list(x)
y.append("D")
x=tuple(y)
print(x)

"""Unpack Tuple"""
thistuple=("Apple","Banana","Cherry")
green,yellow,red=thistuple
print(green)
print(yellow)
print(red,"\n")

"""Assign the rest of the values as a list called "red":"""
thistuple=("Apple","Banana","Cherry","Strawberry","Rasberry")
green,yellow,*red=thistuple
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print("\n",x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
