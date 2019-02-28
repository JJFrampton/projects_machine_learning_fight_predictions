#!/usr/bin/env python3

# Fight metrics
# use the simplest approach you can
# get something working first then tweak,
# rework, or rewrite

import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import stats

# help(pd) # help for pandas
# dir(pd) # list of pandas functions

fighters = pd.read_csv("../data/ufc_fighters__sherdog_2_23_2016.csv")
fights = pd.read_csv("../data/ufc_fights__sherdog_2_23_2016.csv")

fights_n = fights.shape[0]
fighters_n = fighters.shape[0]

stopped_in_round_one = fights[fights["round"] < 2].shape[0]
percent = (stopped_in_round_one / fights_n) * 100
percent = int(percent)
print('\n\n%s%% of fights were stopped in round one' %(percent))
print('(%s of %s fights)\n' %(stopped_in_round_one, fights_n))

print('\nnulls for categorical cols')
cat_cols = fighters.select_dtypes(include=['object']).copy()
stats.m_nulls(cat_cols)

# show all types in the dataframe (objects should be encoded)
print('\ncolumn types')
print(fighters.dtypes)
# get all category types ( ~object == strings in pandas)
objects = fighters.select_dtypes(include=['object']).copy()
# drop nick names (not relevant, many NAs)
fighters.drop(['nick'], axis=1, inplace=True)
#   drop rows with null class (not a good idea to drop rows)
#   loss of data will be compounded when joining with fights
# fighters.drop(fighters[fighters['class'].isna()].index, inplace=True)
#   instead replace with most frequent class # need to check when joining that both fighters are in the same class!!
#   - should really encode a dummie, the replace with opponents class, if still na then encode frequent
# fighters['class'].value_counts()
filler = fighters['class'].describe().top
fighters.fillna({"class": filler}, inplace=True)

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

print('\nFighters stats')
print(fighters.describe())
print("\nvalue count per col (non null)")
print(fighters.count())

# birthdate parsing
fighters['birth_date'] = pd.to_datetime(fighters['birth_date'])
# ages should be calculated per fight event, then nulls can be filled with average


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

# count how many nulls
# fighters['birth_date'].isnull().value_counts()

#   finding duplicates
# fighters[fighters['fid'].duplicated()].sort_values('fid')
#   check original vs duplicate
# x = fighters[fighters['fid'].duplicated()].sort_values('fid').head(1)['fid'].iloc[0]
# fighters[fighters['fid'] == x]

#   look at records with duplicate fid
dup = pd.DataFrame()
fids = fighters[fighters['fid'].duplicated()].sort_values('fid')['fid']
for fid in fids:
    dup = pd.concat([dup, fighters[fighters['fid']== fid]], axis=0)

# replace all nulls with unknown
fighters = fighters.fillna({"association": "unknown"})
fighters = fighters.fillna({"locality": "unknown"})
fighters = fighters.fillna({"country": "unknown"})
fighters = fighters.fillna({"name": "unknown"})
# weight, height and birthdate can be averages by the class?

# break down of nulls per fighter class
# try to fix with averages for that class
averages = fighters.mean() # only includes height and weight, dates will have to be converted to int time
fs = fighters['class'].unique()
for f in fs:
    stats.m_nulls(fighters[fighters['class'] == f])

# merge
full_fights = fights.copy(deep=True)
full_fights = full_fights.merge(fighters, left_on='f1fid', right_on='fid')
full_fights = full_fights.merge(fighters, left_on='f2fid', right_on='fid')

# parse dates
full_fights['event_date'] = pd.to_datetime(full_fights['event_date'])

# get ages (in days)
full_fights['f1_age'] = full_fights['event_date'] - full_fights['birth_date_x']
full_fights['f2_age'] = full_fights['event_date'] - full_fights['birth_date_y']

# testing - no diff in age avg for win / loss
full_fights['f1_age'].describe()
full_fights['f2_age'].describe()

# get averages for height, weight, and age by class
fighters.groupby('class').describe()

# get ages for comparisons
full_fights['f1_age'] = full_fights['f1_age'].dt.days / 365
full_fights['f2_age'] = full_fights['f2_age'].dt.days / 365
# full_fights['f1_age'] = full_fights['f1_age'].astype(int) # need to remove nulls first
# compare
g1 = full_fights[full_fights['f1_age'] < 20].shape[0]
g2 = full_fights[(full_fights['f1_age'] >= 20) & (full_fights['f1_age'] < 30)].shape[0]
g3 = full_fights[(full_fights['f1_age'] >= 30) & (full_fights['f1_age'] < 40)].shape[0]
g4 = full_fights[full_fights['f1_age'] >= 40].shape[0]
print("\n")
print("wins under 20 years old %s" %(g1))
print("wins between 20 and 30 years old %s" %(g2))
print("wins between 30 and 40 years old %s" %(g3))
print("wins over 40 years old %s" %(g4))
