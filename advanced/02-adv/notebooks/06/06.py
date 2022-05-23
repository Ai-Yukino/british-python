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
# # `06.ipynb`
#
# <center>
#     <img src="../../images/06/06.png" style="width:80%; border-radius:5px;">
# </center>
#
# [🖼 JL Lacar | Stairs from Kimi no Na wa (Your Name) | Unsplash](https://unsplash.com/photos/zFLj1i2Rt-M)
#
# ---
#
# [🧑💻 zachhall | `pandas_exercises/06_Stats/US_Baby_Names/` | GitHub](https://github.com/zachhall/pandas_exercises/tree/master/06_Stats/US_Baby_Names)

# + [markdown] tags=[]
# ## 🐍 Python imports 🐍 <a id="🐍"></a>
#
# ---

# + [markdown] tags=[]
# ### 🐍🐍 Standard library <a id="🐍🐍"></a>
#
# ---

# + tags=[]
import pandas as pd

# + [markdown] tags=[]
# ## 📁 Data 📁 <a id="📁"></a>
#
# ---
# -

# ### 📁📁 Cell `1` <a id = "📁📁1"></a>

# + tags=[]
baby_names = pd.read_csv("../../data/06/US_Baby_Names_right.csv")
baby_names.head(10)
# -

# ### 📁📁 Cell `2` <a id = "📁📁2"></a>

baby_names.drop(columns=["Unnamed: 0", "Id"], inplace=True)

# ### 📁📁 Cell `3 -> 4` <a id = "📁📁3->4"></a>

genders = baby_names["Gender"]
genders.value_counts().is_unique

genders.value_counts().idxmax()

# ### 📁📁 Cell `6` <a id = "📁📁6"></a>

gb = baby_names.groupby("Name")
names = gb["Count"].sum()

# ### 📁📁 Cell `7` <a id = "📁📁7"></a>

names.shape[0]

# ### 📁📁 Cell `8 -> 9` <a id = "📁📁8->9"></a>

ser = names == names.max()
names[ser].shape[0]

names[ser].index[0]

# + [markdown] tags=[]
# ### 📁📁 Cell `10` <a id = "📁📁10"></a>

# + tags=[]
ser = names == names.min()
names[ser].shape[0]
# -

# ### 📁📁 Cell `11` <a id = "📁📁11"></a>

names.median()

# ### 📁📁 Cell `12` <a id = "📁📁12"></a>

names.std()

# ### 📁📁 Cell `13` <a id = "📁📁13"></a>

names.describe()

# + [markdown] tags=[]
# ## ❓ "Steps" ❔
#
# ---
#
# - Show line numbers
#     - `SHIFT + L` while not editing cell
# - Use dark theme
#     - `Settings -> Theme -> JupyterLab Dark`

# + [markdown] jp-MarkdownHeadingCollapsed=true tags=[]
# ### ❄❄ Step 1. Import the necessary libraries
# -

# ### ❄❄❄ Solution
#
# ---
#
# - [🐍🐍 Standard library](#🐍🐍)

# ### 🌸🌸 Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv).

# ### 🌸🌸🌸 Solution
#
# ---
#
# - `../../data/06/US_Baby_Names_right.csv`

# ### ❄❄ Step 3. Assign it to a variable called baby_names.

# ### ❄❄❄ Solution
#
# ---
#
# - [📁📁 Cell `1`](#📁📁1)
#     - Line `1`

# ### 🌸🌸 Step 4. See the first 10 entries

# ### 🌸🌸🌸 Solution
#
# ---
#
# - [📁📁 Cell `1`](#📁📁1)
#     - Line `2`

# ### ❄❄ Step 5. Delete the column 'Unnamed: 0' and 'Id'

# ### ❄❄❄ Solution
#
# ---
#
# - [📁📁 Cell `2`](#📁📁2)

# ### 🌸🌸 Step 6. Are there more male or female names in the dataset?

# ### 🌸🌸🌸 Solution
#
# More female names
#
# ---
#
# - [📁📁 Cells `3 -> 4`](#📁📁3->4)

# ### ❄❄ Step 7. Group the dataset by name and assign to names

# ### ❄❄❄ Solution
#
# ---
#
# - [📁📁 Cell `6`](#📁📁6)

# ### 🌸🌸 Step 8. How many different names exist in the dataset?

# ### 🌸🌸🌸 Solution
#
# `17632`
#
# ---
#
# - [📁📁 Cell `7`](#📁📁7)

# ### ❄❄ Step 9. What is the name with most occurrences?

# ### ❄❄❄ Solution
#
# `Jacob`
#
# ---
#
# - [📁📁 Cells `8 -> 9`](#📁📁8->9)

# ### 🌸🌸 Step 10. How many different names have the least occurrences?

# ### 🌸🌸🌸 Solution
#
# `2578`
#
# ---
#
# - [📁📁 Cell `10`](#📁📁10)
#

# ### ❄❄ Step 11. What is the median name occurrence?

# ### ❄❄❄ Solution
#
# `49.0`
#
# ---
#
# - [📁📁 Cell `11`](#📁📁11)
#

# ### 🌸🌸 Step 12. What is the standard deviation of names?

# ### 🌸🌸🌸 Solution
#
# `11006.06946789057`
#
# ---
#
# - [📁📁 Cell `12`](#📁📁12)

# ### ❄❄ Step 13. Get a summary with the mean, min, max, std and quartiles.

# ### ❄❄❄ Solution
#
# ---
#
# - [📁📁 Cell `13`](#📁📁13)
