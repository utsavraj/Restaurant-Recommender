'''
Language: Python 3 

'''

#!/usr/bin/python

'''
LIBRARIES

'''
import os #To check if file exists in directory
import sys #To use sys.exit
import contextlib #Allows for output from function to go to outputfile.
from itertools import islice #to start from another line



'''
FUNCTIONS

'''

#Stops the system if the budget is negative.
def CheckBudg(n): 
    if n < 0:
        print("Budget cannot be negative!")
        sys.exit() 

#Function which prints the recommended dishes/drinks and their quanities based on budget

def Recommendation(resmenu_dict, budget2):
    resmenu_dictsorted = sorted(resmenu_dict, key=resmenu_dict.get, reverse=True) #Sorting decending order
    temp_budget = budget2
    recomm_dict = {}
    for item in resmenu_dictsorted:
        count = 0
        while temp_budget >= resmenu_dict[item]: #'=>' to meet the budget
            if temp_budget  > 0:
                temp_budget = temp_budget - resmenu_dict[item]
                count = count + 1
                recomm_dict[item] = count
            else:
                count = 0
                
    print("**RECOMMENDATION**")
    for item in recomm_dict:
         print (item, "x", recomm_dict[item] )
    print("")
    print("Total Spending: $", "%.2f" % float(budget2 - temp_budget))


'''
MAIN 

'''

def main():
    if (os.path.isfile('./input.txt')): 
        file = open("recommendation.txt", "w+")
        menu_dict = {}
        with open("input.txt") as openput:
            temp_budget = open("input.txt").readline().rstrip()
            budget = float(temp_budget)
            with contextlib.redirect_stdout(file): 
                CheckBudg(budget)
            
            for line in islice(openput, 1, None):
                key, *_, value = line.split("*")  
                menu_dict[key.strip()] = float(value.strip())
            
            with contextlib.redirect_stdout(file): 
                Recommendation(menu_dict, budget)
        file.close()
        
    
    

if __name__ == '__main__':
    main()