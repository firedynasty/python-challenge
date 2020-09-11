#PyPoll

#scrape together everything in a big list then from the list you can do a len of the list 
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

total_votes = []
Khan = []
Correy = []
Li = []
O_Tooley = []

with open(csvpath) as csvfile:
    # read the file    
    csvreader = csv.reader(csvfile, delimiter=",")
    #Loop through looking for the csv reader
    header = next(csvreader)

    for row in csvreader:
        total_votes.append(row[0])
        if row[2] == "Khan":
            Khan.append(row[2])
        elif row[2] == "Correy":
            Correy.append(row[2])
        elif row[2] == "Li":
            Li.append(row[2])
        else:
            O_Tooley.append(row[2])
    
    