#Michael Roberts
#Section 11
#On my honor, I have neither received nor given any unauthorized assistance on this assignment.

import math
AnnualSalary = float(input("Enter your annual salary: $"))

AnnualTakeHomePay = AnnualSalary - (AnnualSalary * .3)

MonthlyTakeHomePay = math.ceil(AnnualTakeHomePay / 12)

print("Your monthly take home pay is: $", MonthlyTakeHomePay)

creditcardAnnual = float(input("Enter your annual credit card fee expense: $"))
autoRegAnnual = float(input("Enter your annual scheduled car maintenance expense: $"))
streamingMonthly = float(input("Enter your monthly streaming platform expense: $"))
phoneMonthly = float(input("Enter your monthly phone plan expense: $"))
nicotineWeekly = float(input("Enter your weekly nicotine expense: $"))
transportWeekly = float(input("Enter your weekly transportation expense: $"))
dineoutWeekly = float(input("Enter your weekly dining out expense: $"))

totalMonthlyExpenses = (streamingMonthly + phoneMonthly + (creditcardAnnual / 12) + (autoRegAnnual / 12) + (nicotineWeekly * 4) + (transportWeekly * 4) + (dineoutWeekly * 4))

print("Your monthly expenses add up to: $",math.ceil(totalMonthlyExpenses))

portionTakeHome = (totalMonthlyExpenses / MonthlyTakeHomePay)
moneyLeft = math.ceil(MonthlyTakeHomePay - totalMonthlyExpenses)

print("You spend ", math.ceil(portionTakeHome * 100), "% of your monthly takehome pay.")

print("You have $",(moneyLeft)," after your expenses.")















