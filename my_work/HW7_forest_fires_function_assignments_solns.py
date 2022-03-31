#!/usr/bin/env python
# coding: utf-8

# ## Fighting Forest Fires with Functions
# 
# 
# ### University of Virginia
# ### Programming for Data Science
# ### Last Updated: July 26, 2021
# ---

# ### Objectives: 
# - Work with functions (built-in and user-defined), lambda functions, and list comprehensions
# 
# ### Executive Summary
# 
# 
# You will work with the Forest Fires Data Set from UCI.  
# 
# Information about the dataset: https://archive.ics.uci.edu/ml/datasets/Forest+Fires
# 
# Background: This dataset was used in a regression task, where the aim was to predict the burned area of forest
# fires, in the northeast region of Portugal, by using meteorological and other data.
# 
# We will apply some of the steps leading to an ML task.

# ### Instructions
# 
# Run the pre-populated code, and along the way, you will be asked to perform several graded tasks <span
# style="color:blue">(prompted in blue font)</span>. Show your code and solutions clearly in the cells following each
# question. When the file is completed, submit the notebook through Collab.
# 
# **TOTAL POINTS: 14**
# 
# ---
# 

# In[1]:


import numpy as np
import pandas as pd
import sys

# #### Read in the dataset from the UCI Machine Learning Repository

# In[2]:

path = sys.argv[1]
# print(path)

path_to_data = 'https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv'
fire = pd.read_csv(path)

# In[3]:


# print(fire.head(3))

# **Working with spatial coordinates X, Y**
# 
# X - x-axis spatial coordinate within the Montesinho park map: 1 to 9  
# Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9

# In[4]:


# extract the spatial coords

X, Y = fire.X.values, fire.Y.values


# **<span style="color:blue">(2 PTS) 1. Write a function called `coord_builder()` with these requirements:</span>**
# 
# - takes X, Y as inputs
# - contains a docstring with short description of the function
# - uses the zip() function (details: https://realpython.com/python-zip-function/)
# - builds and returns a list of tuples [(x1,y1), (x2,y2), ..., (xn,yn)] where (xi,yi) are the ordered pairs from X, Y
# 
# Hint: You'll need to call list() on the zipped object to show the results
# 

# In[5]:


def coord_builder(X, Y):
    """
    Take coordinates X, Y as inputs a build ordered pairs (list of tuples)
    """
    z = zip(X, Y)
    return list(z)


# **<span style="color:blue">(1 PT) 2. Call your `coord_builder()` function, passing in X, Y.  
#     Please subset the returned list to show a list with only the FIRST FIVE TUPLES. </span>**

# In[6]:

# **Working with AREA**

# In[7]:


# extract values for area
area = fire.area.values

# **<span style="color:blue">(1 PT) 3. Write code to print the minimum area and maximum area in a tuple
# (min_value, max_value) where the min_value, max_value are floats.</span>** 

# In[8]:


# **<span style="color:blue">(2 PTS) 4. Write a lambda function that computes the following transformation of a
# variable:</span>** ``` logarithm(base10) of [1 + x] ```
# 
# **<span style="color:blue">Then call the lambda function on *area*, printing the LAST 10 values.</span>**  
# Hint: numpy has a function that can be applied to an array.

# In[9]:


lx = lambda x: np.log10(1 + x)

# **Working with MONTH**
# 
# month - month of the year: 'jan' to 'dec'

# In[10]:


month = fire.month.values

# **<span style="color:blue">(1 PT) 5. Call the `unique()` function (from the numpy package) on *month*, printing the
# unique months:</span>**

# In[11]:


# **<span style="color:blue">(1 PT) 6. Write a list comprehension to select all months starting with letter 'a' from
# *month*. Next, call set() on the result, to get the unique months starting with letter 'a'. Print this
# result.</span>**

# In[12]:


uniq_mos = set([mo for mo in month if mo.startswith('a')])

# **Working with DMC**
# DMC - DMC index from the FWI system: 1.1 to 291.3  

# In[13]:


dmc = fire.DMC.values


# **<span style="color:blue">(2 PTS) 7. Write a function called `bandpass_filter()` with these requirements:</span>**
# 
# - takes three inputs: 
#   - a numpy array to be filtered
#   - an integer serving as a lower bound L
#   - an integer serving as an upper bound U
# - returns a new array containing only the values from the original array which are greater than L AND less than U

# In[14]:


def bandpass_filter(arr, lower, upper):
    return arr[(arr > lower) & (arr < upper)]


# **<span style="color:blue">(1 PT) 8. Call `bandpass_filter()` passing DMC as the array, L=25, U=35, printing the
# result. </span>**
# 

# In[15]:


arr_filt = bandpass_filter(dmc, 25, 35)

# **Working with FFMC**
# FFMC - FFMC index from the FWI system: 18.7 to 96.20

# In[16]:


FFMC = fire.FFMC.values


# **<span style="color:blue">(2 PTS) 9. Write a function called `sum_sq_err()` with these requirements:</span>**
# 
# - take a numpy array as input
# - compute the mean of the array, mu
# - using a for-loop, compute the squared deviation of each array element xi from the mean, (xi - mu)**2  
# Hint: it may be helpful to keep a running sum of the squared deviations
# 
# 
# - computes the sum of squared deviations
# - returns the sum of squared deviations

# In[17]:


def sum_sq_err(arr):
    mu = arr.mean()
    tot = 0
    for ar in arr:
        tot += (ar - mu) ** 2
    return tot


# **<span style="color:blue">(1 PT) 10. Call `sum_sq_err()` passing FFMC as the array, printing the result. </span>**

# In[18]:


print('Nathan Lindley', '\n')
print('Run the pre-populated code, and along the way, you will be asked to perform several graded tasks '
      'prompted in blue font. Show your code and solutions clearly in the cells '
      'following each question. When the file is completed, submit the notebook through Collab.', '\n')
print(path_to_data, '\n')
print(fire.head(3), '\n')
print(coord_builder(X, Y)[:5], '\n')
print((min(area), max(area)), '\n')
print(lx(area[-10:]), '\n')
print(np.unique(month), '\n')
print(uniq_mos, '\n')
print(arr_filt, '\n')
print(sum_sq_err(FFMC), '\n')
