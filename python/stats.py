#!/usr/bin/env python3
import pandas as pd

def cardinality(m):
    result = {}
    for col in m.columns:
        result[col] = {}
        result[col]['cardinality'] = m[col].unique().shape[0]
        percent = result[col]['cardinality'] / m.shape[0]
        percent = percent * 100
        percent = int(percent)
        result[col]['cardinality_percent'] = percent
    return result
