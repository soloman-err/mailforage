import re

# Text input:
text = input("""Paste your text here: """)

# Cheking pattern:
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[A-Za-z0-9-]{2,7}\b"

# Converting to lower case(if needed):
raw_emails = re.findall(pattern, text)

# Final output:
emails = [email.lower() for email in raw_emails]

print("Email address found in the text: ")
print(emails) 