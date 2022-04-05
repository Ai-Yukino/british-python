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

# # `06.ipynb`

# ## ❄ Problem 1 ❄
#
# [🍅 Regex Substitution | HackerRank](https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem)
#
# ---
#
# <center>
# <img src=images/1-instructions.png style="width: 75%">
# </center>

# +
# Solution for problem 1

from re import sub as sub

N = int(input("Enter number of lines:"))

# test = "d \&\& dd && dd || dd"
# test = "    && ||   "

# def repl(matchobj):
#     if matchobj.group(0) == r" && " :
#         return " and "
#     elif matchobj.group(0) == r" || " :
#         return " or "b
#     else :
#         return " "

for i in range(0, N):
    line = sub(r" \&\& ", r" and ", input("Enter line:"))
    line = sub(r" \|\| ", r" or ", line)
    line = sub(r" \&\& ", r" and ", line)
    line = sub(r" \|\| ", r" or ", line)

    # line = sub(r" \&\& ", r" and ", test)

    # line = sub(r" \&\& | \|\| ", repl, input())
    # line = sub(r" \&\& | \|\| ", repl, test)
    print(line)
# -


# ## HackerRank screenshot for problem 1
#
# <center>
# <img src=images/1.png style="width: 75%;">
# </center>

# ## ❄ Problem 2 ❄
#
# [🍅 Validating and Parsing Email Addresses | HackerRank](https://www.hackerrank.com/challenges/validating-named-email-addresses/problem)
#
# ---
#
# <center>
# <img src=images/2-instructions.png style="width: 75%">
# </center>

# +
# Solution for problem 2

import email.utils
import re

# from email.utils import parseaddr as parseaddr
# from email.utils import formataddr as formataddr

N = int(input())
username = r"([a-z]|[A-Z]){1}([a-z]|[A-Z]|[0-9]|\-|\.|\_)+"
domain = r"([a-z]|[A-Z])+"
extension = r"([a-z]|[A-Z]){1,3}"

pattern = re.compile(username + r"\@" + domain + r"\." + extension + r"$")

# test = "name <user@agegsh.comd>"

for i in range(0, N):
    # pair = email.utils.parseaddr(test)
    pair = email.utils.parseaddr(input())
    match = pattern.match(pair[1])
    isValid = match is not None

    if isValid:
        print(email.utils.formataddr(pair))
# -


# ## HackerRank screenshot for problem 2
#
# <center>
# <img src=images/2.png style="width: 75%;">
# </center>
