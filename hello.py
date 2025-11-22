import requests

# Make a GET request to a URL
response = requests.get("https://api.github.com/users/octocat")

# Check the status code
print(f"Status Code: {response.status_code}")