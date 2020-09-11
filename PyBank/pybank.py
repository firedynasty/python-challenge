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

per_month = []
average_list = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
#Loop through looking for the csv reader
    header = next(csvreader)

    #get a list of the changes from month to month
    for row in csvreader:
        per_month.append(row[1]) 

        
    #from the list then you can subtract each subsequent month from the previous one
    #add it to a new list
    
    for i in range(1, len(change)):
       changes = int(change[i]) - int(change[i-1])
       average_list.append(changes)
    
    #then you can take the average of the list
    average_is = sum(average_list) / len (average_list)
    
    print(f'The average change is {average_is}')
    print(average_list)
    print(max(average_list))
    print(min(average_list))
    
    
    #how do I get the corresponding value pair in a list?
    #the way you can do that is to look and print out the line in Excel
    
    
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
    

