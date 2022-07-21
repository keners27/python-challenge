import os
import csv

pypoll_csv = os.path.join('..', 'Resources', 'election_data.csv')


total_votes = 0 
cha_votes = 0
dia_votes = 0
ray_votes = 0


with open(pypoll_csv) as csvfile:


     csvreader = csv.reader(csvfile, delimiter=",") 

 
     header = next(csvreader)     

    
     for row in csvreader: 

       
        total_votes +=1

       
        if row[2] == "Charles Casper Stockham": 
            cha_votes +=1
        elif row[2] == "Diana DeGette":
            dia_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            ray_votes +=1
        

candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [cha_votes, dia_votes,ray_votes]


dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)


cha_percent = (cha_votes/total_votes) *100
dia_percent = (dia_votes/total_votes) * 100
ray_percent = (ray_votes/total_votes)* 100


print(f"Election Results")
print(f"-----------------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------------------------")
print(f"Charles Casper Stockham: {cha_percent:.3f}% ({cha_votes})")
print(f"Diana DeGette: {dia_percent:.3f}% ({dia_votes})")
print(f"Raymon Anthony Doane: {ray_percent:.3f}% ({ray_votes})")
print(f"-----------------------------------------------")
print(f"Winner: {key}")
print(f"-----------------------------------------------")




from pathlib import Path 
output_file = Path("..", "Analysis", "election_results.txt")

with open(output_file,"w") as f:

    f.write("Election Results")
    f.write("\n")
    f.write("------------------------------------------------")
    f.write("\n")
    f.write(f"Total Votes: {total_votes}")
    f.write("\n")
    f.write(f"-----------------------------------------------")
    f.write("\n")
    f.write(f"Charles Casper Stockham: {cha_percent:.3f}% ({cha_votes})")
    f.write("\n")
    f.write(f"Diana DeGette: {dia_percent:.3f}% ({dia_votes})")
    f.write("\n")
    f.write(f"Raymon Anthony Doane: {ray_percent:.3f}% ({ray_votes})")
    f.write("\n")
    f.write("------------------------------------------------")
    f.write("\n")
    f.write(f"Winner: {key}")
    f.write("\n")
    f.write("------------------------------------------------")