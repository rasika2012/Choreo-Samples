import requests
import re

# URL to fetch the data from
url = "https://punchicar.com/inventory-2/?make=suzuki&serie=alto&ajax_action=listings-result"

# Fetch the content from the URL
response = requests.get(url)
response.raise_for_status()  # Raise an exception for HTTP errors

# Parse the JSON response
data = response.json()
match = re.search(r'Rs. ([0-9 ]+)',str(data))
if match:
    # price and replace Rs. with empty string
    price = match.group(0).replace("Rs. ", "").replace(" ", "")
    print(price) 
