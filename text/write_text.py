# -------- Method 1: Using with open() --------
with open("myfile.txt", "w") as file:
    file.write("Hello Students\n")
    file.write("Welcome to Python File Handling")

# -------- Method 2: Manual open() --------
f = open("myfile_manual.txt", "w")

f.write("Hello Students\n")
f.write("Welcome to Python File Handling")

f.close()  # Important to save and close file
