# The data we need to retrieve.

# 1. Open data file
import csv
import os
# Assign a varialbe for the file to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to save file to a path.
file_to_save = os.path.join("analysis","elections_analysis.txt")
#Open election results and read the file
# election_data = open("Resources/election_results.csv","r") replaced with
with open(file_to_load) as election_data:
    #to do: perform analysis
    file_reader = csv.reader(election_data)
    #print header row
    headers = next(file_reader)
    print(headers)
#print eack row in file_reader
    #for row in file_reader:
    #  print(row)

#using the open function with the "w" mode we will write datat to the file 

with open(file_to_save, "w") as txt_file:

#practice writing to a text file
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n")


# 2. write names of all candidates
# 3. Get total votes for each candidate
# 4. Get number of total votes for election
# 5. Winner of the election based on popular vote.

