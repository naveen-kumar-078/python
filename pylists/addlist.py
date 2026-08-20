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