n = int(input("enter the number:"))

if n%2==0 and n>0:
    print("postive")
else:
    print("neagtive")



a = int(input("enter the driver age: "))
has_license = input("driver license (true/false): " )

if a>=18 or a>18 and has_license==True:
    print("yes approved")
else:
    print("not approved")