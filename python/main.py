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
percent = (stopped_in_round_one / fights_n) * 100
percent = int(percent)
print('%s%% of fights were stopped in round one' %(percent))
print('(%s of %s fights)' %(stopped_in_round_one, fights_n))

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

print(fighters.describe())
print("value count per col (non null)\n")
print(fighters.count())


# def matrix_stats(matrix):
#     rows = matrix.shape[0]
#     cols = matrix.shape[1]
#     result = pd.DataFrame(matrix.columns)
#     for i in cols:
#         result
#     matrix[:,0]


# creating a sub matrix of main matrix
# fighters.iloc[[0,1],[0,1]]

# create frame of uniqe values
# x = pd.Series()
# for fight in fighters.columns:
    # x.append(pd.Series(fighters[fight].unique().shape[0]))
