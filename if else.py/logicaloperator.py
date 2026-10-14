age  = int(input("enter your age"))
college_memeber = False
discount_coupon = False

if(age < 16 or age > 60) and  not college_memeber or discount_coupon:
    print("discout applied")
else:
    print("not eligibe")

    # user authntication check

username = "elias"
pasword = "123"
is_verifed = True

if username and pasword and is_verifed:
    print("yes its succssfully verifies")
else:
    print("no")