import os
import csv

# set path for file
election_file = os.path.join(os.getcwd(), 'Resources', "election_data.csv")


with open(election_file, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Move past header
    next(csv.reader(csvfile))

    # Create arrays to hold all data that we read in
    CandidatesDict = {}

    for row in csvreader:
        #Read in the CSV values into the arrays
        if row[2] in CandidatesDict:
            CandidatesDict[row[2]] = CandidatesDict[row[2]] + 1
        else:
            CandidatesDict[row[2]] = 1

    SumVotes = sum(CandidatesDict.values())

    OutputLines = []
    OutputLines.append(f"Election Results ")
    OutputLines.append("----------------------------- ")
    OutputLines.append(f"Total Votes: {SumVotes}" )
    OutputLines.append("-----------------------------")

    for candidateName, voteCount in CandidatesDict.items():
        percent = round(voteCount / SumVotes * 100, 3)
        OutputLines.append(f"{candidateName}: {percent}% ({voteCount})")

    #Find the winner through this method 
    # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    # Not handling run offs
    Winner = max(CandidatesDict, key=CandidatesDict.get)
    
    OutputLines.append("-----------------------------")
    OutputLines.append(f"Winner: {Winner}" )
    OutputLines.append("-----------------------------")

    for line in OutputLines:
        print(line)

output_file = os.path.join(os.getcwd(), 'analysis', "PollAnalysis.txt")

file = open(output_file,"w+")

for line in OutputLines:
    file.write(line + "\n")

file.close()
