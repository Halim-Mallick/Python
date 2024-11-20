thisDict={
    "Name":"Halim",
    "Varsity":"DIU",
    "Batch":"E-89",
    "Roll":47
}
print(thisDict)
print(thisDict["Name"])
print(len(thisDict))

"""You can diferent data type in dictionary"""
print("\nYou can diferent data type in dictionary")
thisDict={
    "Name":["Halim","Foni","Mehedi","Rubel"],
    "Varsity":"DIU",
    "Batch":"E-89",
    "Roll":47
}
x=thisDict.get("Name")
y=thisDict.keys()
z=thisDict.values()
i=thisDict.items()
print(thisDict)
print("\nGet Mathod",x)
print("\nKey Mathod",y)
print("\nvalue Mathod",z)
print("\nitem Mathod",i)

thisDict["Age"]=26
print(thisDict)

"""Nested Dictionary"""
print("\nNested Dictionary")

myFamily={
    "Child1":{
        "name":"Kamal",
        "Age":29
    },
    "Child2":{
        "name":"amal",
        "Age":20
    },
    "Child3":{
        "name":"Kamal",
        "Age":29
    },
    "Child4":{
        "name":"Kamal",
        "Age":29
    }
}
print(myFamily)
