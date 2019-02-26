#!/usr/bin/env python3
import pandas as pd

def cardinality(matrix):
    result = {}
    for col in matrix.columns:
        result[col] = {}
        result[col]['cardinality'] = matrix[col].unique().shape[0]
        percent = result[col]['cardinality'] / matrix.shape[0]
        percent = percent * 100
        percent = int(percent)
        result[col]['cardinality_percent'] = percent
    return result

def c_nulls(column):
    print(column.isnull().value_counts())

def m_nulls(matrix):
    print(matrix[matrix.isnull().any(axis=1)].isna().sum())
