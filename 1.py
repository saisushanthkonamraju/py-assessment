students = [("Anil", 78), ("Ravi", 45), ("Meena", 88), ("Sita", 62), ("Raj", 49)]
passcount = 0
failcount = 0
New = {}
for Name,Marks in students:
    if Marks>=50:
        New[Name] = "Pass"
        passcount+=1
    else:
        New[Name] = "Fail"
        failcount+=1

print(New)
print("Pass:",passcount)
print("Fail:",failcount)