
from matplotlib import pyplot
from pandas import read_csv
series = read_csv('battery_levels.txt', header=0, index_col=0, parse_dates=True, squeeze=True)
print(series.head())

series.plot(subplots=True) #subplots=True, figsize(6,6))
pyplot.show()
