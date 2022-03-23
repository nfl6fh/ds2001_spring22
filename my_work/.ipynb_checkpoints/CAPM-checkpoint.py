#!/usr/bin/env python
# coding: utf-8

# ## Capital Asset Pricing Model (CAPM)
# ### Strength Training with Functions, Numpy
# 
# 
# ### University of Virginia
# ### Programming for Data Science
# ### Last Updated: June 29, 2021
# ---

# ### Objectives: 
# - Use numpy and functions to compute a stock's CAPM beta
# - Perform sensitivity analysis to understand how the data points impact the beta estimate
# 
# ### Background
# 
# 
# In finance, CAPM is a single-factor regression model used for explaining and predicting excess stock returns. There are better, more accurate models, but it has its uses. For example, the *market beta* is a useful output.
# 
# 
# Here is the formula for calculating the expected excess return:
# 
# \begin{aligned} &E[R_i] - R_f  = \beta_i ( E[R_m] - R_f ) \\ \\ &\textbf{where:} \\ &ER_i = \text{expected return of stock i} \\ &R_f = \text{risk-free rate} \\ &\beta_i = \text{beta of the stock} \\ &ER_m - R_f = \text{market risk premium} \\ \end{aligned} 
# 
# #### Review the instructions below to complete the requested tasks.
# 
# #### TOTAL POINTS: 10
# ---  
# 

# In[1]:


# load modules
import numpy as np
import pandas as pd

# risk-free Treasury rate
R_f = 0.0175 / 252


# In[2]:


# read in the market data
data = pd.read_csv('capm_market_data.csv')


# Look at some records  
# SPY is an ETF for the S&P 500 (the "stock market")  
# AAPL is Apple  
# The values are closing prices, adjusted for splits and dividends

# In[3]:


print(data)


# Drop the date column

# In[4]:


data1 = data.drop('date',1)
print(data1)


# Compute daily returns (percentage changes in price) for SPY, AAPL  
# Be sure to drop the first row of NaN  
# Hint: pandas has functions to easily do this

# In[5]:


returnSPY = [0]
returnAAPL = [0]
for i in range(1,len(data1)):
    spy = (data1.spy_adj_close[i]-data1.spy_adj_close[i-1])/100
    returnSPY.append(spy)
    aapl = (data1.aapl_adj_close[i]-data1.aapl_adj_close[i-1])/100
    returnAAPL.append(aapl)
r = {'SPY_returns': returnSPY,'AAPL_returns': returnAAPL}
returns = pd.DataFrame(r)
returns1 = returns.drop(0)


# #### 1. (1 PT) Print the first 5 rows of returns

# In[6]:


print(returns1)


# Save AAPL, SPY returns into separate numpy arrays  
# #### 2. (1 PT) Print the first five values from the SPY numpy array, and the AAPL numpy array

# In[7]:


aapl = pd.DataFrame()
aapl['price'] = data1['aapl_adj_close']
aapl['returns'] = returns['AAPL_returns']

spy = pd.DataFrame()
spy['price'] = data1['spy_adj_close']
spy['returns'] = returns['SPY_returns']

print(spy[0:5])
print(aapl[0:5])


# ##### Compute the excess returns of AAPL, SPY by simply subtracting the constant *R_f* from the returns.
# ##### Specifically, for the numpy array containing AAPL returns, subtract *R_f* from each of the returns. Repeat for SPY returns.
# 
# NOTE:  
# AAPL - *R_f* = excess return of Apple stock  
# SPY - *R_f* = excess return of stock market
# 

# In[8]:


spy_ex_ret = [0]
aapl_ex_ret = [0]
for i in range(1,len(spy)):
    spy_ex_ret.append(spy['returns'][i] - R_f)
    aapl_ex_ret.append(aapl['returns'][i] - R_f)
spy['excess_returns'] = spy_ex_ret
aapl['excess_returns'] = aapl_ex_ret


# #### 3. (1 PT) Print the LAST five excess returns from both AAPL, SPY numpy arrays
# 

# In[9]:


print(spy['excess_returns'][-5:])
print(aapl['excess_returns'][-5:])


# #### 4. (1 PT) Make a scatterplot with SPY excess returns on x-axis, AAPL excess returns on y-axis####
# Matplotlib documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

# In[10]:


import matplotlib.pyplot
matplotlib.pyplot.scatter(spy['excess_returns'],aapl['excess_returns'])


# #### 5. (3 PTS) Use Linear Algebra (matrices) to Compute the Regression Coefficient Estimate, \\(\hat\beta_i\\)
# 
# Hint 1: Here is the matrix formula where *x′* denotes transpose of *x*.
# 
# \begin{aligned} \hat\beta_i=(x′x)^{−1}x′y \end{aligned} 
# 
# Hint 2: consider numpy functions for matrix multiplication, transpose, and inverse. Be sure to review what these operations do, and how they work, if you're a bit rusty.

# In[11]:


x,y = spy['excess_returns'],aapl['excess_returns']

a = (np.matmul(x,np.transpose(x)))**-1
b = np.matmul(np.transpose(x),y)
beta = np.multiply(a,b)
beta


# You should have found that the beta estimate is greater than one.  
# This means that the risk of AAPL stock, given the data, and according to this particular (flawed) model,  
# is higher relative to the risk of the S&P 500.
# 

# 

# #### Measuring Beta Sensitivity to Dropping Observations (Jackknifing)

# Let's understand how sensitive the beta is to each data point.   
# We want to drop each data point (one at a time), compute \\(\hat\beta_i\\) using our formula from above, and save each measurement.
# 
# #### 6. (3 PTS) Write a function called `beta_sensitivity()` with these specs:
# 
# - take numpy arrays x and y as inputs
# - output a list of tuples. each tuple contains (observation row dropped, beta estimate)
# 
# Hint: **np.delete(x, i).reshape(-1,1)** will delete observation i from array x, and make it a column vector

# In[12]:


def beta_sensitivity(x,y):
    sensitivities = []
    for i in range(len(x)-1):
        xd = x.drop(i)
        yd = y.drop(i)
        a = (np.matmul(xd,np.transpose(xd)))**-1
        b = np.matmul(np.transpose(xd),yd)
        beta = np.multiply(a,b)
        beta
        curr = (i,beta)
        sensitivities.append(curr)
    return sensitivities


# #### Call `beta_sensitivity()` and print the first five tuples of output.

# In[13]:


sens = beta_sensitivity(x,y)
print(sens[0:5])

