import os
import csv


# set path for file
BudgetFileName = "budget_data.csv"

CurrentDir = os.getcwd()
my_file = os.path.join(CurrentDir, 'Resources', BudgetFileName)

date = []
profitslosses = []
Totalmonths = []

# Define the function and have it use the budget data as it's only paramenter
# def print_analysis(budget_data):





with open(my_file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csv.reader(csvfile))
  
    for row in csvreader:

        date.append(row[0])

        profitslosses.append(row[1])

        monthsum = sum(int(row[0]))
        Totalmonths.append(monthsum)

cleaned_csv = zip(date, profitslosses, Totalmonths)




print(row)
        
   