import csv

data = [
    ["Names", "Age", "City"],
    ["John", 12, "Pune"],
    ["Om", 78, "Mumbai"]
]

# -------- Using with open() --------
with open("employees.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)  # writes all rows at once

# -------- Manual open() --------
f = open("employees_manual.csv", "w", newline='')
writer = csv.writer(f)
writer.writerows(data)

f.close()
