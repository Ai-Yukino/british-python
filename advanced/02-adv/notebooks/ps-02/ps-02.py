# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # `ps-02.ipynb`
#
# ---
#
# [👩‍💻 Chipotle $\subset$ ... $\subset$ pandas_exerces | GitHub repo](https://github.com/zachhall/pandas_exercises/blob/master/02_Filtering_%26_Sorting/Chipotle/Exercises.ipynb)

# ## 🐍 Python imports 🐍

import pandas as pd

# ### Step 1. Import the necessary libraries
#
# ---
#
# See above cell

# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv).
#
# ---
#
# We manually saved this in `data`

# ### Step 3. Assign it to a variable called chipo.

chipo = pd.read_csv("data/chipotle.tsv", sep="\t")

# ### Step 4. How many products cost more than $10.00?

chipo
