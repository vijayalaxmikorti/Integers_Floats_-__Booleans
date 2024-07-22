'''Problem 1
You are given a sentence which reads "Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation."

Find the number of words in the given sentence.'''

SOLUTION:
# Store the given sentence in a variable
sentence = "Wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation."
# Calculate the total number of words in the sentence.  Hint : Use the count() method
num_of_words = sentence.count(" ")+1
# Print the variable num_of_words
print(num_of_words)

'''Problem 2
Write a Python code which takes a number and returns a corresponding string of hyphens. For example if the number is 3, it will return '---' , if the number is 5 it will return '-----'.'''

SOLUTION:
# Store the user input in a variable
inputted_number = int(input())
# Create a string of equivalent number of hyphens. Hint : remember what happens when we multiply string by a number?
string_of_hyphens = inputted_number * "-"
# Print the string of hyphens
print(string_of_hyphens)

'''Problem 3
A string can be called a safe bridge if it has no gaps in it i.e, no spaces. You are supposed to take an input from the user and print whether the string is a safe bridge or not.'''

SOLUTION:
# Store the user input in a variable
bridge = input()
# Return True if the bridge is safe and False if the bridge is not safe. Hint : Use the find() method
is_safe_bridge = bridge.find(" ") == -1
is_safe_bridge
# Fill in the blanks
print(f"It is {is_safe_bridge} that the bridge is a safe bridge" )

'''Problem 4
Count the number of D's in a string inputted by the user. This will be case insensitive.'''

SOLUTION:
# Store the user input in a variable
user_string = 'Debris was scattered all over the yard in the densest region of Denmark'
# Store the count of letter D in the inputted string. Note this will be a case insensitive search
D_counts = user_string.count("D")
# Fill in the blanks
print(f"The total occurrence of D in the user_string is {D_counts}")

'''Problem 5
Check whether a given string is a palindrome. A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam, racecar.'''

SOLUTION:
# Store the user input in a variable
user_string = input()
# Print True if a string is a Palindrome else print false
user_string[::] == user_string[::-1]
