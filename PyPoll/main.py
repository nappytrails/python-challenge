# Import needed libraries: pathlib, csv
import pathlib
import csv

# Store the path to election_data.csv
election_data_location = pathlib.Path("Resources/election_data.csv")

# Create variables to store the columns
voter_id = []
county = []
candidate_voted_for = []

# Open election_data.csv as read only
with open(file=election_data_location, mode="r") as election_data_csv:
    election_data_reader = csv.reader(election_data_csv, delimiter=",")
    
    # Read in the header to exclude it from variable data
    election_data_header = next(election_data_reader)
    
    # Read column data into variables
    for row in election_data_reader:
       voter_id.append(row[0])
       county.append(row[1])
       candidate_voted_for.append(row[2])

# Calculate the total number of votes
total_votes = len(candidate_voted_for)

# Print "Election Results" and total votes
print("Election Results\n-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")


# Put names of candidates in a list
def candidates_in_election(candidates):
    candidate_names = []

    for candidate in candidates:
        if candidate in candidate_names:
            continue
        else:
            candidate_names.append(candidate)
    return candidate_names

candidate_roster = candidates_in_election(candidate_voted_for)

# Calculate number of votes and percentage of vote recieved by each candidate
vote_tally = []
vote_percentage = []

for i in range(len(candidate_roster)):
    current_candidate = candidate_roster[i]
    current_vote_count = 0
    current_percentage_of_vote = 0

    # Tally number of votes for each candidate
    for vote in range(len(candidate_voted_for)):
        if candidate_voted_for[vote] == candidate_roster[i]:
            current_vote_count = current_vote_count +1
        
    # Add each candidate's vote tally to a list
    vote_tally.append(current_vote_count)

    # Assign each candidate's vote count to an independent variable
    locals()["candidate" + str(i) + "_votes"] = current_vote_count

    # Calculate the percent of the vote recieved by each candidate
    current_percentage_of_vote = current_vote_count / total_votes
    vote_percentage.append(current_percentage_of_vote)
    current_percentage_formatted = "{:.3%}".format(current_percentage_of_vote)
    
    # Assign each candidate's percentage of the vote (as a float) to an independent variable
    locals()["candidate" + str(i) + "_percentage_of_vote"] = current_percentage_of_vote

    # Assign each candidate's name to an independent variable
    locals()["candidate" + str(i) + "_name"] = candidate_roster[i]

    # Print election results for each candidate
    print(f"{candidate_roster[i]}: {current_percentage_formatted} ({current_vote_count})")

# Print dividing line
print("-------------------------")

# Determine the winner of the election by popular vote
election_winner_votes = max(vote_tally)
election_winner_index = vote_tally.index(election_winner_votes)
election_winner_name = candidate_roster[election_winner_index]

print(f"Winner: {election_winner_name}")
print("-------------------------")





















# for vote in range(len(candidate_voted_for)):
#     if candidate_voted_for[vote] == candidate0_name:
#         candidate0_votes = candidate0_votes +1
#     elif candidate_voted_for[vote] == candidate1_name:
#         candidate1_votes = candidate1_votes +1
#     elif candidate_voted_for[vote] == candidate2_name:
#         candidate2_votes = candidate2_votes +1
#     elif candidate_voted_for[vote] == candidate3_name:
#         candidate3_votes = candidate3_votes +1

# print("Election Results\n-------------------------")
# print(f"Total Votes: {total_votes}")
# print("-------------------------")
# print(f"{candidate0_name}: ({candidate0_votes})")
# print(f"{candidate1_name}: ({candidate1_votes})")
# print(f"{candidate2_name}: ({candidate2_votes})")
# print(f"{candidate3_name}: ({candidate3_votes})")
# print(vote_tally)
