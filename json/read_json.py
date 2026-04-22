import json

# -------- Method 1: Using with open() --------
with open("students.json", "r") as file:
    data = json.load(file)

    print("Reading using with open():")
    print(data)

# -------- Method 2: Manual open() --------
f = open("students.json", "r")
data_manual = json.load(f)

print("\nReading using manual open():")
print(data_manual)

f.close()
