import pandas as pd

# Load your data
df = pd.read_csv('/Users/yangzhao/Chat.csv')

# Ensure 'Tenure' is filled (handle NaNs)
df['Tenure'] = df['Tenure'].fillna(0).astype(int)

# Create a function to expand each row based on the Tenure
def expand_rows(row):
    expanded_data = []
    start_year = row['Start Year']
    end_year = row['End Year']
    tenure = row['Tenure']
    
    for year in range(tenure):
        new_row = row.copy()
        new_row['Culmulative Year'] = start_year + year
        new_row['Culmulative Tenure'] = year + 1
        expanded_data.append(new_row)
    
    return pd.DataFrame(expanded_data)

# Group by 'Brand by Gender' and 'Designer', then expand the rows
expanded_df_list = []

# Partition by 'Brand by Gender' and 'Designer'
grouped = df.groupby(['Brand by Gender', 'Designer'])

# Loop through each group and expand
for name, group in grouped:
    expanded_group = pd.concat([expand_rows(row) for _, row in group.iterrows()])
    expanded_df_list.append(expanded_group)

# Concatenate all expanded groups
final_expanded_df = pd.concat(expanded_df_list)

# Reset index for clarity
final_expanded_df.reset_index(drop=True, inplace=True)

# Export the expanded DataFrame to a CSV file
final_expanded_df.to_csv('/Users/yangzhao/Expanded_Tenure_Data.csv', index=False)