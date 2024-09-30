import pandas as pd
import re
import os
import dns.resolver

# Email regex for basic validation
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# List of disposable email domains (add more as needed)
disposable_domains = {'tempmail.com', 'mailinator.com', '10minutemail.com'}


# Function to validate email
def is_valid_email(email):
    if re.match(email_regex, email):
        domain = email.split('@')[-1]

        # Check if the domain is disposable
        if domain.lower() in disposable_domains:
            return False

        try:
            # Check via DNS
            records = dns.resolver.resolve(domain, 'MX')
            return bool(records)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            return False
    return False


def load_csv_files(folder_path):
    all_emails = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            # Ensure the column name matches your CSV structure
            if 'Email 1' in df.columns:
                emails = df['Email 1'].tolist()
                all_emails.extend(emails)
    return all_emails


def remove_duplicates(email_list):
    return list(set(email_list))  # Remove duplicates using a set


def validate_emails(email_list):
    valid_emails = []
    invalid_emails = []

    for email in email_list:
        if is_valid_email(email):
            valid_emails.append(email)
        else:
            invalid_emails.append(email)

    return valid_emails, invalid_emails


def save_emails(emails, output_path):
    df = pd.DataFrame(emails, columns=['email'])
    df.to_csv(output_path, index=False)


def main():
    folder_path = '/Users/annawilliams/Desktop/emailsValidator'
    valid_output_path = '/Users/annawilliams/Desktop/emailsValidator/valid_emails.csv'
    invalid_output_path = '/Users/annawilliams/Desktop/emailsValidator/invalid_emails.csv'

    # Load all emails from CSV files
    all_emails = load_csv_files(folder_path)

    # Remove duplicates
    unique_emails = remove_duplicates(all_emails)

    # Validate emails
    valid_emails, invalid_emails = validate_emails(unique_emails)

    # Save valid and invalid emails
    save_emails(valid_emails, valid_output_path)
    save_emails(invalid_emails, invalid_output_path)

    print(f'{len(valid_emails)} valid email addresses saved to {valid_output_path}.')
    print(f'{len(invalid_emails)} invalid email addresses saved to {invalid_output_path}.')


if __name__ == "__main__":
    main()