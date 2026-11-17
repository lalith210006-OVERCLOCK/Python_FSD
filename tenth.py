age=int(input('Enter your age:'))
if age<0:
    print("Invalid Age")
elif age>=18:
    print("Your eligible for voting")
else:
    print("not eligible for voting")