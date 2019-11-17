import os
import csv


runner = []
votes_cast = 0
vote_counts = []
percentages = []

MyPoll = os.path.join("election_data.csv")

with open(MyPoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    first_row = next(csvreader)

    
    for row in csvreader:

       
        votes_cast = votes_cast + 1

        
        cand = row[2]

       
        if cand in runner:
            candidate_index = runner.index(cand)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            runner.append(cand)
            vote_counts.append(1)



        index = 0

        MostVotes = vote_counts[0]
        



    for count in range(len(runner)):
        vote_percentage = vote_counts[count]/votes_cast*100

        percentages.append(vote_percentage)

        if vote_counts[count] > MostVotes:
            MostVotes = vote_counts[count]
            print(max_votes)
            index = count


        winner = runner[index]

print('\n')
print("Election Results")
print("---------------------------------")
print('\n')
print(f"Total Votes:          {votes_cast}")

for count in range(len(runner)):
    print(f" {runner[count]} {percentages[count]} {vote_counts[count]}")
print("---------------------------------")
print(f"Winner:                 {winner}")
print("---------------------------------")





sys.stdout = open("Poll_Result.txt", "w")
print('\n')
print("Election Results")
print("---------------------------------")
print('\n')
print(f"Total Votes:          {votes_cast}")

for count in range(len(runner)):
    print(f" {runner[count]} {percentages[count]} {vote_counts[count]}")
print("---------------------------------")
print(f"Winner:                 {winner}")
print("---------------------------------")