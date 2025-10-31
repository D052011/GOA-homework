name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
experience = int(input("შეიყვანეთ გამოცდილება წლებში: "))

if age > 22 and experience > 2:
    print("Hired")
elif age > 25 and experience > 1:
    print("Hired")
elif age > 20 and experience > 3:
    print("Hired")
elif name == "გურამ":
    print("Hired")
else:
    print("Not hired")