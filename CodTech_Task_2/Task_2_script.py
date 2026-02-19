import csv
import matplotlib.pyplot as plt

# Step 1: Read data from CSV file
months = []
sales = []

with open("CodTech_Task_2/data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        months.append(row[0])
        sales.append(int(row[1]))

# Step 2: Data analysis
total_sales = sum(sales)
average_sales = total_sales / len(sales)

# Step 3: Create visualization
plt.figure()
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

# Step 4: Save report as PDF
plt.savefig("CodTech_Task_2/Sales_Report.pdf")

print("Report generated successfully!")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)