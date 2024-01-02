#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:43:22 2022

@author: jenniferolguingaray
"""
# ISE Mini Project #2 

# I decided to use pandas for my project
# I am using the combinations function in order to be able to make combinations of the all of the factories to find the minimum cost. 
import pandas as pd 
from itertools import combinations 


# Creating Columns inorder to format all of the data given. 
columnHeadings = ["Factory Number", "Cost $M", "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9", "N10"]

# Opening the text file and creating both a DataFrame and a dictionary for the information within the file. 
data = pd.read_csv("/Users/jenniferolguingaray/Downloads/ProjectData1.txt", names=columnHeadings)
data = pd.DataFrame(data)

combo_dict={}

# Creating a loop to test all of the possible combinationed in a given combination. 
for i in range(1,11):
    # Setting the line below =x so that within each iteration of the loop in which I am creating rhe combinations I am able to do it based on i. 
    x=list(combinations(data["Factory Number"], i))
    # Creating a secondary DataFrame so that I am able to remove already used rows within the combinations, that way I am able to accrautely ensure that all neighboords are accounted for. 
    for combo in x: 
        comboData = data[data["Factory Number"].isin(list(combo))]
        # Covering will make sure that all neighboorhoods are represented 
        covering=[]
        # Checking to see if Neighboord 1 is accoutned for 
        if sum(comboData["N1"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Checking to see if Neighboord 2 is accoutned for 
        if sum(comboData["N2"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Checking to see if Neighboord 3 is accoutned for 
        if sum(comboData["N3"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Checking to see if Neighboord 4 is accoutned for 
        if sum(comboData["N4"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Checking to see if Neighboord 5 is accoutned for 
        if sum(comboData["N5"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Checking to see if Neighboord 6 is accoutned for 
        if sum(comboData["N6"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Checking to see if Neighboord 7 is accoutned for 
        if sum(comboData["N7"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Checking to see if Neighboord 8 is accoutned for 
        if sum(comboData["N8"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Checking to see if Neighboord 9 is accoutned for 
        if sum(comboData["N9"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Checking to see if Neighboord 10 is accoutned for 
        if sum(comboData["N10"])>=1:
        # Appending if it represented 
            covering.append([0])
        # Counting the items that are being incldued in the coverage of the data. 
        if len(covering)==10:
        # Print statement of the combination data. 
            print(comboData)
        # Printing the total number of factories witin the list. 
            print(list(comboData["Factory Number"]))
        # Printing the minimum cost within each of the combinations made.    
            print(sum(comboData["Cost $M"]))
        # Being given the minimum costs overall. 
            key=sum(comboData["Cost $M"])
        # Being given the list of the factory combinations overall. 
            combo_dict[key]=list(comboData["Factory Number"])
            
#Formatting the Solutions so that we are given the Minimum Cost $M and the Factory Combinations.            
FinalDecision = pd.DataFrame(combo_dict.items(), columns = ["Minimum Cost $M", "Factory Combinations"])
#Sorting the values so that they are from the smallest to the greatest.
FinalDecision = FinalDecision.sort_values(by="Minimum Cost $M", ascending=True)
#Printing the Final Decision 
print(FinalDecision)