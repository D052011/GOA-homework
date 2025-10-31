sum = 0

while True:
    num = int(input("შეიყვანე რიცხვი (0-ს შემთხვევაში შეწყდება): "))
    if num == 0:
        break
    sum += num

print("რიცხვების ჯამი არის:", sum)