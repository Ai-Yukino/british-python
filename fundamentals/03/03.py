# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # `03.ipynb`

# ## Problem 1
#
# Guess a number between 1 to 9.

# +
## Solution for problem 1

# import random

from random import randrange

answer = randrange(10)
guess = -1

while guess != answer:
    guess = int(input("Guess an integar in [0, 10]:"))
print("That's correct!")
# -

# ## Problem 2
#
# Validate the user password input according to the follow criteria:
#
# - At least 1 letter between `[a-z]` and 1 letter between `[A-Z]`
# - At least 1 number between `[0-9]`
# - At least 1 character from `[$#@]`
# - Minimum length 6 cahracters
# - Maximum length 16 characters

# +
## Solution for problem 2
# https://www.youtube.com/watch?v=K8L6KVGG-7o
# https://docs.python.org/3/library/re.html

import re

user_input = input("Enter a password:")

# print(has_valid_length)
# print(has_lower)
# print(has_upper)
# print(has_digit)
# print(has_special)

is_valid = False

while is_valid is False:
    user_input = input("Enter a password:")

    lower_matches = list(re.compile(r"[a-z]").finditer(sentence))
    upper_matches = list(re.compile(r"[A-Z]").finditer(sentence))
    digit_matches = list(re.compile(r"\d").finditer(sentence))
    special_matches = list(re.compile(r"[$#@]").finditer(sentence))

    has_valid_length = len(user_input) >= 6 and len(user_input) <= 16
    has_lower = len(lower_matches) >= 1
    has_upper = len(upper_matches) >= 1
    has_digit = len(digit_matches) >= 1
    has_special = len(special_matches) >= 1
    # is_valid = has_valid_length and has_lower and has_upper and has_digit and has_special
    is_valid = all([has_valid_length, has_lower, has_upper, has_digit, has_special])

print("Your password is valid 👍")
# -

# ## Problem 3
#
# - Get the input of the age of 3 people, and
# - print out the oldest and youngest among them.

# +
### Solution for problem 3

age_1 = int(input("Enter the first person's age:"))
age_2 = int(input("Enter the second person's age:"))
age_3 = int(input("Enter the third person's age:"))

ages = [age_1, age_2, age_3]

print(f"The older person is {max(ages)} years old")
print(f"The youngest person is {min(ages)} years old")
# -

# ## Problem 4
#
# A student will not be allowed to sit in an exam if their attendence is less than `75%`.
#
# Take the follow input the from the user:
#
# - Number of classes held
# - Number of classes attended
#
# Compute:
#
# - Attendence percetnage of the student
#
# Output:
#
# - Whether or not the student can sit in the exam

# +
## Solution to problem 4

total = int(input("Enter the total number of lectures:"))
attended = int(input("How many classes have you attended?"))

percentage = round(100 * (attended / total), 2)

print(f"You have attend {percentage}% of the lectures.")
if percentage < 75:
    print("You cannot sit in the exam.")
else:
    print("You can attend the exam.")
# -

# ## Problem 5
#
# Get an integer `N` from the user and do the following:
#
# - if `N` is odd then
#     - print "weird",
# - if `N` is even and $N\in[2,5]$ then
#     - print "Not Weird",
# - if `N` is even and $N\in[6,20]$ then
#     - print "Weird"
# - if `N` is even and $N> 20$ then
#     - print "Not Weird"

# +
## Solution to problem 5

N = int(input("Enter a positive integer:"))
is_odd = N % 2 == 1

if is_odd is True:
    print("Weird")
elif N >= 2 and N <= 5:
    print("Not Weird")
elif N >= 6 and N <= 20:
    print("Weird")
else:
    print("Not Weird")
