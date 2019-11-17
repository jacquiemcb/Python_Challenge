import os
import csv
import sys




Mybank = os.path.join("budget_data.csv")

with open(Mybank, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ",")

	csv_header = next(csvreader)

	months = 0
	Total_P_L = 0
	value = 0
	change = 0
	profits = []
	add_date = []


	first_row = next(csvreader)

	months += 1
	Total_P_L += int(first_row[1])
	value = int(first_row[1])
	
	

	for row in csvreader:
		add_date.append(row[0])

		

		change = int(row[1])-value
		profits.append(change)
		value = int(row[1])

		months += 1

		Total_P_L = Total_P_L + int(row[1])


#######################################
greatest_inc = max(profits)

count_inc = profits.index(greatest_inc)

date_inc = add_date[count_inc]
#######################################



#######################################
lowest_dec = min(profits)

count_dec = profits.index(lowest_dec)

date_dec = add_date[count_dec]
#######################################

avg = sum(profits)/len(profits)


print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(months)}")
print(f"Total: ${str(Total_P_L)}")
print(f"Average Change: ${str(round(avg))}")
print(f"Greatest Increase in Profits: {date_inc} (${str(greatest_inc)})")
print(f"Greatest Decrease in Profits: {date_dec} (${str(lowest_dec)})")


sys.stdout = open("Financial Analysis.txt", "w")
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(months)}")
print(f"Total: ${str(Total_P_L)}")
print(f"Average Change: ${str(round(avg))}")
print(f"Greatest Increase in Profits: {date_inc} (${str(greatest_inc)})")
print(f"Greatest Decrease in Profits: {date_dec} (${str(lowest_dec)})")
