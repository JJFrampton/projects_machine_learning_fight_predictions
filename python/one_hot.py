#!/usr/bin/env python3
import pandas as pd

print(pd.__version__)

def one_hot(matrix, column):
    dummies = pd.get_dummies(matrix[column], prefix=column)
    matrix = pd.concat([matrix, dummies], axis=1)
    matrix.drop([column], axis=1, inplace=True)
    matrix = remove_spaces(matrix)
    print(matrix)
    some = matrix
    return some
    # return matrix

def remove_spaces(matrix):
    matrix.columns = matrix.columns.str.replace(' ', '-')
    return matrix
