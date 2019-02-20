#!/usr/bin/env python3

# Fight metrics
# use the simplest approach you can
# get something working first then tweak,
# rework, or rewrite

import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

fighters = pd.read_csv("../data/ufc_fighters__sherdog_2_23_2016.csv")
fights = pd.read_csv("../data/ufc_fights__sherdog_2_23_2016.csv")

fights_n = fights.shape[0]
fighters_n = fighters.shape[0]

stopped_in_round_one = fights[fights["round"] < 2].shape[0]
print('stopped in round one : %s' %(stopped_in_round_one))

# print(fighters.head)
# print(fights.head)

# can use oneHot
heights = fighters['height'].unique().shape[0]
weights = fighters['weight'].unique().shape[0]
countries = fighters['country'].unique().shape[0]
# might be too much for oneHot, try leave one out
associations = fighters['association'].unique().shape[0]
classes = fighters['class'].unique().shape[0]
locality = fighters['locality'].unique().shape[0]

def one_hot(column):
    labels = column[1:1].name
    result = pd.get_dummies(column,prefix=[labels])
    return result

def column_stats(column):
    n = column.shape[0]
    cardinality = column.unique().shape[0]
    cardinality_percent = cardinality / n
    print("cardinality : %s" %(cardinality))
    print("cardinality percent : %s" %(cardinality_percent))

binary_classes = one_hot(fighters['class'])
