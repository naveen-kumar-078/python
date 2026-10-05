thisdict = {
    "car":"tata",
    "model":2004,
    "colour":"blue",
    
}

y= thisdict["model"]

print(y)

print("print key values-------------")
#There is also a method called get() that will give you the same result:
y = thisdict.get("model")
print(y)



#print only key in the dictionary

print("get keys----------------")

thisdict = {
    "car":"tata",
    "model":2004,
    "colour":"blue",
    
}
y = thisdict.keys()
print(y,"ended----it prints only key")


print("--------------")

# to add item in the dictionary
thisdict = {
    "car":"tata",
    "model":2004,
    "colour":"blue",
    
}

x = thisdict.keys()
print(x)

thisdict["engine"]="petrol"

print(x)

print("-----------------")




# to get values


x = thisdict.values()
print(x)

thisdict["engine"]="diesl"
print(x)

print("---------------")


# The items() method will return each item in a dictionary, as tuples in a list.

x = thisdict.items()
print(x)






clas = {
    "name":"arun",
    "age":21,
    "course":"mca"
}


print(clas["age"])


mobile = {
    "brand":"samsung",
    "model":"s24",
    "price":50000
}

mobile["price"]=60000

print(mobile)





clas = {
    "name":"arun",
    "age":21,

}

clas["course"]="mca"
clas["college"] = "stc"
print(clas)