todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

work = input("해야할 일: ")
day = int(input("남은 일: "))

t = (work, day,)
todo.append(t)

print(todo)