# Election_Anyalsis
## Project Overview
A Colorado Board of Elections employee has asked for an audit of the recent local congressional election.
### Tasks Required:
1. Calculate the total number of votes cast.
2. Get a complete list of all candidates who received votes.
3. Calculate the total votes received for each candidate.
4. Calculate the percentage of total votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resourses
 - data source provided by Board of Elections: election_results.csv
 
 ## Summary:
There were 369,711 total votes cast in this election.

Votes cast by county:
- Jefferson: 10.51% (38,855)
- Denver: 82.78% (306,055)
- Arapahoe: 6.71% (24,801)

Denver county had the highest voter turnout with 306,055 votes cast.

The candidates who received votes were:
- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane
The voting results were:
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

The winner of the election was:
Diana DeGette who received 272,892 votes, which was 73.8% of the total vote.

### Audit Summary:
This script is fairly simple to construct and can be used to audit various single race elections by simply modifying the variables to make sense for the race to be audit. For instance a local election might be interested in votes by precinct rather than county. By highlighting all the places where county variables/print labels are you can replace them with precinct labels.
  1: Create a county list and county votes dictionary.
  **counties = [] replace with *precinct***

**election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")** replace with ***f"Precinct Votes***

This script could also be used to audit elections with multiple races. You would have to add a few more lists, dictionaries, and variables to hold all of the information required depending on the number of races on the ballot, but with a litte care it could easily be done. 
If the results are stored with ballot number, race title, vote cast then a loop would iterate through the ballots to separate out each race with a loop inside that to iterate through the candidates to count vote totals for each candidate or proposal in each race.


