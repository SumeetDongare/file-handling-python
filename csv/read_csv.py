import csv

# -------- Method 1: Using with open() --------
with open("employees.csv", "r") as file:
    reader = csv.reader(file)

    print("Reading using with open():")
    for row in reader:
        print(row)  # Each row is a list

# -------- Method 2: Manual open() --------
f = open("employees.csv", "r")
reader = csv.reader(f)

print("\nReading using manual open():")
for row in reader:
    print(row)

f.close()
