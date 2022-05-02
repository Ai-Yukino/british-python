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

# # `02.ipynb`
#
# <center>
#     <img src="images/02.png", style="width:50%; border-radius:2%">
# </center>
#
# [🖼 Chris Curry | unsplash](https://unsplash.com/photos/KsSxzBnozMY)
#
# ---
#
# [👩‍💻 Chipotle $\subset$ 02_Filtering_&_Sorting $\subset$ pandas_exerces | GitHub repo](https://github.com/zachhall/pandas_exercises/blob/master/02_Filtering_%26_Sorting/Chipotle/Exercises.ipynb)
#
# Run
#
# - [🐍 Python imports 🐍](#🐍), and then
# - [📁 Data processing 📁](#📁).
#
# Then any section [❄ Step 1 ...❄](#❄1) to [❄ Step 9 ...❄](#❄9) can be run independently of each other.
#

# ## 🐍 Python imports 🐍 <a id="🐍"></a>

import pandas as pd

# ## 📁 Data processing 📁 <a id="📁"></a>
#
# - Store data in `chipo` variable
# - Convert object-valued column `item_price` to `float64`-valued `price_usd` column
# - Add unit-price column `unit_price_usd`

# +
chipo = pd.read_csv("data/chipotle.tsv", sep="\t")

chipo.rename(columns={"item_price": "price_usd"}, inplace=True)
chipo["price_usd"] = pd.to_numeric(chipo["price_usd"].str.extract(r"(\d*\.\d*)")[0])

chipo["unit_price_usd"] = chipo["price_usd"] / chipo["quantity"]

# + [markdown] tags=[]
# ## ❄ Step 1. Import the necessary libraries ❄ <a id="❄1"></a>
#
# ## 🌸 Solution 🌸
#
# See [🐍 Python imports 🐍](#🐍) section

# + [markdown] tags=[]
# ## ❄ Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). ❄
#
# ## 🌸 Solution 🌸
#
# We manually saved this in `data`.

# + [markdown] tags=[]
# ## ❄ Step 3. Assign it to a variable called `chipo`. ❄
#
# ## 🌸 Solution 🌸
#
# See [📁 Data processing 📁](#📁) section

# + [markdown] tags=[]
# ## ❄ Step 4. How many products cost more than $10.00? ❄
#
# ## 🌸 Solution 🌸
# -

ser = chipo["unit_price_usd"] > 10
chipo[ser]["item_name"].unique().shape[0]

# + [markdown] tags=[]
# ## ❄ Step 5. What is the price of each item? ❄
# i.e., print a data frame with only two columns `item_name` and `item_price` (which we changed to `price_usd`)
#
# ## 🌸 Solution 🌸
# -

chipo[["item_name", "price_usd"]]

# ## ❄ Step 6. Sort by the name of the item ❄
#
# ## 🌸 Solution 🌸

chipo.sort_values(by="item_name", inplace=False)

# ## ❄ Step 7. What was the quantity of the most expensive item ordered? ❄
#
# ## 🌸 Solution 🌸
#
# This is ambiguous, so we will sort by both total price and unit price.

# ### ⚪ Total price

df = chipo.sort_values(by="price_usd", inplace=False, ascending=False)
df.iloc[0]["quantity"]

# ### ⚫ Unit price

df = chipo.sort_values(by="unit_price_usd", inplace=False, ascending=False)
df.iloc[0]["quantity"]

# ## ❄ Step 8. How many times was a Veggie Salad Bowl ordered? ❄
#
# ## 🌸 Solution 🌸

ser = chipo["item_name"] == "Veggie Salad Bowl"
ser.sum()

# ## ❄ Step 9. How many times did someone order more than one Canned Soda? ❄ <a id="❄9"></a>
#
# ## 🌸 Solution 🌸

ser_1 = chipo["item_name"] == "Canned Soda"
ser_2 = chipo["quantity"] > 1
(ser_1 & ser_2).sum()
