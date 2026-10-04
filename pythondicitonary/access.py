thedict = {
    "name":"ravi",
    "age":21,
    "roll ":25,
    "year":"2026"

}

x = thedict["name"]
y= thedict.get("age")
z = thedict.keys()
print(x)
print(y)
print(z)

print("-------------------------------get keys-------------------------------------------------------------")


# to add items 

car = {
    "model":"fiat",
    "color":"blue",
    "year":2004
}

x = car.keys()
print(x)



print("--------------get values-----------")

car = {
    "model":"fiat",
    "color":"blue",
    "year":2004
}

x = car.values()
print(x)

car["type"]="ev"
print(x)
print("-------change the values-------------")

laptop = {
    "company":"dell",
    "ram":16
}

x = laptop.values()
print("before:",x)
laptop["ram"] = 32

print(x)


