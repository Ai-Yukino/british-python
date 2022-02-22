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

# 1) Accept the user's first and last name and print them in reverse order with a space between them

# +
# https://docs.python.org/3/library/functions.html#input

first_name = input("What's your first name?\n")
last_name = input("Alright, well what about your last name?\n")
print("---\n", last_name, first_name, "\n---")
# -


# 2) Accept an integer $n$ input from the user and compute the value of
#
# $$n + nn + nnn.$$
#
# For example if $n = 4$, then
#
# $$n + nn + nnn = 4 + 44 + 444 = 492.$$

# +
# https://docs.python.org/3/library/functions.html#int
# https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
# n + nn + nnn = n * (1 + 11 + 111) = n * 123


def get_input():
    req = f"Enter a single-digit integer; n ="
    res = input(req)
    n = int(res)
    return n


# Validate input
n = get_input()
is_single = abs(n) < 10

# Repeat user input if validation fails
while is_single is False:
    n = get_input()
    is_single = abs(n) < 10

# Compute nn, nnn, and n + nn + nnn
if n < 0:
    sign = "-"
else:
    sign = ""

n_string = sign + str(abs(n))
nn_string = n_string + str(abs(n))
nnn_string = nn_string + str(abs(n))
total = str(n * 123)

# Print n + nn + nnn
print(
    "n + nn + nnn = "
    + n_string
    + " + "
    + nn_string
    + " + "
    + nnn_string
    + " = "
    + total
    + "."
)
# -

# 3) Ask the user "What country are you from?".
# Then print the following statement:
#
# <center>
#     "I have heard that [input] is a beautiful country!"
# </center>

# +
# https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals

country = input("What country are you from?")
print(f"I have heard that {country} is a beautiful country!")
# -

# 4) What is the output of the following Python code?
#
# ```python
# x = 10
# y = 50
# if (x ** 2 > 100 and y < 100):
#        print(x,y)
# ```

# ## Answer
#
# There is no output since
#
# $$ x^2 = 100 \not< 100.$$

x = 10
y = 50
if x**2 > 100 and y < 100:
    print(x, y)
# print(x ** 2 > 100 and y < 100)

# 5) What is the output of the following (`+`) operator, and why does this code chunk execute this way?
#
# ```python
# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)
# ```

# + [markdown] tags=[]
# ## Answer
#
# ```
# [10, 20, 30, 40]
# [10, 20, 30, 40]
# ```
#
# ## Explanation
#
# Arrays are mutable data-types with pointers, so the code
#
# ```python
# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)
# ```
#
# modifies the value to an underlying list object rather than creating new objects. See the following links for more details.
#
# - https://docs.python.org/3/glossary.html#term-mutable
# - https://docs.python.org/3/library/functions.html#id
# - https://docs.python.org/3/library/stdtypes.html#listhttps://docs.python.org/3/library/stdtypes.html#list

# + tags=[]
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)

print(f"type(a): {type(a)}")
print(f"type(b): {type(b)}")
print(f"id(a) == id(b): {id(a) == id(b)}")
# -

# 6) What is the out of the following code and what arithmetic operation is being used here?
#
# ```python
# print(2%6)
# ```

# ## Answer
#
# ```python
# 2
# ```
#
# ## Explanation
#
# `%` is the modulo operator. See the following links for more details.
#
# - https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
# - https://en.wikipedia.org/wiki/Modulo_operation

print(2 % 6)

# 7) What is the output of the following code and what arithmetic operators are used here?
#
# ```python
# print(2 * 3 ** 3 * 4)
# ```

# ## Answer
#
# $$
# 2 \cdot 3 ^ 3 \cdot 4 = 216
# $$
#
# Multiplication and exponention are the operators. See the following links for more details.
#
# - https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
# - https://docs.python.org/3/reference/expressions.html?highlight=precedence#operator-precedenceprint(2 * 3 ** 3 * 4)

print(2 * 3**3 * 4)

# 8) What is a text editor?

# ## Answer
#
# A text editor is a program that allows you to literally just edit plain text. Some text editors such as [vim](https://en.wikipedia.org/wiki/Vim_(text_editor)) can be extended to have other features that are helpful for programming.

# 9) What is python?

# ## Answer
#
# Python is an interpreted and dynamically-typed general-purpose programming language. See the following links for more details.
#
# - https://en.wikipedia.org/wiki/Python_(programming_language)
# - https://docs.python.org/3/

# + [markdown] jp-MarkdownHeadingCollapsed=true tags=[]
# 10) What is jupyter notebook, what type of python environment is it, and what alternatives are there to jupyter notebook?
# -

# ## Answer
#
# Jupyter notebook is an environment for interactive [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) coding that supports languages such as python, R, and Julia among others. It can be used as an interactive python environment. Nowadays, there are alternatives such as using IDE's like VS Code/Codium and PyCharm that have support for interactive python notebooks.
