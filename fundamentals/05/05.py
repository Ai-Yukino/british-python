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

# # 📝 `05.ipynb`

# ## ❄ Problem 1 ❄
#
# [🍅 itertools.product() | HackerRank](https://www.hackerrank.com/challenges/itertools-product/problem)
#
# ---
#
# <center>
# <img src=images/1-instructions.png style="width: 75%">
# </center>

# +
## Solution to problem 1

from itertools import product as product

A_string = input("Enter a list of numbers:").split()
B_string = input("Enter another list of numbers of the same length:").split()

A = [int(i) for i in A_string]
B = [int(i) for i in B_string]

AxB = list(product(A, B))

for x in AxB:
    print(x, end=" ")
# -

# ## HackerRank screenshot for problem 1
#
# <center>
# <img src=images/1.png style="width: 75%;">
# </center>

# ## ❄ Problem 2 ❄
#
# [🍅 `itertools.permutations()` | HackerRank](https://www.hackerrank.com/challenges/itertools-permutations/problem)
#
# ---
#
# <center>
# <img src=images/2-instructions.png style="width: 75%">
# </center>

# +
## Solution to problem 2

from itertools import permutations as permutations

req = "Give me a string and number less than or equal to that string's length:"

Sk = list(input(req).split())

S = "".join(sorted(list(Sk[0])))
k = int(Sk[1])

# print(S)
# print(k)
# print(list(permutations(S,k)))

for p in list(permutations(S, k)):
    print("".join(p))
# -

# ## HackerRank screenshot for problem 2
#
# <center>
# <img src=images/2.png style="width: 75%">
# </center>
