"Set Not Allowed Duplicate Member"
mySet={"Halim","Dalim","Robin", "dalim"}
print(mySet)
print(type(mySet))
print(len(mySet))

"""Loop in set"""
mySet={"Rissole","Vermicelli","Rice-Puddding", "Yogurt"}
for x in mySet:
    print(x)
print("Yogurt" in mySet)
print("Apple" not in mySet)

print("\nYou don't change item form Sets, But can add new item:")
mySet.add("Hotchpotch")
print(mySet)
"""To add items from another set into the current set, use the update() method."""
print("To add items from another set into the current set, use the update() method.")
newSet={"Jellyfish","Pilaf","Flatbread"}
mySet.update(newSet)
print(mySet)

"""Remove Item"""
newSet.remove("Jellyfish")
print(newSet)
newSet.discard("Pilaf")
print(newSet)

mySet={"Rissole","Vermicelli","Rice_pudding","Pilaf"}
mySet.pop()
x=mySet.pop()
print("\n",mySet)
print(x)

"Union"
print("\nUnion")
setA={1,2,4,6,8}
setB={"Apple", "Mango", "Banana"}
setC=setB.union(setA)
print(setC)
#Differen Mathod
setD=setA | setB
print(setD)

"""Intersection"""
print("\nIntersection")
setA={"Apple", "jackfruits","Banana"}
setB={"Apple", "Mango", "Banana"}
setC=setA.intersection(setB)
print(setC)
#Differen Mathod
setD=setA & setB
print(setD)

"""Difference"""
print("\nDifference")
setA={"Apple", "jackfruits","Banana"}
setB={"Apple", "Mango", "Banana"}
setC=setA.difference(setB)
print(setC)
#Differen Mathod
setD=setB-setA
print(setD)
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

'''Symmetric difference'''
print("Symmetric difference")
setA={1,3,4,5,6}
setB={1,10,7,0,6}
setC=setA.symmetric_difference(setB)
print(setC)
