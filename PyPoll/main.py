"""
This this Challenge we are tasked with helping a small, rural town modernize its vote-counting process.

We are given a set of poll data. The datasets consists of three columns: "Voter ID", "County", and "Candidate".

We want to create a Python script that analyzes the votes and calcualtes the values:

    - Total number of votes cast.

    - A complete list of candidates who received votes.

    - The percentage of votes each candidate won.

    - The total number of votes each candidate won.

    - The winner of the election based on popular vote.
"""

import csv
from collections import defaultdict

def read_votes():

    voter_path = "./Python CSV Processing/PyPoll/Resources/election_data.csv"

    num_votes = 0
    candidate_votes = defaultdict(int)

    with open(voter_path, "r") as voter_csv:

        extraced_header = next(voter_csv)

        csv_reader = csv.reader(voter_csv, delimiter=",")

        for row in csv_reader:

            num_votes += 1
            candidate_votes[row[2]] += 1

        print("Election Results")
        print("-------------------------")
        print(f'Total Votes: {num_votes}')
        print("-------------------------")
        
        candidate_list = list(candidate_votes.keys())

        voting_winner = [None, float('-inf')]

        for candidate_name in candidate_list:

            candidate_percentage = candidate_votes[candidate_name] / num_votes * 100

            if candidate_votes[candidate_name] > voting_winner[1]:
                voting_winner[0] = candidate_name
                voting_winner[1] = candidate_votes[candidate_name]

            print(f'{candidate_name}: {candidate_percentage}% ({candidate_votes[candidate_name]})')

        print("-------------------------")
        print(f'Winner: {voting_winner[0]}')
        print("-------------------------")

    with open('voting_summary.txt', 'w') as voting_text:

        voting_text.write("Election Results\n")
        voting_text.write("----------------------------\n")
        voting_text.write(f'Total Votes: {num_votes}\n')
        voting_text.write("----------------------------\n")
        for candidate_name in candidate_list:
            voting_text.write(f'{candidate_name}: {candidate_percentage}% ({candidate_votes[candidate_name]})\n')
        voting_text.write("----------------------------\n")
        voting_text.write(f'Winner: {voting_winner[0]}\n')
        voting_text.write("----------------------------\n")

if __name__ == '__main__':
    read_votes()
