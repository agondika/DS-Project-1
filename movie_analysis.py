import pandas as pd  # 1. Grab the Pandas tool and give it the nickname 'pd'

# 2. READ
# We use the tool 'pd' and its command 'read_csv' to open the file.
# We store the result in a variable called 'df' (short for DataFrame).
df = pd.read_csv('movies.csv')

# 3. SHOW
# Print the 'df' variable to the screen so we can see the table.
print("--- ALL MOVIES ---")
print(df)