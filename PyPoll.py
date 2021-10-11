import csv
import os

# get data and create file for analysis
input_path = os.path.join('Resources', 'election_results.csv')
output_path = os.path.join('analysis', 'election_analysis.txt')

#set variables
candidate_options = []
candidate_votes = {}
num_votes = 0

winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Load in data
with open(input_path) as election_file:
    election_data = csv.reader(election_file)
    next(election_data)

    for row in election_data:

        # Get the number of votes cast from the length of the data.
        num_votes += 1

        # Get a set of the candidates
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Tally each vote towards the apporpriate candidate
        candidate_votes[candidate_name] += 1 

# Write results to file
with open(output_path, "w") as analysis:


# Write the number of votes cast
    election_results = (
        'Election Results\n'
        f'-------------------------\n'
        f'Total Votes: {num_votes:,}\n'
        f'-------------------------\n')

    analysis.write(election_results)
    print(election_results, end="")

    # Write the percentage of the vote earned by each candidate
    for candidate in candidate_options:
        votes = candidate_votes[candidate]
        vote_percentage = (votes / num_votes) * 100
        analysis.write(f'{candidate}: {vote_percentage:.1f}% ({votes:,})\n')
        print(f'{candidate}: {vote_percentage:.1f}% ({votes:,})')

        # get the candidate with the highest number of votes
        if votes > winning_count:
            winning_candidate = candidate
            winning_count = votes
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n')
    analysis.write(winning_candidate_summary)
    print(winning_candidate_summary)
# analysis.write()
# analysis.close()