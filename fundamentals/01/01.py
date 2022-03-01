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

# # `01.ipynb`

# ## Problem 1
#
# Accept the user's first and last name. Print them in reverse order with a space between them.

# +
## Solution for problem 1

first = input("Gimme your first name:")
last = input("Tell me your last name:")

print(last, first)
# -

# ## Problem 2
#
# Accept a positive single-digit integer (n) and compute the value of
#
# $$
# n + nn + nnn.
# $$

# +
## Solution for question 2

req = "Enter a positive single-digit integer (n):"
n = int(input(req))

print(f"n + nn + nnn = {123 * n}")
# -

# ## Problem 3
#
# Ask the user
#
# > What country are you from?
#
# Then print the following statement:
#
# > I have heard that [input] is a beautiful country!

# +
## Solution for problem 3

country = input("What country are you from?")
print(f"I have heard that {country} is a beautiful country!")
# -

# ## Problem 4
#
# Is a String Immutable in Python?

# ## Solution for problem 4
#
# Yes. See the [docs](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types):
# > ... numbers, strings and tuples are immutable

# ## Problem 5
#
# - What is the output of
# ```python
# x = 36/4 * (3 + 2) * 4 + 2.
# ```
# - Explain why that is the output.

# + [markdown] tags=[]
# ## Solution for problem 5
#
# The [order of operations](https://en.wikipedia.org/wiki/Order_of_operations) gives
#
# $$
# \begin{align}
# x &= \frac{36}{4} \cdot (3 + 2) \cdot 4 + 2\\
# &= 9 \cdot 5 \cdot 4 + 2\\
# &= 180 + 2\\
# &= 182.
# \end{align}
# $$
#
# Division coerces the result into a float, so the final output is
#
# ```python
# x = 182.0
# ```
# -

x = 36 / 4 * (3 + 2) * 4 + 2
print(x)

# ## Problem 6
#
# Write a for loop that
#
# - computes $4\cdot i$ where $i\in[0,10]\cap\mathbb{Z}$, and
# - prints $4\cdot i = $ `4i`

# +
## Solution for problem 6

factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in factors:
    print(f"4⋅i = {4 * i}")
# -

# ## Problem 7
#
# Use two nested for loops to print the following multiplication table:
#
# <img src="images/table.png" style="width:300px">

# +
## Solution for question 7

factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in factors:
    row = ""
    for j in factors:
        product = i * j
        if product < 10:
            row += f"  {i * j} "
        elif product < 100:
            row += f" {i * j} "
        else:
            row += f"{i * j} "
    print(row)
