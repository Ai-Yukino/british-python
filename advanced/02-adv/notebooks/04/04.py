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

# + [markdown] tags=[]
# # `04.ipynb`
#
# <center>
#     <img src="images/04.png" style="width: 60%; border-radius: 2%">
# </center>
#
# [🖼 Thomas Bonometti | Unsplash](https://unsplash.com/photos/OyO5NDiRPMM)
#
# ---
#
# [👩‍💻 Students_Alcohol_Consumption $\subset$ 04_Apply $\subset$ pandas_exercises](https://github.com/zachhall/pandas_exercises/blob/master/04_Apply/Students_Alcohol_Consumption/Exercises.ipynb)

# + [markdown] tags=[]
# ## 📝 Table of contents 📝
#
# - [❄ Grading tips ❄](#❄)
# - [🐍 Python imports 🐍](#🐍)
# - [📁 Data 📁](#📁)
#     - [🍃 Extract](#🍃)
#     - [💧🔥 Transform](#💧🔥)
#     - [🍵 Load](#🍵)
# - [👀 Problems and solutions 👀](#👀)
#     - [❄ Step 1. $\dots$](#❄1)
#         - [🌸 Solution](#🌸1)
#     - $\vdots$
#     - [❄ Step 10. $\dots$](#❄10)
#         - [🌸 Solution](#🌸10)

# + [markdown] tags=[]
# ## 🐍 Python imports 🐍 <a id="🐍"></a>
# -

import pandas as pd
import numpy as np

# ## 📁 Data 📁 <a id="📁"></a>

# ### 🍃 Extract <a id="🍃"></a>

df = pd.read_csv("data/student-mat.csv")

# ### 💧🔥 Transform <a id="💧🔥"></a>

# +
df = df.loc[0:, "school":"guardian"]

cap = lambda s: s.capitalize()
columns = ["Mjob", "Fjob"]
df[columns] = df[columns].applymap(cap)

majority = lambda age: age > 17
df["legal_drinker"] = df["age"].apply(majority)

why = lambda x: 10 * x if type(x) is int else x
df = df.applymap(why)
# -

# ### 🍵 Load <a id="🍵"></a>

ser = df.iloc[-1, 0:]
pd.DataFrame(ser).T

# ## 👀 Problems and solutions 👀 <a id="👀"></a>

# ### ❄ Step 1. Import the necessary libraries <a id="❄1"></a>
#
# #### 🌸 Solution <a id="🌸1"></a>
#
# Line `1` in [🐍 Python imports 🐍](#🐍)

# ### ❄ Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv). <a id="❄2"></a>
#
# #### 🌸 Solution 🌸<a id="🌸2"></a>
#
# `data/student-mat.csv`

# ### ❄ Step 3. Assign it to a variable called df. <a id="❄3"></a>
#
# #### 🌸 Solution <a id="🌸3"></a>
#
# Line `1` in [🍃 Extract](#🍃)

# ### ❄ Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column <a id="❄4"></a>
#
# #### 🌸 Solution <a id="🌸4"></a>
#
# Line `1` in [💧🔥 Transform](#💧🔥)

# ### ❄ Step 5. Create a lambda function that will capitalize strings. <a id="❄5"></a>
#
# #### 🌸 Solution <a id="🌸5"></a>
#
# Line `3` in [💧🔥 Transform](#💧🔥)

# ### ❄ Step 6. Capitalize both Mjob and Fjob. <a id="❄6"></a>
#
# #### 🌸 Solution <a id="🌸6"></a>
#
# Line `4 -> 5` in [💧🔥 Transform](#💧🔥)

# ### ❄ Step 7. Print the last elements of the data set. <a id="❄7"></a>
#
# #### 🌸 Solution <a id="🌸7"></a>
#
# Line `1` in [🍵 Load](#🍵)

# ### ❄ Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob. <a id="❄8"></a>
#
# #### 🌸 Solution <a id="🌸8"></a>
#
# > Did you notice the original dataframe is still lowercase?
#
# Nope. No fix necessary

# ### ❄ Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old) <a id="❄9"></a>
#
# #### 🌸 Solution <a id="🌸9"></a>
#
# Line `7 -> 8` in [💧🔥 Transform](#💧🔥)

# ### ❄ Step 10. Multiply every number of the dataset by 10. <a id="❄10"></a>
#
# #### 🌸 Solution <a id="🌸10"></a>
#
# Line `10 -> 11` in [💧🔥 Transform](#💧🔥)
