# PyBank, python-challenge

# imports
import os
import csv

# csv file path
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Create Storage Lists ["Count", "Average Change", "Date"]

count = []
avg_change = []
date = []

# Set Inital Variables ["Count", "Total Profit", "Net Profit", "Intial Profit"]

count = 0
total_profit = 0
net_profit = 0
intial_profit = 0

# Open with CSV File using pybank_csv, relative path

with open(pybank_csv, newline = "") as csvfile:

    # CSV reader specifing delimiter=','
    csvreader = csv.reader(csvfile, delimiter=",")
    # CSV header  
    csv_header = next(csvreader)

    

