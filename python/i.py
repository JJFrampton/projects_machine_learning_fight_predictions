#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import importlib

libs = ['main', 'matrix_stats', 'one_hot']

for lib in libs:
    globals()[lib] = importlib.import_module(lib)
