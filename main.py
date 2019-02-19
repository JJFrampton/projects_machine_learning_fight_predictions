#!/usr/bin/env python3

import numpy as np
import pandas as pd

fighters = pd.read_csv('./ufc_fighters__sherdog_2_23_2016.csv')
fights = pd.read_csv('./ufc_fights__sherdog_2_23_2016.csv')

print(fights.head())
print(fighters.head())

print(fights.shape)
print(fighters.shape)

print(fights.columns.values)
print(fighters.columns.values)
