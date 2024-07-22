#Problem 1

'''In a cricket tournament, based on the outcome of a particular match a team gets following points:
* wins gets 3 points
* draws gets 1 points
*losses gets 0 points
Team Aravali plays 8 matches in this tournament. It wins 4 matches, loses 3 matches and draws 1. What is the total number of points gained by the Team Aravali?
SOLUTION:'''
# The outcome variables are defined below
wins = 4
losses = 3
draws = 1
# Calculate the total points gained by Team Aravali
aravali_points = wins*3 + losses*0 + draws*1
# Print the variable aravali_points
aravali_points

#Problem 2
'''Root of a function  f(x)  is defined as the value  x  where  f(x)=0 
Consider a quadratic function  f(x)=x2+3x−4 
Find the value of the function  f(x)  at points  x=2,x=−1,x=1 .
SOLUTION:'''
# Calculate the value of the function f(x) at x = 2
func_evaluated_at_2 = 2**2 + 3*2 - 4
# Print the value below
func_evaluated_at_2
# Calculate the value of the function f(x) at x = -1
func_evaluated_at_minus1 = (-1)**2 + 3*(-1) - 4
# Print the value below
func_evaluated_at_minus1
# Calculate the value of the function f(x) at x = 1
func_evaluated_at_1 = 1**2 + 3*1 -4
# Print the type of the variable below
func_evaluated_at_1

#Return the boolean for each value of x to find out whether that value is a root of  f(x)
SOLUTION:
# Check whether 2 is a root of f(x)
func_evaluated_at_2 == 0
# Check whether -1 is a root of f(x)
func_evaluated_at_minus1 == 0
# Check whether 1 is a root of f(x)
func_evaluated_at_1 == 0

#Problem 3
'''A bag contains 45 apples, 65 oranges and 30 bananas. Find the percentage of each type of food items in the bag.
SOLUTION:'''
apples = 45
oranges = 65
bananas = 30
# Calculate the percentage of apples and print the variable
apples/(apples + oranges + bananas)*100
# Calculate the percentage of oranges and print the variable
oranges/(apples + oranges + bananas)*100
# Calculate the percentage of bananas and print the variable
bananas/(apples + oranges + bananas)*100

#Problem 4
'''You were playing a fun guessing game during your school break. There were a total of 100 participants excluding you. Out of these 100 people, 30 were Maths Majors, 45 were Economics Majors and 25 were Physics Majors.

The game was divided into three rounds.

In the first round, you had to guess the number of Maths Majors and you correctly guessed 20 of them.
In the second round, you had to guess the number of Economics Majors and you correctly guessed 30 of them.
In the final third round, you had to guess the number of Physics Majors and you correctly guessed 20 of them.
Accuracy is defined as the number of correct guesses upon total number of people in the group (expressed in percentage)
SOLUTION:'''
#Define your variables:
# Store the number of Maths majors
mathsm = 30

# Store the number of Economics majors
ecom = 45

# Store the number of Physics majors
phym = 25

# Store the number of your correct guesses of Maths majors
correct_mathsm = 20

# Store the number of your correct guesses of Economics majors
correct_ecom = 30

# Store the number of your correct guesses of Physics majors
correct_phym = 20

Calculate your accuracy in each of the three rounds:
# Print the Maths accuracy
maths_acc = correct_mathsm/mathsm  * 100
maths_acc

# Print the Economics accuracy
eco_acc = correct_ecom/ecom  * 100
eco_acc

# Print the Physics accuracy
phy_acc = correct_phym/ phym * 100
phy_acc

#Calculate your overall accuracy in the entire game:
# Print the overall accuracy
overall_acc = (correct_mathsm + correct_ecom + correct_phym)/(mathsm + ecom + phym) * 100
overall_acc
