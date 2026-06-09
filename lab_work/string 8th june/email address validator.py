# The input email to be checked
email = "rahul.sharma2026@gmail.com"

# 1. & 2. Split the email at '@' to get the username and the rest (domain + extension)
# 'rahul.sharma2026' goes to username, 'gmail.com' goes to rest
username, domain_part = email.split('@')

# 3. Split the domain_part at '.' to get the domain and extension
# 'gmail' goes to domain, 'com' goes to extension
domain, extension = domain_part.split('.')

# 4. Count how many numbers (digits) are in the username
digits_count = sum(c.isdigit() for c in username)

# 5. Count special characters in the username (anything that isn't a letter or number)
special_count = sum(not c.isalnum() for c in username)

# 6. Check if the email is valid based on the rules
# Rule A: Does it have exactly one '@' symbol?
has_one_at = email.count('@') == 1

# Rule B: Is there at least one '.' after the '@' symbol?
has_dot_after_at = '.' in domain_part

# 7. Determine the final status message
if has_one_at and has_dot_after_at:
    status = "Valid"
else:
    status = "Invalid"

# Displaying the results exactly like the sample output
print(f"Email: {email}\n")
print(f"Username: {username}")
print(f"Domain: {domain}")
print(f"Extension: {extension}\n")
print(f"Digits Found: {digits_count}")
print(f"Special Characters Found: {special_count}\n")
print(f"Email Status: {status}")