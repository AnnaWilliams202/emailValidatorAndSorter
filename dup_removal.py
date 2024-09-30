import pandas as pd
import os

def load_csv_files(folder_path):
    all_emails = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            emails = df['Email 1'].tolist()  # Change 'email' to the appropriate column name
            all_emails.extend(emails)
    return all_emails

def remove_duplicates(email_list):
    unique_emails = set(email_list)
    return list(unique_emails)

def save_unique_emails(unique_emails, output_path):
    df = pd.DataFrame(unique_emails, columns=['email'])
    df.to_csv(output_path, index=False)

def main():
    folder_path = '/Users/annawilliams/Desktop/emailsValidator'
    output_path = '/Users/annawilliams/Desktop/emailsValidator/unique_emails.csv'

    all_emails = load_csv_files(folder_path)
    unique_emails = remove_duplicates(all_emails)
    save_unique_emails(unique_emails, output_path)

    print(f'{len(unique_emails)} unique email addresses saved to {output_path}.')

if __name__ == "__main__":
    main()