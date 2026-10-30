
n = int(input("Enter number of subjects: "))
marks = []

for i in range(n):
    m = int(input("Enter marks: "))
    if m < 0 or m > 100:
        print("Invalid marks")
        exit()
    marks.append(m)

failed = []

for i in range(n):
    if marks[i] < 40:
        failed.append(i)

if len(failed) == 1:
    i = failed[0]
    shortage = 40 - marks[i]

    if shortage <= 5:
        marks[i] += shortage
        print("Grace marks awarded:", shortage)

print("Final marks:", marks)

if any(m < 40 for m in marks):
    print("Result: FAIL")
else:
    average = sum(marks) / n
    print("Average:", round(average, 2))

    if average >= 75:
        print("DISTINCTION")
    elif average >= 60:
        print("FIRST CLASS")
    elif average >= 50:
        print("SECOND CLASS")
    else:
        print("PASS")
      
