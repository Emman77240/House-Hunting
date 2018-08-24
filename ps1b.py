# -*coding: utf-8 -*-
"""
Created on Tue Aug  7 14:05:05 2018

@author: Emman240
"""
#I worked with MMK on this exercise


annual_salary = float(input("Enter your starting annual salary :  "))
percentage_saved = float(input("Enter the percent of your salary saved as a decimal :  "))
total_house_cost = float(input("Enter the cost of your dream home :  "))
semi_annual_raise = float(input("Enter the semi annual raise as a decimal :  "))
current_savings = float(0)
month = 0
monthly_salary = float(annual_salary / 12)
portion_saved = float(percentage_saved * monthly_salary)
down_payment = float(total_house_cost * 0.25)
rate_of_return = 0.04

while (current_savings < down_payment):
    
    if (month == 0):
        current_savings += portion_saved
    else :
        if(month % 6 == 0) :
            monthly_salary += (semi_annual_raise * monthly_salary)
            portion_saved = float(percentage_saved * monthly_salary)
            current_savings += portion_saved + (current_savings * rate_of_return)/12
            
        else :
            current_savings += portion_saved + (current_savings * rate_of_return)/12
    
    month += 1
    
    
print (month)

