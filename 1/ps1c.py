# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:28:16 2021

@author: MirunaConstantin
"""

print ("Enter the starting salary:")
annual_salary = float ( input() )
semi_annual_raise = 0.7
total_cost = 1000000
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
months = 36
k = 0
monthly_salary = annual_salary / 12.0
while portion_down_payment * total_cost > current_savings :
    current_savings +=  monthly_salary * portion_saved
    current_savings += current_savings * r /12
    months = months + 1
    if months % 6 == 0 :
        monthly_salary += monthly_salary * semi_annual_raise
print( "Best saving rate:", portion_saved)
print( "Steps in bisection search:", k)
