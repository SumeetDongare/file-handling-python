# Program: Write CSV using writer.writerow() (one row at a time)
# Method: Using both 'with open()' and manual open()

import csv

# -------- Using with open() (recommended) --------
with open("employees.csv", "w", newline='') as file:
    writer = csv.writer(file)

    # Writing rows one by one
    writer.writerow(["Names", "Age", "City"])
    writer.writerow(["John", 12, "Pune"])
    writer.writerow(["Om", 78, "Mumbai"])

# -------- Manual open() and close() --------
f = open("employees_manual.csv", "w", newline='')
writer = csv.writer(f)

writer.writerow(["Names", "Age", "City"])
writer.writerow(["John", 12, "Pune"])
writer.writerow(["Om", 78, "Mumbai"])

f.close()
