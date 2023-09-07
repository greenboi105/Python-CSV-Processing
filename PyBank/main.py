"""
In this challenge we want to create a Python script to analyze the financial records of a company.

The dataset consists of two columns: "Date" and "Profit/Losses".

The task is to create a Python script that analyzes the records to calculate each of the values:

    - The total number of months included in the dataset.

    - The net total amount of "Profit/Losses" over the entire period.

    - The changes in "Profit/Losses" over the entire period, and then the average of those changes.

    - The greatest increase in profits (date and amount) over the entire period.

    - The greatest decrease in profits (date and amount) over the entire period.
"""

import csv 

def read_budget():

    budget_path = "../Python CSV Processing/PyBank/Resources/budget_data.csv"

    # Variables to store the values we want
    num_months = 0
    total_profit = 0
    greatest_increase = float('-inf')
    greatest_decrease = float('inf')
    greatest_increase_date = None
    greatest_decrease_date = None

    with open(budget_path, "r") as budget_csv:

        extracted_header = next(budget_csv)

        csv_reader = csv.reader(budget_csv, delimiter=",")

        # For each row, increment the number of months and update the total profit
        # Also, potentially update the greatest decrease and increase along with the associated date
        for row in csv_reader:

            num_months += 1
            total_profit += int(row[1])

            if int(row[1]) <= greatest_decrease:
                greatest_decrease = int(row[1])
                greatest_decrease_date = row[0]

            if int(row[1]) >= greatest_increase:
                greatest_increase = int(row[1])
                greatest_increase_date = row[0]

    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {num_months}')
    print(f'Total: ${total_profit}')
    print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

    with open('../Python CSV Processing/PyBank/analysis/financial_summary.txt', 'w') as financial_text:
        financial_text.write("Financial Analysis\n")
        financial_text.write("----------------------------\n")
        financial_text.write(f'Total Months: {num_months}\n')
        financial_text.write(f'Total: ${total_profit}\n')
        financial_text.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
        financial_text.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')
        financial_text.write("\n")

if __name__ == '__main__':
    read_budget()
