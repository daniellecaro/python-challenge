import csv
import os

# Define data path
election_data = os.path.join('Resources/election_data.csv')

# Set variables
total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

# Set lists 
unique_list = []
candidate_name = []

# Open csv file
with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Skip Header
    csv_header = next(csv_reader)

    # To read all the rows of data
    for row in csv_reader:

        total_votes +=1

        # Append total votes by candidate
        for names in candidate_name:
            if row [2] not in candidate_name:
                candidate_name.append(row[2])

        # Vote count by candidate
        if row[2] == "Charles Casper Stockham":
            stockham_votes = stockham_votes + 1 
        elif row[2] == "Diana DeGette":
            degette_votes =  degette_votes + 1 
        else:
            doane_votes = doane_votes + 1 
        
    # Calculate percentage of votes each candidate won
    stockham_percent = (stockham_votes / total_votes)
    degette_percent = (degette_votes / total_votes)
    doane_percent = (doane_votes / total_votes)

    # Identify popular vote winner
    winner = max(stockham_votes,degette_votes,doane_votes)

    # Display name of winner
    if winner == stockham_votes:
        winner_name = "Charles Casper Stockham"
    elif winner == degette_votes:
        winner_name = "Diana DeGette"
    else:
        winner_name = "Raymon Anthony Doane"

# Print the analysis 
print("Election Results")
print("-------------------------------------------------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------------------------------------------------")
print(f'Charles Casper Stockham: {stockham_percent: .3%} ({stockham_votes})')
print(f'Diana DeGette: {degette_percent: .3%} ({degette_votes})')
print(f'Raymon Anthony Doane: {doane_percent: .3%} ({doane_votes})')
print("-------------------------------------------------------------------")
print(f'Winner is: {winner_name} with {winner} votes!')
print("-------------------------------------------------------------------")


# Print results to text file*********** 
with open('analysis/election_data.txt', 'w') as text:
    # with open('election_data.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------------------------------------------------\n")
    text.write(f'Total Votes: {total_votes}\n')
    text.write("-------------------------------------------------------------------\n")
    text.write(f'Charles Casper Stockham: {stockham_percent: .3%} ({stockham_votes})\n')
    text.write(f'Diana DeGette: {degette_percent: .3%} ({degette_votes})\n')
    text.write(f'Raymon Anthony Doane: {doane_percent: .3%} ({doane_votes})\n')
    text.write("-------------------------------------------------------------------\n")
    text.write(f'Winner is: {winner_name} with {winner} votes!\n')
    text.write("-------------------------------------------------------------------\n")
