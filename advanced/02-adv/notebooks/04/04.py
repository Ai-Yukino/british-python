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
# ---
#
# [👩‍💻 Students_Alcohol_Consumption $\subset$ 04_Apply $\subset$ pandas_exercises](https://github.com/zachhall/pandas_exercises/blob/master/04_Apply/Students_Alcohol_Consumption/Exercises.ipynb)
#
# -

# ## 🐍 Python imports 🐍 <a id="🐍"></a>

import pandas as pd

# ## 📁 Data processing 📁 <a id="📁"></a>

# +
df = pd.read_csv("data/student-mat.csv")
df = df.loc[0:, "school":"guardian"]

cap = lambda s: s.capitalize()
# -

# ## ❄ Step 1. Import the necessary libraries ❄
#
# ## 🌸 Solution 🌸
#
# See [🐍 Python imports 🐍](#🐍) section.

# ## ❄ Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv). ❄
#
# ## 🌸 Solution 🌸
#
# See [📁 Data processing 📁](#📁) section.

# ## ❄ Step 3. Assign it to a variable called df. ❄
#
# ## 🌸 Solution 🌸
#
# See [📁 Data processing 📁](#📁) section.

# ## ❄ Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column ❄
#
# ## 🌸 Solution 🌸
#
# See [📁 Data processing 📁](#📁) section.

# ## ❄ Step 5. Create a lambda function that will capitalize strings. ❄
#
# ## 🌸 Solution 🌸
#
# See [📁 Data processing 📁](#📁) section.

# ## ❄ Step 6. Capitalize both Mjob and Fjob. ❄
#
# ## 🌸 Solution 🌸
#
# See [📁 Data processing 📁](#📁) section.
