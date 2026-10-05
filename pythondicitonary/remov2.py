#
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
print("using pop to remove")
print("----------------------")

#The popitem() method removes the last inserted item
#
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.popitem()
print(thisdict)
print("popitem")
print("-------------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del thisdict["year"]
print(thisdict)
print("del also used to delete the key and values")
print("----------------")




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#thisdict.clear()
print(thisdict)

print("clear  used to delete all")
print("----------------")







car= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("brand")
car.popitem()
del car["model"]
car.clear()
print(car)