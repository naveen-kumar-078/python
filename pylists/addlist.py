#o add an item to the end of the list, use the append() method:

thislisys = ["apple","orange","mango","orange"]
thislisys.append("pineapple")
print(thislisys)


# insert an item

thislisys = ["apple","orange","mango","orange"]
thislisys.insert(3, "pinabble")
print(thislisys)


# to add elemnsts from another list to current list

thislisys = ["apple","orange","mango","orange"]
veg = ["carrot","beetrooot","totmato"]
thislisys.extend(veg)
print(thislisys)






fruits = ["apple","orage","mago"]
fruits.append("bannna")
print(fruits)




fruits = ["apple","orage","mago"]
fruits.insert(2,"bannna")
print(fruits)


fruits = ["apple","orage","mago"]
veg = ["carrot","beetroot","tomato"]
fruits.extend(veg)
print(fruits)





#append

meat = ["chcken","fish","beef"]

meat.append("pork")
print(meat)

meat.insert(1,"mutton")
print(meat)



more_meats = ["crocodile","frog"]

more_meats.extend(meat)
print(more_meats)




  
cars = ["BMW", "Audi", "Benz"]
cars.append("toyota")
print( cars)
cars[1] = "toyota"
print(cars)


