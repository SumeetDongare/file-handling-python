import csv

# -------- Method 1: Using with open() --------
with open("employees.csv", "a", newline='') as file:
    writer = csv.writer(file)

    # Adding new rows
    writer.writerow(["Rahul", 35, "Delhi"])
    writer.writerow(["Sneha", 28, "Mumbai"])

# -------- Method 2: Manual open() --------
f = open("employees_manual.csv", "a", newline='')
writer = csv.writer(f)

writer.writerow(["Rahul", 35, "Delhi"])
writer.writerow(["Sneha", 28, "Mumbai"])

f.close()
