# Write CSV using manual open() and close()
import csv
f = open("employees.csv", "w", newline='')
writer = csv.writer(f)
# Header + data rows
writer.writerows([
    ["Names", "Age", "City"],
    ["John", 12, "Pune"],
    ["Om", 78, "Mumbai"]
])
f.close()
print("File written successfully")
