#doing the homework 
#pretty much this is how I would get started
#import modules
# read the file
# to calculate the number of months 

# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV

months = []
earnings_per_month = []
change_list = []
total = 0
i = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Loop through looking for the csv reader
    header = next(csvreader)

    #get a list of the changes from month to month
    for row in csvreader:
        earnings_per_month.append(row[1]) 
        months.append(row[0])
        total = total + float(row[1])
        
    #from the list then you can subtract each subsequent month from the previous one
    #add it to a new list
    
    for i in range(1, len(earnings_per_month)):
       changes = int(earnings_per_month[i]) - int(earnings_per_month[i-1])
       change_list.append(changes)
    
    #then you can take the average of the list
    average_is = sum(change_list) / len(change_list)
    
    print('FINANCIAL ANALYSIS')
    print('----------------------------------')
    
    #set the max value and min value of profit into a variable

    greatest_increase = int(max(change_list))
    greatest_decrease = int(min(change_list))
    

    #get the value of the index of where the value is in the list
    max_month_index = change_list.index(greatest_increase)
    min_month_index = change_list.index(greatest_decrease)
    
    #print the values
    print(f'Total months: {len(months)}')
    print(f'Total: {total}')
    print(f'The average change: {round(average_is,2)}')
    print(f'Greatest increase in profits: {months[max_month_index+1]} (${greatest_increase})')
    print(f'Greatest decrease in profits: {months[min_month_index+1]} (${greatest_decrease})' )

output_path = os.path.join("output", "budget_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as writer:
    writer.write('FINANCIAL ANALYSIS')
    writer.write('\n----------------------------------')
    writer.write(f'\nTotal months: {len(months)}')
    writer.write(f'\nTotal: {total}')
    writer.write(f'\nThe average change: {round(average_is,2)}')
    writer.write(f'\nGreatest increase in profits: {months[max_month_index+1]} (${greatest_increase})')
    writer.write(f'\nGreatest decrease in profits: {months[min_month_index+1]} (${greatest_decrease})')