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

# # `02.ipynb`

# ## Problem 1
#
# - Get a space-separated list of integers from the user,
# - create a tuple of those integers, and
# - compute and print `hash(tuple)`.

# +
## Solution for problem 1

user_input = input("Give me a list of space-separate integers:")
user_tuple = user_input.replace(" ", ",")

print(f"The hash for the tuple ({user_tuple}) is {hash(user_tuple)}")
# -

# ## Problem 2
#
# Consider the lists
#
# ```python
# list1 = [3, 6, 9, 12, 15, 18, 21]
# list2 = [4, 8, 12, 16, 20, 24, 28]
# ```
#
# Create a third list containing
#
# - all the odd-index elements from the first list, and
# - all the even-index elements from the second list.

# +
## Solution for problem 2

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

list3 = list1[1::2] + list2[::2]

print(list3)
# -

# ## Problem 3
#
# Take the follow list.
#
# ```python
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# ```
#
# - Slice it into three equal sublists, and
# - reverse each sublist.

# +
## Solution for problem 3

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

list_1 = []
list_1 += [sample_list.pop(2)]
list_1 += [sample_list.pop(1)]
list_1 += [sample_list.pop(0)]

list_2 = []
list_2 += [sample_list.pop(2)]
list_2 += [sample_list.pop(1)]
list_2 += [sample_list.pop(0)]

list_3 = []
list_3 += [sample_list.pop(2)]
list_3 += [sample_list.pop(1)]
list_3 += [sample_list.pop(0)]

list = [list_1, list_2, list_3]

print(list)
# -

# ## Problem 4
#
# Consider the follow list and dictionary.
#
# ```python
# roll_numbers = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {"Zach" : 47, "Emma" : 69, "Kelly" : 76, "Jason" : 97}
# ```
#
# - Iterate through the elements `i` of `roll_number`,
# - check if `i` exists in `sample_dict` as a key, and
# - if not delete it from `roll_number`.

# +
## Solution for problem 4

roll_numbers = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {"Zach": 47, "Emma": 69, "Kelly": 76, "Jason": 97}
sample_values = sample_dict.values()

i = 0

while i < len(roll_numbers):
    if roll_numbers[i] in sample_values:
        roll_numbers.pop(i)
    else:
        i += 1
print(roll_numbers)
# -

# ## Problem 5
#
# Which of the following are valid ways to craete strings in Python?
#
# ```python
# str1 = "str1"
# str1 = 'str1'
# str1 = "'str1"'
# str1 = str("str1")
# ```

# ## Solution to problem 5
#
# Lines 1, 2, and 4 are valid.

str1 = "str1"
str1 = "str1"
# str1 = "'str1"'
str1 = str("str1")
