import pandas as pd

# Path to the folder
folder_path = '/Users/annawilliams/Desktop/emailsValidator'

# Read the input CSV file
data_files = pd.read_csv(f'{folder_path}/markedByBouncer.csv')

# Display initial information about the dataset
print(data_files.head())
print(data_files.info())

# Create separate DataFrames for each category
deliverable = data_files[data_files['status'] == 'deliverable']
risky = data_files[data_files['status'] == 'risky']
undeliverable = data_files[data_files['status'] == 'undeliverable']
unknown = data_files[data_files['status'] == 'unknown']

# Save the DataFrames to CSV files
deliverable.to_csv(f'{folder_path}/deliverable.csv', index=False)
risky.to_csv(f'{folder_path}/risky.csv', index=False)
undeliverable.to_csv(f'{folder_path}/undeliverable.csv', index=False)
unknown.to_csv(f'{folder_path}/unknown.csv', index=False)

# Print the number of emails in each file
print(f"Number of deliverable emails: {deliverable.shape[0]}")
print(f"Number of risky emails: {risky.shape[0]}")
print(f"Number of undeliverable emails: {undeliverable.shape[0]}")
print(f"Number of unknown emails: {unknown.shape[0]}")