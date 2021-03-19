import os
import csv



BudgetFileName = "budget_data.csv"

CurrentDir = os.getcwd()
my_file = os.path.join(CurrentDir, 'Resources', BudgetFileName)


#set path for file
with open(my_file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csv.reader(csvfile) )
    
    reader = csv.reader(csvfile)
    print(csvreader)
    
    
    for row in reader:

        print(row)
        
   