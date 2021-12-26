
# Add our dependencies.
import csv
import os


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

#declare a new list
candidate_options = []
#declare empty dictionary
candidate_votes ={}

#winning candidate and winning vote count
winning_candidate = ""
winning_count =0
winning_percentage =0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data) 

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            #add the candidate name
            candidate_options.append(candidate_name)
            #begin initialize
            candidate_votes[candidate_name] = 0 
        #add each candidate votes
        candidate_votes[candidate_name] += 1

        
#print the candidate list
print(candidate_votes)

#determine the percentage of votes
#iterate through candidate list
for candidate_name in candidate_votes:
    #retreive the vote count
    votes = candidate_votes[candidate_name]
    #calculate the percentage
    votes_percentage = float(votes)/float(total_votes) *100
    #print the candidate name and its percentage
    print(f"{candidate_name}: received {votes_percentage}% of the vote.")

    #determine winning vote
    if (votes > winning_count) and (votes_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = votes_percentage
        winning_candidate = candidate_name
    print (f"{candidate_name}: {votes_percentage:.1f}%  {votes:,}\n")

    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate:}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")
    print(winning_candidate_summary)

    
