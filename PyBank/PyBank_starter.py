# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 1
total_net = 0
# Add more variables to track other necessary financial data
net_change = []
months = []
monthly_dict = {}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_net = int(first_row[1])

    #print(total_net)
    previous_row = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total ## and total months
        total_net = total_net + int(row[1])
        total_months = total_months + 1
        months.append(row[0])

        # Track the net change
        net_change.append(int(row[1]) - previous_row)
        previous_row = int(row[1])

       ## Create a dictionary with month name and net change inside and then look up max with month
    monthly_dict = dict(zip(months,net_change))
        
        # Calculate the greatest increase in profits (month and amount)
    max_value = max(net_change)
    max_value_index = net_change.index(max_value) 
    max_month = months[max_value_index]

        # Calculate the greatest decrease in losses (month and amount)
    min_value = min(net_change)
    min_value_index = net_change.index(min_value) 
    min_month = months[min_value_index]
    

# Calculate the average net change across the months
    average_change = round(sum(net_change)/len(net_change),2)

# Generate the output summary


# Print the output

print(f'Total Months: {total_months}')
print(f'Total: ${total_net}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_month} ({max_value})')
print(f'Greatest Decrease in Profits: {min_month} ({min_value})')

# Write the results to a text file

with open(file_to_output, "w") as txt_file:
    txt_file.write(f'Financial Analysis \n')
    txt_file.write(f'--------------------------------------- \n')
    txt_file.write(f'Total Months: {total_months} \n')
    txt_file.write(f'Total: ${total_net} \n')
    txt_file.write(f'Average Change: ${average_change} \n')
    txt_file.write(f'Greatest Increase in Profits: {max_month} (${max_value}) \n')
    txt_file.write(f'Greatest Decrease in Profits: {min_month} (${min_value}) \n')


    

    