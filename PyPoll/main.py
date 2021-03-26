import os
import csv

#set path for file
election_file = os.path.join(os.getcwd(), 'Resources', "election_data.csv")

with open(election_file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Move past header
    next(csv.reader(csvfile))

    # Create arrays to hold all data that we read in
    Votes = []
    CandidatesList = []
    CandidateVoteCount = []
    Candidates = []


    for row in csvreader:

        #Read in the CSV values into the arrays
        
        Votes.append(int(row[0]))
        
        Candidates = (row[2])
   
        
        if Candidates in CandidatesList:
            CandidateIndex = CandidatesList.index(Candidates)
            CandidateVoteCount[CandidateIndex] = CandidateVoteCount[CandidateIndex] + 1
        else:
            CandidatesList.append(Candidates)
            CandidateVoteCount.append(1)
        

    print(f"Election Results")
    print("-----------------------------")
    print(f"Total Votes: {len(Votes)}" )
    print("-----------------------------")
    #print(f"Total: ${locale.currency(sum(ProfitsLosses), grouping=True)}")
    #print(f"Average Change: ${str(round(sum(ProfitsLosses) / len(Months), 2))  }")
    
    # In order to show the Candidate that won, we need to first determine
    # the max/min and then use the .index function to determine the CSV line the first occurrance of the max/min
    # happened on. We can then use that to index into the Months array.