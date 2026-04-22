import json
import csv

# -------- Method 1: Using with open() --------
with open("students.json", "r") as json_file:
    data = json.load(json_file)  
    # data = list of dictionaries

with open("students.csv", "w", newline='') as csv_file:
    headers = data[0].keys()  # extract column names

    writer = csv.DictWriter(csv_file, fieldnames=headers)

    writer.writeheader()      # write column names
    writer.writerows(data)    # write all rows

# -------- Method 2: Manual open() --------
json_file = open("students.json", "r")
data_manual = json.load(json_file)
json_file.close()

csv_file = open("students_manual.csv", "w", newline='')

headers = data_manual[0].keys()

writer = csv.DictWriter(csv_file, fieldnames=headers)

writer.writeheader()
writer.writerows(data_manual)

csv_file.close()
