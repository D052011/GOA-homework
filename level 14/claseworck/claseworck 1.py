age = int(input("please enter your age: "))
experiense = int(input("please enter your experiense: "))
hight = int(input("please enter your higt: "))

isHired = age >= 18 and experiense >= 2 and hight >= 180

print("you are hired: " + str(isHired))
