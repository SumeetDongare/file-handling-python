# Write multiple rows into CSV using writer.writerows()
import csv

with open("employees.csv","w",newline="") as f:
    writer = csv.writer(f)
# Header + data rows
    writer.writerows([
        ["Names","Age","City"],
        ["John",12,"Pune"],
        ["Om",78,"Mumbai"]
    ])
