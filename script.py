import codecademylib

# 1 import
import numpy as np

# 2 generate DataFrame from csv
calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')
# print(calorie_stats)

# 3 calculate calorie mean
comp_average = np.mean(calorie_stats)
crunchy_average = 60
average_calories = comp_average - crunchy_average

print("Comp AVG (initial): {ca1}\nCrunchy AVG: 60\nDifference: {avg1}".format(ca1=comp_average, avg1=average_calories))

# 4
calorie_stats_sorted = np.sort(calorie_stats)
# print(calorie_stats_sorted)

# 5
median_calories = np.median(calorie_stats_sorted)
print("Median: {}".format(median_calories))

# 6
perc=4
nth_percentile = np.percentile(calorie_stats_sorted, perc)
print("% of competition with lower calories: {}".format(perc))
print(nth_percentile)

# 7
more_calories = np.mean(calorie_stats_sorted > 60)*100
print("percentage with more calories: {}".format(more_calories))

# 8
calorie_std = np.std(calorie_stats_sorted)
print("STD: {}".format(calorie_std))
