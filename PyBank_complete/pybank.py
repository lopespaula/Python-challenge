
import csv
import os

csvpath = os.path.join('Resources', 'budget_data.csv')

#variables
total_months = 0
total_net = 0

#lists
list_profit_losses = []
list_months = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

#Open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read the header row first
    csv_header = next(csv_reader)

    #Read through each row of data after the header
    first_row = next(csv_reader)
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in csv_reader:

    #The total number of months included in the dataset
        total_months += 1

    #The net total amount of "Profit/Losses" over the entire period
        profit_losses = int(row[1])
        total_net += profit_losses

    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        changes = int(row[1]) - prev_net
        prev_net = int(row[1])

        list_profit_losses += [changes]
        list_months += [row[0]]

    #The greatest increase in profits (date and amount) over the entire period
        if changes > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = changes

    #The greatest decrease in losses (date and amount) over the entire period
        if changes < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = changes


avg_changes = round(sum(list_profit_losses) / len(list_profit_losses), 2)
       

#Print the analysis

print('Financial Analysis')
print('------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_net}')
print(f'Average Change: ${avg_changes}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')
print('------------------------------')


#Export a text file with the results
results_file = os.path.join('Analysis', 'results_pybank.txt')
with open(results_file, "w") as txtfile:

    txtfile.write('Financial Analysis\n')
    txtfile.write('------------------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${total_net}\n')
    txtfile.write(f'Average Change: ${avg_changes}\n')
    txtfile.write(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n')
    txtfile.write(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n')
    txtfile.write('------------------------------\n')





