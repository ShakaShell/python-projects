# Michael Roberts
# Section 11
# On my honor, I have neither received nor given any unauthorized assistance on this assignment.

import math


# Step One: Get input from user
weight_lbs = input("Enter your body weight in lbs: ")
height_inches = input("Enter your height in inches: ")
age_years = input("Enter your age: ")
activity_level = input("Enter your activity level (LOW or HIGH): ")
gender = input("Enter your gender (Male or Female): ")

weight_lbs = float(weight_lbs)
height_inches = float(height_inches)
age_years = int(age_years)
activity_level = str(activity_level)
gender = str(gender)


# Step 2: Conversion Functions
# this shouldn't be an issue with incorrect BMR - as conversions are what they should be.
def lb_kg_conversion(weight_lbs):
    weight_kg = float(weight_lbs * .453592)
    return weight_kg

def in_cm_conversion(height_inches):
    height_cm = float(height_inches * 2.54)
    return height_cm

weight_kg = lb_kg_conversion(weight_lbs)
height_cm = in_cm_conversion(height_inches)


# Step 3: Calculating BMR

def bmr_calc (weight_kg, height_cm, age_years, activity_level, gender):
    if gender == "Male":
        BMR_beforeActivity = (10 * weight_kg) + (6.25 * height_cm) - (5 * age_years) + 5
    elif gender == "Female": 
        BMR_beforeActivity = (10 * weight_kg + (6.25 * height_cm) - (5 * age_years) - 161)
    else:
        print("Error. Please input 'Male' or 'Female' for gender.")

    if activity_level == "LOW":
        BMR = BMR_beforeActivity * 1.4
        BMR = float(BMR)
    elif activity_level == "HIGH":
        BMR = BMR_beforeActivity * 1.8
        BMR = float(BMR)
    else:
        BMR = "unable to be provided due to inaccurate activity level. Please use LOW or HIGH activity level to determine your"

    return BMR

BMR = bmr_calc(weight_kg, height_cm, age_years, activity_level, gender)
print("Your current BMR is ", bmr_calc(weight_kg, height_cm, age_years, activity_level, gender), "calories.")
        
# Step 4: Calories consumed

num_days_data = int(input("Enter the number of days you will input data for: "))

def totalCalories(num_days):
    totalCals = 0 
    for i in range(int(num_days)):
        print("Day", (i+1), "Information:")
        breakfast = int(input("How many calories did you consume for breakfast?: "))
        totalCals = totalCals + breakfast
        lunch = int(input("How many calories did you consume for lunch?: "))
        totalCals = totalCals + lunch
        dinner = int(input("How many calories did you consume for dinner?: "))
        totalCals = totalCals + dinner
    return totalCals

total_calories = totalCalories(num_days_data)

print("The total number of calories consumed in ", num_days_data, "days is", total_calories, "calories.")

# Step 5: Weight Change

def weightchange(BMR, totalCals, num_days):
    total_BMR = BMR * num_days
    BMR_less_Cals = total_BMR - totalCals
    total_lbs = (BMR_less_Cals / 3500)
    total_lbs = math.floor(total_lbs * 100)
    total_lbs = (total_lbs / 100)
    return total_lbs

print("Your weight change is: ", weightchange(BMR, total_calories, num_days_data), "lbs.")

    











# print(weight_conversion, height_conversion)



