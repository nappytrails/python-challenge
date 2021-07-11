# Import needed libraries: pathlib, csv
import pathlib
import csv

# Store the path to budget_data.csv
budget_data_location = pathlib.Path(Resources/budget_data.csv)

# Open budget_data.csv as read only
with open(budget_data_location) as budget_data_csv
    read_budget_data = csv.reader(budget_data_csv, delimiter=",")
