def myFunction(fname):
    print(fname,"Mallick")

myFunction("Halim ")
myFunction("Dalim ")
myFunction("Arafat")

print("\nIf the number of arguments is unknown, add a * before the parameter name:")
def myFunction2(*brothers):
    print("Your Younger Brother is",brothers) #You can add here index [1]
myFunction2("Halim","Dalim","Arafat")

def myFunction3(food):
    for x in food:
        print(x)
fruits=["Apple","Banana","cherry"]
myFunction3(fruits)

"""Tri-Recursion function"""
print("\nTri-Recursion function")
def tri_recursion(k):
    if (k>0):
       result=k+tri_recursion(k-1)
       print(result)
    else:
       result=0
    return result
print("Recursion Example Result: ")
tri_recursion(6)
