#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:07:32 2022

@author: nathanlindley
"""

import numpy as np
import os

data_path = '/Users/nathanlindley/Desktop/Spring 2022/DS 2001/Coffee/'
file_name = 'Coffee_TRAIN.txt'
full_path = os.path.join(data_path, file_name)

data = np.loadtxt(full_path, delimiter='  ',dtype=str)

data2 = np.loadtxt(full_path)
