# Python File for PyBank
# ----------------------------------------------------------------------------------------------------------
# INSTRUCTIONS
#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#-----------------------------------------------------------------------------------------------------------
# Modules
import os
import csv

budget_csv = os.path.join("budget_data.csv")

with open(budget_csv, newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')

   row_count = (sum(1 for row in csvreader) - 1)
   print(row_count)

   total = 0

   for row in csvreader:
       total = sum(int(row[1]))
   print(total)

   max_profit = 0
   min_profit = 0

   csvfile.seek(0)

   for row in csvreader:
       max_profit = max(int(row[1]))
       min_profit = min(int(row[1]))
   print(max_profit)
   print(min_profit)

