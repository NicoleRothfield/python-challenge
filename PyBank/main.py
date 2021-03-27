import os
import csv
import locale

#set $ to USA 
locale.setlocale( locale.LC_ALL, '' )

# Takes a decimal number and returns a string representing the value in currency notation.
# Negative values are enclosed in parenthesis
def currencyToString(value):
    if (value < 0):
        return "(" + locale.currency(value * -1, grouping=True) + ")"
    else:
        return locale.currency(value, grouping=True)

# set path for file
my_file = os.path.join(os.getcwd(), 'Resources', "budget_data.csv")

with open(my_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # We expect a header. Move past it to the data.
    next(csv.reader(csvfile))
  
    # Create arrays to hold all data that we read in
    Months = []
    ProfitsLosses = []
    MonthlyChanges = []
    PriorMonthProfitsLoss = 0

    for row in csvreader:
        # Read in the CSV values into the arrays
        Months.append(row[0])
        ProfitsLosses.append(int(row[1]))
        
        if len(ProfitsLosses) > 1:
            MonthlyChanges.append(int(row[1]) - PriorMonthProfitsLoss)

        PriorMonthProfitsLoss = int(row[1])

    print(f"Financial Analysis")
    print("-----------------------------")
    print(f"Total Months: {len(Months)}" )
    print(f"Total: {locale.currency(sum(ProfitsLosses), grouping=True)}")
    print(f"Average Change: ${str(round(sum(MonthlyChanges) / len(MonthlyChanges), 2))  }")

    # In order to show the month in which we incurred our greatest profit/loss, we need to first determine
    # the max/min and then use the .index function to determine the CSV line the first occurrance of the max/min
    # happened on. We can then use that to index into the Months array.
    maxProfit = max(MonthlyChanges)
    minProfit = min(MonthlyChanges)

    maxProfitMonthIndex = MonthlyChanges.index(maxProfit)
    minProfitMonthIndex = MonthlyChanges.index(minProfit)

    print(f"Greatest Increase in Profits: {Months[maxProfitMonthIndex + 1]} {currencyToString(maxProfit)}")
    print(f"Greatest Decrease in Profits: {Months[minProfitMonthIndex + 1]} {currencyToString(minProfit)}")

file = open("FinancialAnalysis.txt","w+")

file.write(f"Financial Analysis\n")
file.write("-----------------------------\n")
file.write(f"Total Months: {len(Months)}\n" )
file.write(f"Total: {locale.currency(sum(ProfitsLosses), grouping=True)}\n" )
file.write(f"Average Change: ${str(round(sum(MonthlyChanges) / len(MonthlyChanges), 2))  }\n")
file.write(f"Greatest Increase in Profits: {Months[maxProfitMonthIndex]} {currencyToString(maxProfit)}\n")
file.write(f"Greatest Decrease in Profits: {Months[minProfitMonthIndex]} {currencyToString(minProfit)}\n")

file.close()



    