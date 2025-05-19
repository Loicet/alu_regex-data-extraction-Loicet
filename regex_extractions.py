import re

# 1. Email validation
def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)

# 2. URL validation
def extract_urls(text):
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

# 3. Phone number validation
def extract_phone_numbers(text):
    pattern = r'(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'
    return re.findall(pattern, text)

# 4. Credit card validation
def extract_credit_cards(text):
    pattern = r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'
    return re.findall(pattern, text)

# 5. Hashtag validation
def extract_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)


# Sample input string (you can replace this with API response or file input)
sample_text = """
user@example.com
firstname.lastname@company.co.uk
https://www.example.com
https://subdomain.example.org/page
(123) 456-7890
123-456-7890
123.456.7890
1234 5678 9012 3456
1234-5678-9012-3456
#example
#ThisIsAHashtag
"""