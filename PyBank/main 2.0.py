import csv
import os

# Define data path
budget_data = os.path.join('PyBank/Resources/budget_data.csv')

#Set variables
month_count = 0 
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Create lists to store data
profit = []
monthly_changes = []
date = []
total_change_profits_list = []

# Open csv
with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    # Skip Header
    csv_header = next(csv_reader)

    # Set the parameters
    for row in csv_reader:

        # Count the number of months in the dataset
        month_count = month_count + 1
        #print(str(month_count) + "month_count")
    
        # Append date
        date.append(row[0])
        #print(str(date) + "date")

        # Append profit information
        profit.append(row[1])
        #print(str(profit) + "profit")
        
        # Calculate total profit
        total_profit = total_profit + int(row[1])
        print(str(total_profit) + "total_profit")

        #Calculate the average change in profits from month to month. Then calulate the average change in profits
        final_profit = int(row[1])
        print(str(final_profit) + "final_profit")
        print(type(final_profit))
        print(type(initial_profit))
        monthly_change_profits = sum([final_profit,initial_profit])
        print(str(monthly_change_profits) + "monthly_change_profits")

        #Store these monthly changes in a list YOU CAN USE THIS LIST NOW
        monthly_changes.append(monthly_change_profits)
        #print(str(monthly_changes) + "monthly_changes\n" )

        total_change_profits = total_change_profits + monthly_change_profits
        total_change_profits_list.append(total_change_profits)
        print(str(total_change_profits) + "total_change_profits\n")
        
        initial_profit = final_profit
        print(str(initial_profit) + "initial_profit\n")
        print(str(final_profit) + "final_profit\n")

        #Calculate the average change in profits
        average_change_profits = (total_change_profits/month_count)
        #print(str(total_change_profits) + "total_change_profits\n")
        #print(str(month_count) + "month_count\n")
        #print(str(average_change_profits) + "average_change_profits\n")

      
    #Find the max and min change in profits and the corresponding dates these changes were obeserved
    greatest_increase_profits = max(monthly_changes)
    greatest_decrease_profits = min(monthly_changes)

    increase_date = date[monthly_changes.index(greatest_increase_profits)]
    decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

    print (monthly_change_profits)
    print (monthly_change_profits/86)
    
    #monthchange = (sum(monthly_changes))
    #print (monthchange)



    #print(str(date))
    #print(str(profit))
    #print(str(monthly_changes))
    #print(str(increase_date))
    #print(str(decrease_date))
    #print(str(sum(monthly_changes)))
      
    # Print calculations/analysis in terminal 
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(month_count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(month_count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
