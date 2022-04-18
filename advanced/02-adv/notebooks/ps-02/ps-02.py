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

# + [markdown] tags=[]
# ## ❄ Step 1. Import the necessary libraries ❄
#
# ---
#
# See above code cell

# + [markdown] tags=[]
# ## ❄ Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). ❄
#
# ---
# -

# We manually saved this in `data`

# + [markdown] tags=[]
# ## ❄ Step 3. Assign it to a variable called `chipo`. ❄
#
# ---
# -

chipo = pd.read_csv("data/chipotle.tsv", sep="\t")

# + [markdown] tags=[]
# ## ❄ Step 4. How many products cost more than $10.00? ❄
#
# ---
# -

# This is an ambiguous question because "products" may have unique prices. For example, run

chipo.iloc[[4001, 1002]]

# So we'll just create a sub-DataFrame of `chipo` where the price row has value greater than $10.00.

# ### Rename price column: `"item_price" -> "price_usd"`

chipo.rename(columns={"item_price": "price_usd"}, inplace=True)

# + [markdown] tags=[]
# ### Convert "price_usd" values to `float64`
# -

chipo["price_usd"] = pd.to_numeric(chipo["price_usd"].str.extract(r"(\d*\.\d*)")[0])

chipo["price_usd"].dtype

# ### Filter for values greater than $10.00

df_boolean = chipo["price_usd"] >= 10.00
df_filtered = chipo[df_boolean]
df_filtered

# ### Final answer

df_filtered.shape[0]

# + [markdown] tags=[] jp-MarkdownHeadingCollapsed=true tags=[]
# ## ❄ Optional section: explore price discrepancies❄
#
# ---

# + [markdown] tags=[]
# ### Dataset overview

# +
# chipo
# -

# ### Store list of unique values in `item_name`

items = chipo["item_name"].unique()
items

# ### Price groups (`"quantity" == 1` only, though)

for item in items:
    print(f"{item} price(s):")
    print(
        chipo[(chipo["item_name"] == item) & (chipo["quantity"] == 1)][
            "price_usd"
        ].unique()
    )
    print("\n")

# ### Example: "Bottled Water"

# +
# df = (chipo["item_name"] == "Bottled Water") & (chipo["quantity"] == 1)
# chipo[df]

# +
# df = (chipo["item_name"] == "Bottled Water") & (chipo["quantity"] == 1) & (chipo["item_price"].str.match(r"\$1.09"))
# # chipo[df]

# chipo[df].index

# +
# df = (chipo["item_name"] == "Bottled Water") & (chipo["quantity"] == 1) & (chipo["item_price"].str.match(r"\$1.50"))
# # chipo[df]

# chipo[df].index.tolist()

# + [markdown] tags=[]
# ## ❄ Step 5. What is the price of each item? ❄
# i.e., print a data frame with only two columns `item_name` and `item_price` (which we changed to `price_usd`)
#
# ---
# -

df_lazy_prices = chipo[["item_name", "price_usd"]]
df_lazy_prices

# ## ❄ Step 6. Sort by the name of the item ❄
#
# ---

df_lazy_prices.sort_values(by="item_name")

# ## ❄ Step 7. What was the quantity of the most expensive item ordered? ❄
#
# ---

df_sorted = chipo.sort_values(by="price_usd", ascending=False)
df_sorted.iloc[0]["quantity"]

# ## ❄ Step 8. How many times was a Veggie Salad Bowl ordered? ❄
#
# ---

df_boolean = chipo["item_name"] == "Veggie Salad Bowl"
df_boolean.sum()
# chipo[df_boolean].shape[0]

# ## ❄ Step 9. How many times did someone order more than one Canned Soda? ❄
#
# ---

df_boolean_1 = chipo["item_name"] == "Canned Soda"
df_boolean_2 = chipo["quantity"] > 1
(df_boolean_1 & df_boolean_2).sum()
# chipo[df_boolean_1 & df_boolean_2].shape[0]
