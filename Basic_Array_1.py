#List/ Array
myList=["apple", "Watermelon", "Pineapple", "Grave", "apple"]
print(myList)
myList=["apple", "Watermelon", "Pineapple", "Grave", "apple"]
print(len(myList))

print("List item can be any data")
List_1=["Grape", "Watermelon", "Berry"]
List_2=[1,2,5,9,0]
List_3=[True,False,True]
print("string=",List_1,"Integer=",List_2,"Boolean=",List_3)

myList=["apple", 1, "Pineapple", True, 0.2]
print("Type=",type(myList))

"""Acess lis item"""
print("access list item")
myList=["Black berry",2,True, "Jackfruits"]
print(myList[1])
print(myList[-2])

"""Range of Indexes"""
print("\nRange of Indexes")
myList=["jackfruits", "Pineapple", "Grape", "Guava", 1, True]
print(myList[2:5])
print(myList[:4])
print(myList[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "jackfruits" not in thislist:
    print("No, this have no jackfruits")

"""Change Item Value"""
print("Change Item Value")
myList=["Guava", "Pineapple", "berry"]
print(myList)
myList[1]="Orange"
print(myList,"Changed")

"""Ranged based change value"""
print("Ranged based change value")
myList=["Guava", "Pineapple", "berry",12,True]
myList[1:3]=["Aplle", "Coconut"]
print(myList)

"""Insert Items"""
print("Insert Items")
myList=["Guava", "Pineapple", "berry"]
myList.insert(2,"Mango")
print(myList)

"""Append Items"""
print("Append Items")
myList=["Guava", "Pineapple", "berry"]
myList.append("Mango")
print(myList)

"""Extend List"""
myList=["jackfruit", "Olive", "berry"]
Another_list=["Cococola", "speed", "Sprite"]
myList.extend(Another_list)
print(myList)

"""Remove  List"""
print("\nRemove item from list")
myList=["jackfruit", "Olive", "berry"]
myList.remove("Olive")
print(myList)

"""Remove Specified Index"""
myList = ["apple", "banana", "cherry"]
myList.pop(1)
print(myList)
"""If you do not specify the index, the pop() method removes the last item.
"""
myList = ["apple", "banana", "cherry"]
myList.pop()
print(myList)

myList = ["apple", "banana", "cherry"]
del myList

myList = ["apple", "banana", "cherry"]
myList.clear()
print(myList)

"""Loop Lists"""
print("\nLoop list")
myList=["Ginger","Garlic","Onion", "Turmeric"]
for x in myList:
    print(x)
print("\nPrint all items by referring to their index number:")
myList=["Ginger","Garlic","Onion", "Turmeric"]
for i in range(len(myList)):
    print(myList[i])

print("\nPrint all items by referring using while loop :")
myList=["ginger", "apple","banana"]
i=0
while i<len(myList):
    print(thislist[i])
    i=i+1
print("A short hand for loop that will print all items in a list:")
myList=["ginger", "apple","banana"]
[print(x) for x in myList] #Shorthand loop
