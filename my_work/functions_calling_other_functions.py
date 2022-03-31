#!/usr/bin/env python
# coding: utf-8

# # Functions Calling Other Functions
# 
# ### University of Virginia
# ### Programming for Data Science
# ### Last Updated: April 5, 2021

# ### CONCEPTS
# 
# - functions
# - functions calling other functions
# 
# ---

# Calling a function from the "math" library is straightforward:
# 
# 1) import the math library (a class) using:  import math
# 
# 2) call methods using "dot" notation, that is, <name of the library>.<name of the method>(any parameters), such as:  math.sqrt(12)

# In[ ]:


## Importing math functions
import math # Typically best to put this line of code at the TOP of the file
print(math.sqrt(12)) # using the square-root function from the math library

print(math.floor(2.5)) # returns largest whole number less than the argument
print(math.floor(2.9))
print(math.floor(2.1))

# Literature will give a full list of all mathematical functions


# Here's an example using the random library (a class).
# 
# 1) import the random library using: import random
# 
# 2) use the random() function in the random library to generate a random number

# In[ ]:


## Importing Random - for random number generation
import random # Typically best to put this line of code at the TOP of the file
print(random.random()) # using random() function in random library
    # will return a number between 0 and 1
                       
print(random.randint(1,100)) # specify a range in the parenthesis
    # this will return a random integer in the range 1-100


# ### Functions - definition and benefits

# Definition:  
# A piece of source code, separate fom the larger program, that performs  
# a specific task. This section of code is given a name and can be called  
# from the main/larger program. It is called by using its given name
# 
# -- Reasons to use functions:  
# 1. reduce complex tasks into simpler tasks  
# 2. eliminate  duplicate code (no need to re-write, reuse function as needed)  
# 3. code reuse (once function is written, can reuse it in any other program)  
# 4. distribute tasks to multiple programmers (each function written by someone)  
# 5. hide implementation details - abstraction  
#    (increase readability, increase maintenance and quality)  
# 6. improves debugging by improving traceability  
#    (easier to follow - jump from function to function)
# 
# ====================================================================  
# 
# -- Example of a function  
# use the key word "def" - for "definition"  
# 
# Format:  
# ```
# def functionName(parameters):  
#     statements (indented) [return used]
#     ```
#     
# **Function Examples**

# In[2]:


def square(number):
    return number * number  # square a number
    
def addTen(number):
    return number + 10  # Add 10 to the number   
    
def numVowels(string):
    string = string.lower()  # convert user input to lowercase
    count = 0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or            string[i] == "i" or string[i] == "o" or            string[i] == "u":
           count += 1 # increment count
    return count


# ### TRY FOR YOURSELF
# 
# The cells below call the defined functions. Run the cells to try them out.

# In[3]:


# Usage:
num = int(input("Enter a number to square: "))
numSquared = square(num)  # calling the square function with num as parameter
plusten = addTen(num)  # calling the addTen function
print(str(num) + " squared is: " + str(numSquared))
print(str(num) + " plus 10 is: " + str(plusten))


# In[4]:


strng = input("Enter a string: ")
print("There are " + str(numVowels(strng)) + " vowels in the string.")


# ### Functions Calling Other Functions

# #### EXAMPLE: Using a conversion program to convert degrees F to degrees C and vice versa

# In[5]:


def ftoc(temp):  # *F to *C
    return (temp-32.0) * (5.0/9.0)
    
def ctof(temp):  # *C to *F
    return temp * (9.0/5.0) + 32.0
    
def convert(temp, toTemp):  # Two parameters
    # No problem to call another function in the body of a function
    if toTemp.lower() == "c":
        return ftoc(temp)  # function call to ftoc
    else:
        return ctof(temp)  # function call to ctof
    

temp = int(input("Enter a temperature: "))                
scale = input("Enter the scale to convert to: (c or f) ")
if (scale == 'c'):
    currentScale = 'f'
else:
    currentScale = 'c'

converted = convert(temp, scale)
print(temp, currentScale, "converted becomes:" ,converted, scale)


# #### EXAMPLE: Counting the number of vowels

# In[6]:


# Predicate functions - often used as helper functions that return True or False

def isVowel(l):
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        return True  # if the letter is a vowel, return True
    else:
        return False # else, return False
        
def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):  # for each character
        if isVowel(string[i]):  # calling function above
            count += 1  # increment count
    return count
    
    
theStrng = input("Enter a string: ")
print("There are " + str(numVowels(theStrng)) + " vowels in the string.")


# #### EXAMPLE: Calculating tax on a given amount

# Writing two functions:
# 1. computes tax based on a gross amount
# 2. calculates a net pay using the tax function (written previously)
# 
# Gross Amount and associated tax:
# 
# * 0-240:    0%
# * 241-480: 15%
# * 481-:    28% 

# In[7]:


def tax(amount):
    if amount <= 240:
        return 0
    elif amount > 240 and amount <= 480:
        return amount * .15
    else:
        return amount * .28
        
def netpay(grosspay):
    return grosspay - tax(grosspay)


# In[8]:


def howMuchTax():
    # Calling tax            
    amount = int(input("Enter amount of money: "))                            
    print("The tax is: " + str(tax(amount)))
    
def calcNetPay():
    # Calling netpay 
    gp = int(input("Enter gross pay: "))
    print("Net pay is " + str(netpay(gp)))


# In[9]:


# Testing tax
howMuchTax()


# In[11]:


# Testing netpay
calcNetPay()


# In[ ]:




