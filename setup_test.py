import pandas as pd

# Create a simple dictionary of data
data = {
    'Student': ['You', 'Friend'],
    'Goal': ['Master in Europe', 'Learn Git'],
    'Level': ['Year 2', 'Beginner']
}

# Turn it into a Pandas DataFrame (a fancy Excel table)
df = pd.DataFrame(data)

# Print it to the screen
print("--- My First Data Science Object ---")
print(df)
print("------------------------------------")

