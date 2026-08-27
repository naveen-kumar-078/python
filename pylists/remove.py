# to remove specified value

thelist = ["apple","orange","bannana","pineapple"]
thelist.remove("apple")
print(thelist)


# to remove specified using index
thelist = ["apple","orange","bannana","pineapple"]
thelist.pop(3)
print(thelist)


#del function as same as pop

thelist = ["apple","orange","bannana","pineapple"]
del thelist[2]
print(thelist)


#clear method is used to delete the content but the list still remains

thelist = ["apple","orange","bannana","pineapple"]
thelist.clear()
print(thelist)

