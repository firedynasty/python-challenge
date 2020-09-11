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

    #now that I have the lists, I can take a measure of the number of individual indexes 
    #and then do a printout 
    
    Khan_count = len(Khan)
    Correy_count = len(Correy)
    Li_count = len(Li)
    O_Tooley_count = len(O_Tooley)
    total_votes_count = len(total_votes)
    
    Khan_percentage = round((Khan_count / total_votes_count) *100, 3)
    Correy_percentage = round((Correy_count / total_votes_count) *100, 3)
    Li_percentage = round((Li_count / total_votes_count) *100, 3)
    O_Tooley_percentage = round((O_Tooley_count / total_votes_count) *100, 3)
    
    print('Election Results')
    print('--------------------------------')
    print(f'Total Votes: {total_votes_count}')
    print('--------------------------------')
    print(f'Khan: {Khan_percentage}% ({Khan_count})')
    print(f'Correy: {Correy_percentage}% ({Correy_count})')
    print(f'Li: {Li_percentage}% ({Li_count})')
    print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley_count})")
    print('--------------------------------')
    print('Winner: Khan')
    print('--------------------------------')
    
output_path = os.path.join("output", "voter_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as writer:
    writer.write('Election Results')
    writer.write('\n--------------------------------')
    writer.write(f'\nTotal Votes: {total_votes_count}')
    writer.write('\n--------------------------------')
    writer.write(f'\nKhan: {Khan_percentage}% ({Khan_count})')
    writer.write(f'\nCorrey: {Correy_percentage}% ({Correy_count})')
    writer.write(f'\nLi: {Li_percentage}% ({Li_count})')
    writer.write(f"\nO'Tooley: {O_Tooley_percentage}% ({O_Tooley_count})")
    writer.write('\n--------------------------------')
    writer.write('\nWinner: Khan')
    writer.write('\n--------------------------------')