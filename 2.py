import re
emails = ["user@example.com", "invalid.email", "test_123@domain.co.uk", "@nodomain.com"]
pattern = r"^[A-Za-z0-9_]+@[A-Za-z0-9-.]+\.[A-Za-z]{2,}$"

for email in emails:
    if re.match(pattern, email):
        print("valid")
    else:
        print("Invalid")

