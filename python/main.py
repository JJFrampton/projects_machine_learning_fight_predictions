#!/usr/bin/env python3

# Fight metrics

import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

fighters = pd.read_csv("ufc_fighters__sherdog_2_23_2016.csv")
fights = pd.read_csv("ufc_fights__sherdog_2_23_2016.csv")

fights_n = fights.shape[0]
fighters_n = fighters.shape[0]

stopped_in_round_one = fights[fights["round"] < 2].shape[0]
print('stopped in round one : %s', %(stopped_in_round_one))

# print(fighters.head)
# print(fights.head)
