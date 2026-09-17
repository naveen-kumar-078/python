student = ("Arun", 21, "MCA", 85, 78, 92)
print("student name:",student[0])
print("student course:",student[2])
print("student marks:",student[3:])
print("student higest mark:",max(student[3:]))
print("student lowest mark:",min(student[3:]))
print("student avearge:",sum(student[3:])/len(student[3:]))

y = list(student)
y[3] = 98
print(y)

student = tuple(y)
print(student)



#2. Product Details System 🛒

product = ("Laptop", 55000, "Dell", "16GB RAM", "512GB SSD")
print("product name and price: ",product[0:2])
print("ram and price",product[3],"and",product[1])
y = list(product)
y.append("nvdia 3050")

product = tuple(y)
print("add new specification:",product)

print("------------------------------------------------")


#4. Shopping Cart
item1 = ("Keyboard", 800, 2)
item2 = ("Mouse", 500, 1)
item3 = ("Headset", 1500, 1)
#-----------------------------------------------------#

#individual cost

cost1 = item1[1] * item1[2] 
cost2= item2[1] * item2[2] 
cost3 = item3[1] *item3[2] 

print("keyboard",cost1)
print("mouse",cost2)
print("headset",cost3)


total_bill =  cost1+cost2+cost3
print("total bill",total_bill)

#most expensive
print("mostexpensive",item3[1])

#update the quantity of keyboard 
y = list(item1)
y[2] = 5

item1 = tuple(y)
print("quantity updated",item1)




print("---------------------------------------- next tuple practise")



#Movie Information 🎬

movie = ("Leo", "Action", 2023, 7.8)
print("movie",movie[0])
print("genre",movie[1])

#Find an Item
languages = ("Python", "Java", "C++", "JavaScript")
print("Python" in languages)
print("html" in languages)


# Shopping Cart

cart = ("Laptop", "Mouse", "Keyboard", "USB Cable")

print("number of products.:",len(cart))
print("whether Mouse exists.:","Mouse" in cart)
print(cart.index("Keyboard"))
print(cart.count("Mouse"))
