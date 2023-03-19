from faker import Faker

fake = Faker()

name = fake.name()

email = fake.email()

phone_number = fake.phone_number()

# User Data

user_names = ['Alice', 'Bob', 'Charlie', 'David']
user_emails = ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com']
user_passwords = ['changeme', 'changeme', 'changeme', 'changeme']