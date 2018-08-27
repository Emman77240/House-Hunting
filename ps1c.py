# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 12:03:53 2018

@author: Emman240
"""






# Set the default values.

semi_annual_raise = 0.07
rate_of_return = 0.04
r = rate_of_return/12
total_house_cost = 1000000
percentage_down_payment = 0.25
down_payment = percentage_down_payment * total_house_cost
current_savings = 0
month_limit = 36
savings_rate = 0.50


# Counters

month_counter = 0
step_counter = 1


min = 0
max = 10000
current_salary = int(input("Enter your current salary: "))
present_salary = current_salary

def compute_rate(lower, upper):
    global current_savings, current_salary, month_counter, max, min, step_counter, savings_rate


    
    while (current_savings < down_payment):
        savings_rate = ((upper+lower)/2)/10000
        monthly_salary = current_salary/12
        monthly_return = current_savings * r
        monthly_contribution = monthly_salary * savings_rate
        current_savings = current_savings + monthly_contribution + monthly_return
        
        month_counter += 1
        
        if month_counter % 6 == 0:
            current_salary = current_salary + (current_salary * semi_annual_raise)
            
      
    
    if month_counter > month_limit:
        
        month_counter = 0
        current_savings = 0
        current_salary = present_salary
        step_counter += 1
        min = savings_rate * 10000
        compute_rate(min, max)
        
    
    elif month_counter < month_limit:
        month_counter = 0
        current_savings = 0
        current_salary = present_salary
        step_counter += 1
        max = savings_rate * 10000
        compute_rate(min, max)
        
        
    elif current_savings > down_payment + 100:
        month_counter = 0
        current_savings = 0
        current_salary = present_salary
        step_counter += 1
        max = (savings_rate * 10000)-1
        compute_rate(min, max)
        
        
    elif current_savings < down_payment - 100:
        month_counter = 0
        current_savings = 0
        current_salary = present_salary
        step_counter += 1
        max = (savings_rate * 10000)+1
        compute_rate(min, max)
        
        

compute_rate(min, max)
print('Rate: ', savings_rate)
print('Steps in bisection search: ', step_counter)
