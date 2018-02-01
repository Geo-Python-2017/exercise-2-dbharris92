# -*- coding: utf-8 -*-
"""
Description:
    A script to print average monthly temperatures (C) 
    from Helsinki Malmi airport
Created on Thu Feb  1 11:42:07 2018

@author: Drew Harris
"""
###list months and temperatures
month = ['January', 'Februay', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [-3.5, -4.5, -1.0, 4.0, 10.0, 15.0, 18.0, 16.0, 11.5, 6.0, 2.0, -1.5]

###Enter selected month below
selectMonth = 'March'
###Enter selected month above

###Find Month
monthIndex = month.index(selectMonth)

###Find corresponding temp
tempIndex = temperature[monthIndex]



###Print month and average temperature
print('The average temperature in Helsinki in', selectMonth, 'is', tempIndex, '.')