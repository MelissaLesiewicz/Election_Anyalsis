# The data we need to retrieve.

# 1. Open data file
import csv
import os
# Assign a varialbe for the file to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to save file to a path.
file_to_save = os.path.join("analysis","elections_analysis.txt")
# 2. Assign variables, lists, dictionaries, etc.
#variable to set accumulator to count total votes
total_votes = 0
#create new list to hold canidates in election
candidate_options = []
#create dictionary to hold votes count for each candicate
candidate_votes = {}
#create variables to hold Winning Candidate & count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 3. Open election results and read the file
# election_data = open("Resources/election_results.csv","r") replaced with
with open(file_to_load) as election_data:

    # 4. perform analysis
    # 4a. get data to read for analysis
    file_reader = csv.reader(election_data)
    # 4a. remove header row from data to analyze
    headers = next(file_reader)
    # 4b. iterate through rows to determine total votes & get list of candidates
    for row in file_reader:
        #add to the total vote count
        total_votes +=1
        #get candidate names
        candidate_name = row[2]
        #add candidates names to list if not already in list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #start tracking each candidate's vote count
            candidate_votes[candidate_name] =0
            #add vote to candidate total
        candidate_votes[candidate_name] += 1
    # 4c.iterate through candidate list to detemine percentage of vote for each candidate
    for candidate_name in candidate_votes:
        #get total vote for candidate
        votes = candidate_votes[candidate_name]
        #calculate vote percentage
        vote_percentage = float (votes) / float (total_votes) * 100
        # print each candidate's name, vote percentage, & vote total
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # 4d. determine winning candidate, vote percentage, & vote total
        #check if candidate vote count & percentage is greater than current winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #update winning variable as needed
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        #create winner summary for printing
        winning_candidate_summary = (
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
#5. Print winner summary
print(winning_candidate_summary)
   
#using the open function with the "w" mode we will write datat to the file 

with open(file_to_save, "w") as txt_file:

#practice writing to a text file
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n")


