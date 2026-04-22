# -------- Method 1: Using with open() --------
with open("myfile.txt", "a") as file:
    file.write("\nThis is appended line 1")
    file.write("\nThis is appended line 2")

# -------- Method 2: Manual open() --------
f = open("myfile_manual.txt", "a")

f.write("\nThis is appended line 1")
f.write("\nThis is appended line 2")

f.close()
