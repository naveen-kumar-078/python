coins  =  int(input(2))
total_rupees = 0
for coin in range (1,coins+1):
    total_rupees+=coin**2
print(total_rupees)