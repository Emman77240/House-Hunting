# -*coding: utf-8 -*-
"""
Created on Tue Aug  7 14:05:05 2018

@author: Emman240
"""
#I worked with MMK on this exercise

annual_salary = float(input("Enter your starting annual salary :  "))
percentage_saved = float(input("Enter the percent of your salary saved as a decimal :  "))
total_house_cost = float(input("Enter the cost of your dream home :  "))
current_savings = float(0)
number_of_months = 0
monthly_salary = float(annual_salary / 12)
portion_saved = float(percentage_saved * monthly_salary)
down_payment = float(total_house_cost * 0.25)
rate_of_return = 0.04

while (current_savings <= down_payment):
    
    if (number_of_months == 0):current_savings += portion_saved
    else : current_savings += portion_saved + (current_savings * rate_of_return)/12
    
    number_of_months += 1
    
    
    
print (number_of_months)

