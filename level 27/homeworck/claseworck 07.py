students = []
for i in range(3):
    name = input(f"შეიტანეთ სტუდენტის სახელი #{i+1}: ")
    students.append(name)
students.insert(0, "Teacher")
students.pop()
print("სიის სიგრძე:", len(students))
print("საბოლოო სია:", students)
