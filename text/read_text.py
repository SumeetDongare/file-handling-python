# -------- Method 1: Using with open() --------
with open("myfile.txt", "r") as file:
    data = file.read()

    print("Using with open():")
    print(data)

# -------- Method 2: Manual open() --------
f = open("myfile.txt", "r")
data_manual = f.read()

print("\nUsing manual open():")
print(data_manual)

f.close()
