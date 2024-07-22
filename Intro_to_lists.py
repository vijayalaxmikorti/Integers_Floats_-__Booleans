'''Problem 1
A list contains the average daily temperature(in degree Celsius) of a city over a particular week. Write a Python code to swap the highest and the lowest temperatures.'''

SOLUTION:
# A list containing average daily temperature over a week
temperatures = [34, 40, 29, 33, 42, 37, 39 ]

# The expected output
# output_temperatures = [34, 40, 42, 33, 29, 37, 39]
# Store the highest temperature
max_temp = max(temperatures)

# Index of the element with the highest temperature
max_temp_index =temperatures.index(max_temp)

# Store the lowest temperature
min_temp = min(temperatures)

# Index of the element with the lowest temperature
min_temp_index = temperatures.index(min_temp)

# Swap the highest and the lowest temperatures
temperatures[max_temp_index] = min_temp
temperatures[min_temp_index] = max_temp

# Print the output list
print(temperatures)

'''Problem 2
Measures of Averages
Mean of a group is defined as the sum of the elements in the group divided by the number of elements in the group.
Median is the middle number in a sorted, ascending or descending, list of numbers. If the list has  N  numbers where  N  is odd, then median is the element in the middle i.e,  (N+12)th  element. If  N  is even, then median is the mean of  (N2)th  and  (N2+1)th  elements'''

SOLUTION:
# List of product prices

prod_price_list = [400, 250, 800, 550, 600, 820, 720, 15000, 360,250]
# Calculate the mean of the product prices. Use list functions. Also print the mean_price
mean_price = sum(prod_price_list)/len(prod_price_list)
print(mean_price)
#Calculate the median price
# Step 1 - Obtain the sorted list. Print the sorted_prices
sorted_prices = sorted(prod_price_list)
print(sorted_prices)
# Check if the number of elements in the list is even or odd
len(sorted_prices) % 2 == 0
# Use the corresponding formula to calculate the median and print the median
length_list = len(sorted_prices)
median_price = (sorted_prices[int(length_list/2)-1] + sorted_prices[int(length_list/2)])/2
median_price
# Check which is greater, mean or median
mean_price > median_price

'''Problem 3
Having a nested list sometimes might be a bit problematic. An individual was asked to collect the names of companies in the technology sector. While creating the list, by mistake the last three companies were subsumed in a list as shown below. You are required to get rid of the nesting'''

SOLUTION:
# The list of tech companies curated by the individual
tech_companies = ['Qualcomm','Google','Apple',['Nvidia','Cisco','Samsung']]

# The final list that we want
# correct_tech_companies = ['Qualcomm','Google','Apple','Nvidia','Cisco','Samsung']
# Write your code below
last_element = tech_companies[-1]
companies = tech_companies[:3] + tech_companies[-1]
companies
# Do the same task another way
tech_companies.remove(last_element)
tech_companies.extend(last_element)
tech_companies
