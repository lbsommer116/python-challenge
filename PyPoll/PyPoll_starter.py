# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates =[]
vote_count = []
candidate_vote_count = {}

# Winning Candidate and Winning Count Tracker
count_tracker1 = 0
count_tracker2 = 0
count_tracker3 = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        ##print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1                                
       
        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)

        # Add a vote to the candidate's count
        if candidate_name == candidates[0]:
            count_tracker1 = count_tracker1 + 1

        elif candidate_name == candidates[1]:
            count_tracker2 = count_tracker2 + 1
    
        elif candidate_name == candidates[2]:
            count_tracker3 = count_tracker3 + 1

    vote_count.append(count_tracker1)
    vote_count.append(count_tracker2)
    vote_count.append(count_tracker3)
    candidate_vote_count[candidates[0]] = vote_count[0]
    candidate_vote_count[candidates[1]] = vote_count[1]
    candidate_vote_count[candidates[2]] = vote_count[2]

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f'The total vote count is {total_votes}')

    # Write the total vote count to the text file
    txt_file.write('Election Results \n')
    txt_file.write('---------------------------------------------- \n')
    txt_file.write(f'Total Votes: {total_votes} \n')
    txt_file.write('---------------------------------------------- \n')


    # Loop through the candidates to determine vote percentages and identify the winner
    print(f'Here are the vote counts:')
    for keys in candidate_vote_count:

        # Get the vote count and calculate the percentage
        values = candidate_vote_count[keys]
        percentage = round(values/total_votes * 100,3)

        # Update the winning candidate if this one has more votes
        if values is max(vote_count):
            winner = vote_count.index(values)


        # Print and save each candidate's vote count and percentage
        candidate_summary = [f'{keys}: {percentage}% ({values})']
        for items in candidate_summary:
            print(f'{candidate_summary}')
            txt_file.write(f'{items} \n')

    # Generate and print the winning candidate summary
    # Save the winning candidate summary to the text file
    txt_file.write('---------------------------------------------- \n')
    winner_summary = candidates[winner]
    print(f'Winner: {winner_summary}')
    txt_file.write(f'Winner:{winner_summary} \n')
