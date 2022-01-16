# PyPoll

# Importing os and csv 
import os
import csv

# Set File Path, relative path
csv_path = os.path.join("Resources", "election_data.csv")

# Initialize Count
count = 0

# Stroage Lists 
candidate_list = []
unique_candidate = []
vote_count = []
vote_percentage = []

# Open csv file using csv_path
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # for loop
    for row in csvreader:
        # total vote count
        count = count + 1
        # candidate_list
        candidate_list.append(row[2])
    # unique_candidate
    for x in set(candidate_list):
        unique_candidate.append(x)
        # total vote per candiate
        y = candidate_list.count(x)
        # append vote_count
        vote_count.append(y)
        # vote percentage per candidate
        z = (y/count) * 100
        # append vote_percentage
        vote_percentage.append(z)

    # count of the winning vote
    winning_count = max(vote_count)
    # Who won?
    winning_candidate = unique_candidate[vote_count.index(winning_count)]

# formating ex, line 77 in README.md
print("------------------------------------------------------")
print("Election Results")
print("------------------------------------------------------")
print("Total Votes " + str(count))
print("------------------------------------------------------")
for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ": " + str(round(vote_percentage[i])) + "% (" + str(vote_count[i]) + ")")
print("------------------------------------------------------")
print("Winner: " + winning_candidate)
print("------------------------------------------------------")

# text file
with open("election_results.txt", "w") as text:
    text.write("------------------------------------------------------\n")
    text.write("Election Results\n")
    text.write("------------------------------------------------------\n")
    text.write("Total Votes " + str(count) + "\n")
    text.write("------------------------------------------------------\n")
    for i in range(len(unique_candidate)):
        text.write(unique_candidate[i] + ": " + str(round(vote_percentage[i])) + "% (" + str(vote_count[i]) + ")\n")
    text.write("------------------------------------------------------\n")
    text.write("Winner: " + winning_candidate + "\n")
    text.write("------------------------------------------------------\n")

