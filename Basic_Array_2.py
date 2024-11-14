"""List Comprehension
"""
mylist=["apple","Mango", "Banana","Cherry","Jackfruits"]
newlist=[]
for x in mylist:
    if "a" in x:
        newlist.append(x)
print(newlist)

print("\nonly one line of code:")
mylist=["apple","Mango", "Banana","Cherry","Jackfruits"]
newlist=[x for x in mylist if "a" in x]
newlist1=[x.upper() for x in mylist if "a" in x]
print(newlist)
print(newlist1)

newlist=[x for x in range(10)]
print(newlist)
newlist=[x for x in range(10) if x<5]
print(newlist)

"""Sort list"""
print("\n Sort List")
mylist=["Banana", "Apple","another","Coconut", "Jackfruits"]
digit=[100,30,50,70,10]
digit.sort()
print(digit)
print(mylist)

"""Decending order list"""
print("\n Decending order List")
mylist=["Banana", "Apple","Coconut","another", "Jackfruits"]
digit=[100,30,50,70,10]
mylist.sort(reverse=True)
digit.sort(reverse=True)
print(digit)
print(mylist)
mylist.sort(key=str.lower)
print(mylist)

"""Copy a List"""
thisList=["Ginger","Turmeric","Greenchili","Onion"]
newlist=thisList.copy()
print(newlist)

"""Join a List"""
List_1=["Ginger","Turmeric","Greenchili","Onion"]
List_2=[2,5,7,12,9]
list_3=List_1+List_2
print(list_3)

print("\n Using For loop")
for x in List_2:
    List_1.append(x)
print(List_1)
