import os
import csv

pypoll_csv = os.path.join('..', 'Resources', 'election_data.csv')


total = 0 
cha = 0
dia = 0
ray = 0


with open(pypoll_csv) as csvfile:


     csvreader = csv.reader(csvfile, delimiter=",") 

 
     header = next(csvreader)     

    
     for row in csvreader: 

       
        total +=1

       
        if row[2] == "Charles Casper Stockham": 
            cha +=1
        elif row[2] == "Diana DeGette":
            dia +=1
        elif row[2] == "Raymon Anthony Doane": 
            ray +=1
        

candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [cha, dia,ray]


dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)


cha_percent = (cha/total) *100
dia_percent = (dia/total) * 100
ray_percent = (ray/total)* 100


print(f"Election Results")
print(f"-----------------------------------------------")
print(f"Total Votes: {votes}")
print(f"-----------------------------------------------")
print(f"Charles Casper Stockham: {cha_percent:.3f}% ({cha})")
print(f"Diana DeGette: {dia_percent:.3f}% ({dia})")
print(f"Raymon Anthony Doane: {ray_percent:.3f}% ({ray})")
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
    f.write(f"Total Votes: {total}")
    f.write("\n")
    f.write(f"-----------------------------------------------")
    f.write("\n")
    f.write(f"Charles Casper Stockham: {cha_percent:.3f}% ({cha})")
    f.write("\n")
    f.write(f"Diana DeGette: {dia_percent:.3f}% ({dia})")
    f.write("\n")
    f.write(f"Raymon Anthony Doane: {ray_percent:.3f}% ({ray})")
    f.write("\n")
    f.write("------------------------------------------------")
    f.write("\n")
    f.write(f"Winner: {key}")
    f.write("\n")
    f.write("------------------------------------------------")