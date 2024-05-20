import requests
import re

type = [{'make':"suzuki", 'series':"alto"}, {'make':"honda", 'series':"civic"}, {'make':"suzuki", 'series':"celerio"}]
# URL to fetch the data from

for i in type:
    url = f"https://punchicar.com/inventory-2/?make={i['make']}&serie={i['series']}&ajax_action=listings-result"

    # Fetch the content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    # Parse the JSON response
    data = response.json()
    match = re.search(r'Rs. ([0-9 ]+)',str(data))
    if match:
        # price and replace Rs. with empty string
        price = match.group(0).replace("Rs. ", "").replace(" ", "")
        print(i['series'] + ' , ' + price)

