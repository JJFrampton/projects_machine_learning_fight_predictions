
# need better data to plot
x = pd.DataFrame()
x = pd.concat([x, fighters['class']], axis=1)
x = pd.concat([x, fighters['birth_date']], axis=1)
x = x.transpose()
x.plot.hist()

