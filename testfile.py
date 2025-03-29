import requests
from bs4 import BeautifulSoup

LOGIN_URL = "https://cses.fi/login"

# Create a session
client = requests.Session()

# Get login page
response = client.get(LOGIN_URL)
soup = BeautifulSoup(response.text, "lxml")

# Extract CSRF token
csrf_input = soup.select('input[name="csrf_token"]')

if not csrf_input:
    print("❌ CSRF token not found. The login page structure might have changed.")
else:
    csrf = csrf_input[0]['value']
    print(f"✅ CSRF token found: {csrf}")
