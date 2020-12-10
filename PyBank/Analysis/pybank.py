
import csv

budged_data_csv = "/Users/paulalopes/Desktop/Boot Camp/Python/Python-challenge/PyBank/Resources/pybank_challenge.cvs (1).csv"

months = []

i = 2

sum = 0

lista = []




#Open and read csv
with open(budged_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    #Read through each row of data after the header
    for row in csv_file:
       months.append(row[0])
        total_months = len(months)
       

    print(total_months)



for i in (n,2):
    sum = sum + arq[i]
lista.append(sum)






