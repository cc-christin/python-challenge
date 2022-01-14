# PyBank, python-challenge

# imports
import os
import csv

# csv file path
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Create Storage Lists ["Count", "Average Change", "Date"]

PL = []
monthly = []
date = []

# Set Inital Variables ["Count", "Total Profit", "Net Profit", "Intial Profit"]

count = 0
total_profit = 0
net_profit = 0
initial_profit = 0

# Open with CSV File using pybank_csv, relative path

with open(pybank_csv, newline = "") as csvfile:

    # CSV reader specifing delimiter=','
    csvreader = csv.reader(csvfile, delimiter=",")
    # CSV header  
    csv_header = next(csvreader)

    # For Loop reading each row of data after the header
    # for <variable> in <list sequence> 
    for row in csvreader:
        # Count the number of months
        count = count + 1

        # Appending row[0] to list, date
        date.append(row[0])

        # Appending row[1], Profit/Losses to list, PL
        PL.append(row[1])

        # Count of Total Profit from Profit/Losses, row[1]
        total_profit = total_profit + int(row[1])

        # Final Profit, equivalent to Profit/Losses, row[1] 
        final_profit = int(row[1])

        # Calculate Average Monthly Change in Profits
        monthly_change_profits = final_profit - initial_profit 
        

        # Append monthly with Calculate Average Monthly Change in Profits, monthly_change_profits
        monthly.append(monthly_change_profits)

        # Calculate Total Change by Adding Average Monthly Change in Profits to Existing Total
        total_change_profits = total_change_profits + monthly_change_profits

        # Set Inital Equal to Final
        initial_profit = final_profit

        # Calculate Average Change in Profits 
        avg_change_profit = (total_change_profits/ count)

        # Find the Maximum and Minimum Changes in Profits
        greatest_profit_increase = max(monthly)
        greatest_profit_decrease = min(monthly)

        # Find corresponding dates for min <-> max(monthly)
        max_date = date[monthly.index(greatest_profit_increase)]
        min_date = date[monthly.index(greatest_profit_decrease)]

        # Print Functions













        # appending 

    

