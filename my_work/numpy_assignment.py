#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:41:35 2022

@author: nathanlindley

Numpy programming assignment
"""

import pandas as pd
import numpy as np

path_to_data1 = "https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"
fire = pd.read_csv(path_to_data1)
print(fire.head(2))

cols_to_keep = ['temp','wind','rain','area']

