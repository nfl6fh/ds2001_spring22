#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 14:31:18 2022

@author: nathanlindley (nfl6fh)
"""

print('1.')

gradebook = {}

gradebook["Jon"] = 95
gradebook["Mike"] = 84
gradebook["Jaime"] = 99

print(gradebook)
print()

print('2.')

print(gradebook["Jon"])
print()

print('3.')

print('print(gradebook["Jeff"])')
print('KeyError: \'Jeff\'')
print()

print('4.')

names = ['Alex','Patrick','Tom','Joe','Alex']
print(names)
print()

print('5.')

names.sort()
print(names)
print()

print('6.')

namesSet = {'Alex','Patrick','Tom','Joe','Alex'}
print(namesSet)
print()

print('7a.')

td = [2,4,1,3,1]
print(td)
print()

print('7b.')

tdOdd = [x for x in td if (x%2) != 0]
print(tdOdd)
print()

print('7c')

tdGreater = [y for y in td if y > 1]
print(tdGreater)
print()