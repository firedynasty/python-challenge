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


# read the file
