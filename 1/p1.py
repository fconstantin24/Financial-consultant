# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 12:12:40 2021

@author: MirunaConstantin
"""
print ("Enter your annual salary:")
annual_salary = float ( input() )
print ("Enter the percent of your salary to save, as a decimal:")
portion_saved = float ( input() )
print ("Enter the cost of your dream home:")
total_cost = float ( input() )
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
months = 0
monthly_salary = annual_salary / 12.0
while portion_down_payment * total_cost > current_savings :
    
    current_savings +=  monthly_salary * portion_saved
    current_savings += current_savings * r /12
    months = months + 1
    print(months)
print( "Number of months:", int (months))