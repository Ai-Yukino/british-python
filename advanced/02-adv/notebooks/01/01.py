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

# # `ps-01.ipynb`
#
# ---
#
# [👩‍💻 World Food Facts $\subset$ ... $\subset$ pandas_exerces | GitHub repo](https://github.com/zachhall/pandas_exercises/blob/master/01_Getting_%26_Knowing_Your_Data/World%20Food%20Facts/Exercises.ipynb)
#

# ## 🐍 Python imports 🐍

import pandas as pd

# ### Step 1. Go to https://www.kaggle.com/openfoodfacts/world-food-fats/data
#
# ### Step 2. Download the dataset to your computer and unzip it.
#
# ### Step 3. Use the tsv file and assign it to a dataframe called food

# ## ❄ Solution to steps 1 -> 3 ❄
#
# ❗ This is a huge dataset: 963MB ❗
#
# It took me almost 30 seconds to load.
#
# <div align="center">
#     <img src="images/large.png" style="width: 30%; border-radius: 2%">
# </div>
#
# ---
#
# - `en.openfoodfacts.org.products.tsv` is not included in the remote GitHub repo
# - If you cloned this repo, you need to redownload `en.openfoodfacts.org.products.tsv` following steps 1 -> 2
#     - You need to sign up for a kaggle account to download the dataset

food = pd.read_csv("data/en.openfoodfacts.org.products.tsv", sep="\t", low_memory=False)

# ### Step 4. See the first 5 entries

food.head(5)

# ### Step 5. What is the number of observations in the dataset?

food.shape[0]

# ### Step 6. What is the number of columns in the dataset?

food.shape[1]

# ### Step 7. Print the name of all the columns.

# help(type(food.columns))
columns = food.columns.tolist()
columns

# ### Step 8. What is the name of 105th column?

food.columns.tolist()[104]

# ### Step 9. What is the type of the observations of the 105th column?

food.iloc[:, 104].dtype

# ### Step 10. How is the dataset indexed?

food.index

# ### Step 11. What is the product name of the 19th observation?

food.iloc[18]["product_name"]
