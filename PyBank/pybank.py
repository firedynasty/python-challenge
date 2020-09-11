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
    

    greatest_increase = int(max(change_list))
    greatest_decrease = int(min(change_list))
    

    max_month_index = change_list.index(greatest_increase)
    min_month_index = change_list.index(greatest_decrease)
    print(f'Total months: {len(months)}')
    print(f'Total: {total}')
    print(f'The average change: {round(average_is,2)}')
    print(f'Greatest increase in profits: {months[max_month_index+1]} (${greatest_increase})')
    print(f'Greatest decrease in profits: {months[min_month_index+1]} (${greatest_decrease})' )

output_path = os.path.join("output", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as writer:
    writer.write('FINANCIAL ANALYSIS')
    writer.write('\n----------------------------------')
    writer.write(f'\nTotal months: {len(months)}')
    writer.write(f'\nTotal: {total}')
    writer.write(f'\nThe average change: {round(average_is,2)}')
    writer.write(f'\nGreatest increase in profits: {months[max_month_index+1]} (${greatest_increase})')
    writer.write(f'\nGreatest decrease in profits: {months[min_month_index+1]} (${greatest_decrease})')
    





    
       
        

    
    #create two lists using zip 
    #why can't you write the new changes to another csv file?
    #do it with zip
    
    
        
    
#finding the greatest and least amount change:
#the way to do that is from that list what you can do is call the greatest or the least number


    
#finding the average change and in this way you need to be able to locate the change for each month
#then you can subtract from month to month

#how do I get the previous row?

#create a list
#then from the list what you want to do is to subtract each other

# Write a function that returns the arithmetic average for a list of numbers

# you can use a list comprehension to subtract a number from a previous number
# or in this case what you can do is : 
#select a range and then in the list you can do stuff to it
    


