#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 22:02:48 2018

@author: Avadhoot
"""

import pandas as pd
import numpy as np
import conda.cli

df = pd.read_csv("anaconda_package_list_macos.csv")

for index, row in df.iterrows():
    print("Installing - ", row['Name'])
    conda.cli.main('conda', 'install',  '-y', row['Name'])
   
#conda.cli.main('conda', 'install',  '-y', 'numpy')