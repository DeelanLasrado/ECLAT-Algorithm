'''# importing dataset ( example 1 and example 2 are datasets in pyECLAT)
from pyECLAT import Example2
# storing the dataset in a variable
dataset = Example2().get()
# printing the dataset
print(dataset.head())

# printing the info
dataset.info()

# importing the ECLAT module
from pyECLAT import ECLAT
# loading transactions DataFrame to ECLAT class
eclat = ECLAT(data=dataset)
# DataFrame of binary values
print(eclat.df_bin)

# count items in each column
items_total = eclat.df_bin.astype(int).sum(axis=0)
print(items_total)

# count items in each row
items_per_transaction = eclat.df_bin.astype(int).sum(axis=1)
print(items_per_transaction)

# the item shoud appear at least at 5% of transactions
min_support = 5/100
# start from transactions containing at least 2 items
min_combination = 2
# up to maximum items per transaction
max_combination = max(items_per_transaction)
rule_indices, rule_supports = eclat.fit(min_support=min_support,
                                                 min_combination=min_combination,
                                                 max_combination=max_combination,
                                                 separator=' & ',
                                                 verbose=True)'''

'''#The fit() method of the ECLAT class returns:

association rule indices
association rule support values'''

from pyECLAT import Example2, ECLAT

# Load the dataset
dataset = Example2().get()

# Create an instance of the ECLAT class
eclat = ECLAT(data=dataset)

# Set minimum support and combination parameters
min_support = 0.05  # 5% of transactions
min_combination = 2  # Minimum combination of 2 items
max_combination =3  # Maximum combination of items per transaction

# Find frequent item combinations
rule_indices, rule_supports = eclat.fit(min_support=min_support, min_combination=min_combination, max_combination=max_combination, separator=' & ')
print(rule_indices)

# Print the frequent item combinations
for item_combination in rule_indices:
    print(f"Items: {item_combination}, Support: {rule_supports[item_combination]}")
