# Import needed libraries: pathlib, csv
import pathlib
import csv
import statistics

# Store the path to budget_data.csv
budget_data_location = pathlib.Path("Resources/budget_data.csv")

# Create variables to store the columns
date = []
profit_losses = []

# Open budget_data.csv as read only
with open(file=budget_data_location, mode="r") as budget_data_csv:
    budget_data_reader = csv.reader(budget_data_csv, delimiter=",")
    
    # Read in the header to exclude it from variable data
    budget_data_header = next(budget_data_reader)
    
    # Read column data into variables
    for row in budget_data_reader:
       date.append(row[0])
       profit_losses.append(int(row[1]))

changes = []

for i in range((len(profit_losses)-1)):
    change = profit_losses[i+1] - profit_losses[i]
    changes.append(change)

# Find total months included in dataset
total_months = len(date)

# Find net total amount of "Profit/Losses" over the entire period
total = sum(profit_losses)

# Find the average of the changes in "Profit/Losses" over the entire period
average_change = round(statistics.mean(changes),2)

# Find the greatest increase in profits over the entire period
greatest_increase = max(changes)

# Find the month of the greatest increase in profits
greatest_increase_month_index = changes.index(greatest_increase) + 1
greatest_increase_month = date[greatest_increase_month_index]

# Find the greatest decrease in profits over the entire period
greatest_decrease = min(changes)

# Find the month of the greatest decrease
greatest_decrease_month_index = changes.index(greatest_decrease) + 1
greatest_decrease_month = date[greatest_decrease_month_index]

# Print financial analysis
print("Financial Analysis\n----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Concatenate financial analysis in variable findings
findings = f"Financial Analysis\n----------------------------\nTotal Months: {total_months}\nTotal: ${total}\nAverage Change: ${average_change}\nGreatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"

# Write findings to text document
financial_analysis_location = pathlib.Path("Analysis/financial_analysis.txt")
financial_analysis_txt = open(financial_analysis_location, "w")
financial_analysis_txt.write(findings)
financial_analysis_txt.close() 