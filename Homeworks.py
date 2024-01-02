#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:21:32 2022

@author: jenniferolguingaray
"""

# Homework 1
#%% Question 2 (2.5 pts):
# The following steps calculate a company’s profit. Write a program that has one line of code for each step.
    #a.	Create the variable revenue and assign it the value 98,456.
Revenue = 98456 
    
    #b.	Create the variable costs and assign it the value 45,000.
Costs = 45000
   
     #c.	Create the variable profit and assign it the difference between the values of the variables revenue and costs.
Profit = (Revenue - Costs)
   
     #d.	Display the value of the variable profit.
print(Profit)

#%% Question 3 (2.5 pts):
# population of the United States was about 281 million in 2000 and is 
# predicted to be about 404 million in 2050. Approximate the percentage population growth in the 
# United States during the first half of the 21st century. Round the percentage to the nearest whole number.

USPopulationin2000 = 281000000

USPopulationin2050 = 404000000

IncreaseofUSPop = (USPopulationin2050 - USPopulationin2000)
print(IncreaseofUSPop)

PercentageofIncrease = ((IncreaseofUSPop / USPopulationin2000) * 100) 

print("PercentageofIncrease:" + str(round(PercentageofIncrease)) + '%')


# Homework 2 
#%% Question 2 
#Calculate the amount of a server's tip, given the amount of the bill and the 
#percentage tip as input. 
print("Enter amount of bill: ")
bill = float(input())
tip = ((bill*18)/100)
print("Enter percentage tip: " , tip)
print("Tip: " , bill*0.18)

#%% Question 3 
#Common misconcpetion is that if you recieve three successive 5% pay raises, 
#then your original slalary will have increased by 15% 
#Request a salary as input and then display the salary after recieveing three
#successive 5% pay raises. 
print("Enter beginning salary: ")
salary =int(input())
firstsuccessivepay = ((salary*0.05)+salary)
secondsuccessivepay = ((firstsuccessivepay*0.05)+firstsuccessivepay)
thirdsuccessivepay = ((secondsuccessivepay*0.05)+secondsuccessivepay)
print("New salary: " , thirdsuccessivepay)

salarydifference = (thirdsuccessivepay-salary)
salarychange = ((salarydifference/salary)*100)
print("Change: " , salarychange)

#%% Question 4
#Lenght Conversion: Write a program to convert U.S. Customary System lenght 
#into a Metric System lenght 
print("Enter number of miles: " )
miles = float(input())
print("Enter number of yards: " )
yards = float(input())
print("Enter number of feet: " )
feet = float(input())
print("Enter number of inches" )
inches = float(input())
totalinches = ((63360 * miles)+(36 * yards)+(12 * feet)+(inches))
totalmeters = (totalinches / 39.37)
totalkilometers = int(totalmeters / 1000)
#Problem with the meters
meters = int(totalmeters % 1000)
centimeters = int((totalmeters * 100) % 100)
print("Metric lenght")
print("kilometers: " , totalkilometers)
print("meters: " , meters)
print("centimeters: " , centimeters)


# Homework 3
#%% Question 1 
#Ask for first students's inputs: ask name, last name, and grade separately 
name1=input("Enter first student's name: ")
lastname1=input("Enter first student's last name: ")
grade1=input("Enter first stduent's grade: ")

#Ask for second student's inputs: ask name, last name, and grade separately
name2= input("Enter second student's name: ")
lastname2=input("Enter second student's last name: ")
grade2=input("Enter second student's grade:  ")

#Give 15 spaces for left-justified "Name", 10 spaces for left-justfiied "Last Name", and 5 spaces for right-justfiied "Grade". 
#Print your inputs properly.
print("Name" .ljust(15), "Last Name" .ljust(10), "Grade" .rjust(5) , sep="")
print("{0:<15s}{1:<10s}{2:<5s}" .format(name1, lastname1, grade1))
print("{0:<15s}{1:<10s}{2:<5s}" .format(name2, lastname2, grade2))

#%% Question 2 
#Write a script to reverse the order of the characters in a given sentence entered by the user. 
sentence=input("Enter a setence: ")
print("The reverse version of your sentence is: ", " " .join(reversed(sentence.split())))

#%% Question 3
#Ask user to enter a list containing a mix of intergers and float values. 
#Find the sum, min, max of values within the list. 
#Delete the minimum value in the original list to create a new list, but make sure the original list remains unchanged. 
numbers = eval(input("Enter a list: "))
list1 = list(numbers)
print("max: ", max(list1))
print("min: ", min(list1))
print("sum: ", sum(list1))
print("The original list:", list1)

list2=list1[:]
list2.remove(min(list2))
print("The new list: ", list2)

#%% Question 4 
revenue1=eval(input("Enter the revenue in the first quarter: "))
expenses1=eval(input("Enter the expenses in the first quarter: "))

revenue2=eval(input("Enter the revenue in the second quarter: "))
expenses2=eval(input("Enter the expenses in the second quarter: "))

revenue3=eval(input("Enter the revenue in the third quarter: "))
expenses3=eval(input("Enter the expenses in the third quarter: "))

revenue4=eval(input("Enter the revenue in the fourth quarter: "))
expenses4=eval(input("Enter the expenses in the fourth quarter: "))

dataList= [[revenue1,expenses1],[revenue2,expenses2],[revenue3,expenses3],[revenue4,expenses4]]
print(dataList)

totalrevenue=revenue1+revenue2+revenue3+revenue4 
totalexpenses=expenses1+expenses2+expenses3+expenses4
profit=totalrevenue-totalexpenses
print("The total revenues are " "${:,.2f}".format(totalrevenue),"and the total expenses are " "${:,.2f}".format(totalexpenses),"Your profit is " "${:,.2f}".format(profit))

# Homework 4
#%% Question 1 
wage=float(input("Enter hourly wage: "))
hours=float(input("Enter number of hours worked: "))
if hours <=40:
    grossPay=wage*hours
else:
    grossPay=(wage*40)+(1.5*wage*(hours-40))
print("Gross pay for week is ${0:.2f}.".format(grossPay))

#%% Question 2
#How many years are required for 100 grams of strontium-90 to decay to less than 1 gram. 
mass=100
year=0
while(mass>1):
    mass/=2
    year+=28
print("The decay time is", year, "years.")

#%% Question 3 
#Asking the deposit amount, the target value at the end of the whole period, and interest rate 
#Calculate how many years and months are needed to reach the target amount. 
deposit=eval(input("How much money will you deposit at the end of each month?: "))
target=eval(input("How much money do you want at the end?: "))
rate=eval(input("Enter the interest rate per year (ex:0.06): "))
balance=0
months=0
while balance<=target:
    balance=((1+rate/12)*balance)+deposit
    months+=1
years=months//12
months=months%12
print("Annuity will be worth ${0:n} after {1:n} years and {2:n} months.".format(target,years,months))

#%% Quesion 4 
#Asks the user for the PIN no more than three times, and does the following 
#a.If the user enters the right number, print a message saying, "Your PIN is correct" & end the program.
#b.If the user enters the wrong number, print a message saying "Ypur PIN is incorrect"ask for it again 
#c.If the user enters a wrong number three times, print a message sayiing, "Your bank card is blocked" & end the program. 
originalPin="1234"
pin=input("Enter your PIN: ")
if pin==originalPin: 
    print("Your PIN is correct")
else:
    print("Your PIN is incorrect")
    pin=input("Enter your PIN:")
    if pin==originalPin:
        print("Your PIN is correct:")
    else: 
        print("Your PIN is incorrect")
        pin=input("Enter your PIN: ")
        if pin==originalPin:
            print("Your PIN is correct")
        else: 
            print("Your PIN is incorrect")
            print("Your bank card is blocked")
            

# Homework 5 
#%% Question 1 
# Write a program finding min, max, average of user inputs. 
# (thousands separator, 2-decimal points)
List=[]
while True: 
    try: 
        number = input("Enter a number: ")
        if number == "DONE": 
            break
        new = int(number)
        List.append(new)
    except:
        print("Invalid input")
print("Minimum: ""{:,.2f}".format(min(List)))
print("Maximum: ""{:,.2f}".format(max(List)))
print("Average: ""{:,.2f}".format(sum(List)/len(List)))

#%% Question 2 
# Credit Card Remove Spaces and Dashes 
userInput=input("Enter a credit card number: ")
creditCard = ""
for char in userInput:
    if char != " " and char != "-": 
        creditCard = creditCard+char
#%% Question 3 
# Replace a word in a given sentence with another one. 
originalsentence=input("Enter a sentence: ")
word=input("Enter a word from the sentence you entered: " ) 
newword=input("Enter the new word: ")
sentenceList=originalsentence.split(" ")   
for i in range(len(sentenceList)): 
    if sentenceList[i]==word:
        sentenceList[i]==newword
        break
print(" ".join(sentenceList))
#%% Question 4
# A run is a sequence of adjacent repeated values. 
# Write a cord for computing the lenght of the longest run and print it. 
numbers=input("Enter a sequence of numbers: ")
count = 0
i = 0
max = 0
previous = numbers[0]
while True: 
    if numbers[i]==previous:
        count +=1
    else:
        count = 1
        if count>max:
            max=count
            previous=numbers[i]
            i+=1
            if i==len(numbers):
                break
print("Longest run's lenght is", max)


# Homework 6
#%% Question 1 
constant = 8.314
def main():
    pressure,moles,temp = computegasvolume()
    volume = calculateVolume(pressure,moles,temp)
    display(volume)
    
def computegasvolume():
        pressure=eval(input("Enter Pressure: "))
        moles=eval(input("Enter Moles: "))
        temp=eval(input("Enter Temperature: "))
        
        return pressure, moles, temp

def calculateVolume(pressure,moles,temp):
    volume=(moles*constant*temp)/pressure
    return volume 
def display(volume):
    print("Gas Volume: {0:.2f} cubic meters.".format(round(volume,2)))
    
main()

#%% Question 2 
def ave(list1):
    mean=round((sum(list1))/(len(list1)),2)
    return mean 

def SD(list1):
    mean=round((sum(list1))/(len(list1)),2)
    var=sum((x-mean)**2 for x in list1)/len(list1)
    SD=round((var**.5),2)
    return SD 

list1=[75, 84, 66, 99, 51, 65]

print("Average Score: ", ave(list1))
print("Standard Deviation: ", SD(list1))

#%% Question 3 
def main():
    string=input("Enter a String: ")
    subString=input("Enter the substring you want tot check: ")
    string1=string.lower()
    subString1=subString.lower()
    if find(string1, subString1):
        print("The String '", string, "; contains", subString)
    else: 
        print("The String '", string, "' does NOT contain", subString)
        
def find(string, match):
    if string.startswitch(match)==True: 
        return True 
    elif len(string) >= len(match):
        return find(string[1:len(string)], match)
    else: 
        return False 
main() 

#%% Question 4
def main():
    password=input("Enter a password: ")
    passwordConfirmation=input("Re-enter your password: ") 
    x=ValidPassword(password)
    
    while password!=passwordConfirmation or not x:
        print("That password is not valid.")
        password=input("Enter a password: ")
        passwordConfirmation=input("Re-enter your password: ")
        x=passwordConfirmation(password)
        if x:
            print("That is a valid password.")

def ValidPassword(password): 
    if len(password)<8: 
        return False 
    digit=False
    upper=False 
    lower=False 
    for ch in password: 
        if ch>="0" and ch<="9": 
            digit=True 
        if ch>="A" and ch<="Z":
            upper=True 
        if ch>="a" and ch<="z": 
            lower=True 
    return digit and upper and lower 

main() 

# Homework 7
#%% Question 1 
# Dr.Ozaltin's Offer for HW 
offer = input('"Accept" or "Reject" Dr.Ozaltin offer to evaluate ISE 135 and its instructor for a chance to have the lowest graded homework dropped if at least 90% of the student that takes the course fill out the evaluation: ')
if offer == "Accept":
    print("Go to http://go.ncsu.edu/cesurvey and evaluate her, thanks for your contribution.")
else:
    print("☹ It does not take too long, we should reach 90% participation!")
    
#%% Question 2 
import pandas as pd 
import seaborn as sns


# A. What is the correlation between Cholesterol and Heart Disease? 
data=pd.read_csv("/Users/jenniferolguingaray/Downloads/heart.csv")
correlation=data["Cholesterol"].corr(data["HeartDisease"])
print (correlation)

# B. Group the Cholesterol Column as & How Many Patients Exist in Each Group 
data["Cholesterol Group"]=pd.cut(data["Cholesterol"],[-1,1,200,350,610],labels=["No_Ch","Opt_Ch","High_Ch","VeryH_Ch"])
print(data.groupby(["Cholesterol Group"]).size())

# C. Plot the Number of Patients with and without Heart Disease in Each Cholesterol Group 
sns.countplot(x="Cholesterol Group", hue="HeartDisease", data=data)

# D. Find the Following Ratio's 
df=data[(data.HeartDisease==1)]
df["CholesterolGroup"]=pd.cut(df["Cholesterol"],[-1,1,200,350,610],labels=["No_Ch","Opt_Ch","High_Ch","VeryH_Ch"])

print((df.groupby(["Cholesterol Group"]).size())/(df.groupby(["Cholesterol Group"]).size()))

# E. Calculate the Female and Male Patients's Cholesterol Average
print(data.groupby(["Sex"])["Cholesterol"].mean()) 

# F. Plot the # of Patients with and without Heart Disease in Males and Females 
sns.countplot(x="Sex", hue="HeartDisease", data=data)

# G. Sort the Data with Respect to "Age" low to high and Draw a Line Plot with X-Axis as Age and Y-Axis as "Cholesterol"
import matplotlab as plt
data=data.sort_values(by="Age", ascending=True)#data.groupby("Age").Cholesterol.mean().plot.line(x="Age", y="Cholesterol")

plt.scatter(data["Age"],data["Cholesterol"], color = 'g', s = 1 )

# H.Calculate Average Cholesterol and Heart Disesase in Each Group 
data["Age Group"]=pd.cut(data["Age"],[25,40,65,90],labels=["YoungerAdults","OlderAdults","Seniors"])

print(data.groupby(["Age Group"])[["Cholesterol", "HeartDisease"]].mean().sort_values(by="HeartDisease",ascending=False))

# I. Plot the Average Cholesterol in each Age Group 
data.groupby(["Age Group"])["Cholesterol"].mean().plot.bar()

# J. Find the Following Values: 
    # How many patients have greater than 120 RestingBP and Greater than 150 MaxHR? 
print((data.query('RestingBP > 120 and MaxHR > 150'))["Age"].size)
    
# How many patients have both heart disease and "Flat" ST slope? 
print((data.query('HeartDisese == 1 and ST_Slope == "Flat"'))["Age"].size)
    
    # What percentage of patients with heart disease have "Flat" ST Slope? 
print((data.query('HeartDisease == 1 and St_Slope =="Flat"'))["Age"].size/((data.query('HeartDisease'))))
    
    # What percenatge of patients with ExerciseAngina have heart disease? 
numExerciseAnhinaTotal=(data.query('ExerciseAngina == "Y"'))["Age"].size

    # What percentage of patients without ExerciseAngina have Heart Disease? 
numExerciseAnginaHD=(data.query('ExerciseAngina == "Y" and HeartDisease == 1'))["Age"].size









