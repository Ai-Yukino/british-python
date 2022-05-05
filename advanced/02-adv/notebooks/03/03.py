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
# # `03.ipynb`
#
# <center>
#     <img src="images/03.png" style="width: 70%; border-radius: 2%;">
# </center>
#
# [🖼 Li Jiangang | Unsplash](https://unsplash.com/photos/b4lS_gXkQp0)
#
# ---
#
# [👩‍💻 Alcohol_Consumption $\subset$ 03_grouping $\subset$ pandas_exercises](https://github.com/zachhall/pandas_exercises/blob/master/03_Grouping/Alcohol_Consumption/Exercise.ipynb)
#
# <center>
#     <img src="images/diagram.png" style="width: 25%; border-radius:2%">
# </center>
# -

# ## 🐍 Python imports 🐍 <a id="🐍"></a>

import pandas as pd

# ## 📁 Data processing 📁 <a id="📁"></a>

drinks = pd.read_csv("data/drinks.csv")

# ## ❄ Step 1. Import the necessary libraries ❄
#
# ## 🌸 Solution 🌸
#
# See [🐍 Python import 🐍](#🐍) section.

# ## ❄ Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv). ❄
#
# ## 🌸 Solution 🌸
#
# Local copy made in `data` folder

# ## ❄ Step 3. Assign it to a variable called drinks. ❄
#
# ## 🌸 Solution 🌸
#
# See [📁 Data processing 📁](#📁) section.

# ## ❄ Step 4. Which continent drinks more beer on average? ❄
#
# ## 🌸 Solution 🌸

gb_df = drinks.groupby("continent")
gb_ser = gb_df["beer_servings"]
gb_ser.mean()

# ## ❄ Step 5. For each continent print the statistics for wine consumption. ❄
#
# ## 🌸 Solution 🌸

gb_df = drinks.groupby("continent")
gb_ser = gb_df["wine_servings"]
gb_ser.describe()

# ## ❄ Step 6. Print the mean alcohol consumption per continent for every column ❄
#
# ## 🌸 Solution 🌸

gb_df = drinks.groupby("continent")
gb_df.mean()

# ## ❄ Step 7. Print the median alcohol consumption per continent for every column ❄
#
# ## 🌸 Solution 🌸

gb_df = drinks.groupby("continent")
gb_df.median()

# ## ❄ Step 8. Print the mean, min and max values for spirit consumption. ❄
#
# ## 🌸 Solution 🌸

gb_df = drinks.groupby(drinks["continent"])
gb_ser = gb_df["spirit_servings"]
gb_ser.agg(["mean", "min", "max"])
