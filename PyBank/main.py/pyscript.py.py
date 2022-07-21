import os
import csv


pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

date = []
total_profit = []
monthly_profit = []

with open(pybank_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",") 

    header = next(csvreader)  

    for row in csvreader: 

        date.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        
        monthly_profit.append(total_profit[i+1]-total_profit[i])
        

increase = max(monthly_profit)
decrease = min(monthly_profit)

max_increase = monthly_profit.index(max(monthly_profit)) + 1
max_decrease = monthly_profit.index(min(monthly_profit)) + 1 

print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit)/len(monthly_profit),2)}")
print(f"Greatest Increase in Profits: {date[max_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {date[max_decrease]} (${(str(decrease))})")


from pathlib import Path 
output_file = Path("..", "analysis", "finance.txt")

with open(output_file,"w") as f:

    f.write("Financial Analysis")
    f.write("\n")
    f.write("--------------------------------------")
    f.write("\n")
    f.write(f"Total Months: {len(date)}")
    f.write("\n")
    f.write(f"Total: ${sum(total_profit)}")
    f.write("\n")
    f.write(f"Average Change: {round(sum(monthly_profit)/len(monthly_profit),2)}")
    f.write("\n")
    f.write(f"Greatest Increase in Profits: {date[max_increase]} (${(str(increase))})")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits: {date[max_decrease]} (${(str(decrease))})")




