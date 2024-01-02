#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:09:57 2022

@author: jenniferolguingaray
"""

 # Output: Most Economical Desired 
# *Choose the design that will give you the highest profit (revenue-cost) 

# Three Designs 
# - Flat Solar Panels 
# - Mechanized Solar Panels 
# - Solar Collector Field 

# Useful Information 
# Initial Cost 
# Annual Operating Cost 
# Benefits // Revenue 
# Current Interest Rate: 10% 
# Time: 20 Years 
# Inputs: Interest Rate and Year 
# Ask User to Input Initial Costs 
# - Return CURRENT (present*) values of the Overall Profit 
# - Present value of money = Future value of money *(1+interest rate)^(-number of years)


# Design 1: Flat Solar Panels
# *Field if “Flat” Solar Panels angled best to catch the sun. 
# *Yield: 2.6MW
	#Implementing Cost - $87 Million 
	#Operating Cost // Year 1 - $2 Million
	#Grow $250,000 Annually
	#Operating Cost // Year 2 - $2,250,000
	#Revenue // Year 1 - $6.9 Million 
	#Revenue {Increase 8%} Each Year After. 
    
def Flat(interestrate,year):
    initial_costs=input("Enter the Initial Costs for Flat: ")
    profit = -float(initial_costs)
    #Current Year Cost 
    cost = 0
    #Annual Electricty Production in the First Year
    produce = 0
    
    for i in range(1,year+1):
        if i == 1:
            produce=6900000
            cost +=2000000
            totalprofit=(produce-cost)
        else:
            produce *=(1+0.08)
            cost +=250000
            totalprofit=(produce-cost)
        profit=profit+totalprofit*((1+interestrate)**(-i))
    return profit 


# Design 2: Mechanized Solar Panels 
# *Field of Mechanized Solar Panels rotate side to side so that they are always positioned parallel to the sun’s rays, maximizing the production of electricity. 
# *Yield: 3.1 MW 
	#Implementing Cost - $101 Million 
	#Operating Cost // Year 1 - $2.3 Million 
	#Grow $300,000 Annually 
	#Operating Cost // Year 2 - $2,500,000
	#Revenue // Year 1 - $8.8 Million
	#Revenue {Increase 8%} Each Year After. 

def Mechanized(interestrate,year):
    initial_costs=input("Enter the Initial Costs for Mechanized: ")
    profit = -float(initial_costs)
    #Current Year Cost 
    cost = 0
    #Annual Electricty Production in the First Year
    produce = 0
    
    for i in range(1,year+1):
        if i == 1:
            produce=8800000
            cost +=2300000
            totalprofit=(produce-cost)
        else:
            produce*=(1+0.08)
            cost+=300000
            totalprofit=(produce-cost)
        profit=profit+totalprofit*((1+interestrate)**(-i))
    return profit

# Design 3: Solar Collector Field 
# *Field of Mirrors to focus the sun’s rays onto a boiler mounted in a tower. 
# *Yield: 3.3 MW 
    #Implementing Cost = $91 Million
    #Operating Cost // Year 1 - $3 Million
    #Grow $350,000 Annually
    #Operating Cost // Year 2 - $3,3500,000
    #Revenue // Year 1 - $9.7 Million 
    #Revenue {8%} Each Year 

def Collector(interestrate,year):
    initial_costs = input("Enter the Initial Costs for Collector: ")
    profit = -float(initial_costs)
    #Current Year Cost
    cost = 0  
    #Annual Electrcity Production in the First Year
    produce = 0 

    for i in range(1,year+1):
        if i == 1:
            produce=9700000
            cost+=3000000  
            totalprofit =(produce-cost)
        else:
            produce*=(1+0.08)
            cost+=350000
            totalprofit=(produce-cost)
        profit=profit+totalprofit*((1+interestrate)**(-i))
    return profit

def main():
    while True:
        interestrate = float(input("Interest Rate: "))
        year = int(input("Year: "))
        flatprofit = Flat(interestrate, year)
        mechanizedprofit = Mechanized(interestrate,year)
        collectorprofit = Collector(interestrate,year)
        print(f'Flat Profit={flatprofit}')
        print(f'Mechanized Profit={mechanizedprofit}')
        print(f'Collector Profit={collectorprofit}')
        maxprofit = max(flatprofit,mechanizedprofit,collectorprofit)
        if flatprofit == maxprofit:
            bestdesign = 'Flat'
        elif mechanizedprofit == maxprofit:
            bestdesign = 'Mechanized'
        else:
            bestdesign = 'Collector'
        print(f'Max Profit={bestdesign}, {maxprofit}')

if __name__ == '__main__':
    main()

    










