age = input("Youre age: ")
age = int(age)
if age < 3:
    print("免费")
elif age >= 3 and age < 12:
    print("10$")
else:
    print('12$')
