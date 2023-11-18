import requests

# API endpoint (example using JSONPlaceholder API)
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# Sending a GET request
response = requests.get(api_url)

# Handling the response
if response.status_code == 200:
    # Response content as JSON
    data = response.json()
    title = data["title"]
    body = data["body"]
    print(f"Title: {title}")
    print(f"Body: {body}")
else:
    print(f"Request failed with status code: {response.status_code}")