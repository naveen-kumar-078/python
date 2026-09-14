# we can chnage the tuple 

mytuple = ("apple","orange","mango")
y = list(mytuple)
print(y)

y[2] ="grapes"
print(y)

x = tuple(y)
print(x)

# we can add items using tuples
mytuple = ("apple","orange","mango")
y = list(mytuple)
y.append("tomato")
print(y)

mytuple = tuple(y)
print(mytuple)