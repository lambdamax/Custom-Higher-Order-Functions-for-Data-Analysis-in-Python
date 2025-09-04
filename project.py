import csv
from functools import reduce

def count(predicate, itr):
  """Returns the number of elements in itr for which predicate returns True."""
  # task 1
  count_filter = filter(predicate, itr)
  # task 2
  count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
  return count_reduce

def average(itr):
  # If itr is not iterable, this will generate an iterator.  
  """Returns the average of the elements in the iterable itr. If the iterable
  is empty, returns 0."""
  iterable = iter(itr)
  # task 8
  return avg_helper(0, iterable, 0)

# task 3
def avg_helper(curr_count, itr, curr_sum):
  # task 4
  """Recursively calculates the average of the elements in the iterable itr.
  
  Takes as arguments the current count of elements seen, the iterable itself,
  and the current sum of the elements seen.  If the iterable is exhausted,
  returns the average of the elements seen.  Otherwise, adds the next element
  in the iterable to the current sum, increments the count, and calls itself.
  """
  next_num = next(itr, "null")
  # task 5
  if next_num == "null":
    # return curr_sum/curr_count
    return curr_sum/curr_count if curr_count != 0 else 0  # adding error handling for empty iterable

  curr_count += 1
  # task 4
  curr_sum += next_num
  # task 6
  return avg_helper(curr_count, itr, curr_sum)

# reading the CSV file and using the functions above
with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  # task 9
  count_belgiums = count(lambda x: x[1] == "Belgium", reader)
  print(count_belgiums)

  # reset `csvfile` object to the beginning of the file
  csvfile.seek(0)
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')  # reset `reader` object as well (recommended)
  
  # task 10
  avg_portugal = average(map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader)))
  print(avg_portugal)
  
# task 11
# Create more higher order functions. Ex: `median()`, `standard_deviation()`
  
def median(itr):
  """Returns the median of the elements in the iterable itr. If the iterable
  is empty, returns 0."""
  sorted_list = sorted(itr)
  n = len(sorted_list)
  if n == 0:
    return 0
  mid_index = n // 2
  if n % 2 == 0:
    return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
  else:
    return sorted_list[mid_index]
  
def standard_deviation(itr):
  """Returns the standard deviation of the elements in the iterable itr. If
  the iterable is empty, returns 0."""
  avg = average(itr)
  n = len(list(itr))
  if n == 0:
    return 0
  sum_squared_diffs = sum((x - avg)**2 for x in itr)
  return (sum_squared_diffs / (n - 1))**0.5

# use median and standard_deviation functions
with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  
  count_belgiums = count(lambda x: x[1] == "Belgium", reader)
  print("Count Belgium: ", count_belgiums)
  
  csvfile.seek(0)
  avg_portugal = average(map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader)))
  print("Average: ", avg_portugal)
  
  csvfile.seek(0)
  median_portugal = median(map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader)))
  print("Median: ", median_portugal)
  
  csvfile.seek(0)
  std_portugal = standard_deviation(map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader)))
  print("Standard Deviation: ", std_portugal)

# task 12
# Come up with different ways to calculate the values from tasks nine and ten

# Ex: using `pandas` library
import pandas as pd

# task 9
df = pd.read_csv('1kSalesRec.csv')
count_belgiums = len(df[df['Country'] == 'Belgium'])
print(count_belgiums)

# task 10
avg_portugal = df.loc[df['Country'] == 'Portugal', 'Total Profit'].mean()
print(avg_portugal)

# Ex: using `statistics` library
import statistics

# task 9
with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  count_belgiums = sum(1 for x in reader if x[1] == "Belgium")
  print(count_belgiums)

# task 10
with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  avg_portugal = statistics.mean(map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader)))
  print(avg_portugal)
  
# Ex: using `numpy` library
import numpy as np

# task 9
with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  count_belgiums = sum(1 for x in reader if x[1] == "Belgium")
  print(count_belgiums)

# task 10
with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)
  avg_portugal = np.mean(list(map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader))))
  print(avg_portugal)
