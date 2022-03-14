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

# # 📝 `04.ipynb`

# ## ❄ Problem 1 ❄
#
# [🍅 Write a function | HackerRank](https://www.hackerrank.com/challenges/write-a-function/problem)
#
# ---
#
# Let $n\geq 0$ be an integer.
# Then n is an `leap year` if
#
# $$
# n \equiv 0 \pmod 4,
# $$
#
# and
#
# $$
# n \equiv 0 \pmod{100} \quad \Rightarrow \quad n \equiv 0 \pmod{400}.
# $$
#
# Write a programming function `f(n)` which takes integer inputs
#
# $$
# 1900 \leq n \leq 10^5
# $$
#
# such that
#
# $$
# f(n) =
# \begin{cases}
# \text{True}, \quad &\text{if } n \text{ is a leap year}\\
# \text{False}, \quad &\text{if } n \text{ is not a leap year}\\
# \end{cases}.
# $$

# +
## Solution to problem 1


def f(n):
    if n % 100 == 0:
        if n % 400 == 0:
            return True
        else:
            return False
    else:
        if n % 4 == 0:
            return True
        else:
            return False


n = int(input("Give me a year:"))

if f(n) == True:
    print(f"{n} is a leap year.")
else:
    print(f"{n} is not a leap year.")
# -

# ## HackerRank screenshot for problem 1
#
# <center>
# <img src="images/1.png" style="width: 75%;">
# </center>

# ## ❄ Problem 2 ❄
#
# [🍅 Exceptions | HackerRank](https://www.hackerrank.com/challenges/exceptions/problem)
#
# ---
#
# <center>
# <img src="images/2-instructions.png" style="width: 75%;">
# </center>
#
#

# +
## Solution to problem 2

import traceback

j = int(input("Enter an postive integer:"))

for i in range(0, j):
    x = input("Enter two characters:").split()
    try:
        a = int(x[0])
        b = int(x[1])
        print(a // b)
    except Exception as e:
        print(f"Error Code: {e}")
# -

# ## HackerRank screenshot for problem 2
#
# <center>
# <img src="images/2.png" style="width: 75%;">
# </center>
