<h1 align="center">Query String Parameters, Headers, Body</h1>

<hr>

## Query string parameters:

Used to customize and refine API requests by adding extra information to the URL. They play a crucial role in filtering, sorting, paginating, and customizing data retrieval from APIs.

Example Code:

```python
import requests

# Base API URL
base_url = "https://api.example.com/products"

# Query parameters
params = {
    "category": "electronics",
    "sort": "desc",
    "page": 1,
    "per_page": 10
}

# Adding query parameters to the URL
response = requests.get(base_url, params=params)

# The full URL with query parameters is constructed automatically
print("Full URL:", response.url)

# Sending the GET request
if response.status_code == 200:
    products_data = response.json()  # Assuming the response contains JSON data
    print("Products Data:", products_data)
else:
    print("API request failed with status code:", response.status_code)
```

In this example, we specify query parameters in the `params` dictionary and pass it as an argument to the `requests.get()` method. The `requests` library automatically constructs the full URL with the query parameters, and we make the API request to retrieve data based on our customization.

<hr>
<br>

## Headers 
Are metadata included in requests and responses to provide crucial information and instructions. They play various roles, including authentication, content type specification, user agent identification, caching directives, security enhancements, and more. Two common headers are 'User-Agent,' which identifies the client making the request, and 'Authorization,' which conveys authentication credentials. These headers are set and utilized in Python using the `requests` library to customize API requests. Headers are essential for conveying context and controlling the behavior of HTTP communication.

Example Code:

```python
import requests

# API endpoint
api_url = "https://api.example.com/data"

# Custom headers
headers = {
    "User-Agent": "MyCustomApp/1.0",
    "Authorization": "Bearer your-access-token"
}

# Sending a GET request with custom headers
response = requests.get(api_url, headers=headers)

# Display response and headers
print("Response Status Code:", response.status_code)
print("Response Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")

# Response content (in this case, it's just an example)
print("Response Content:", response.text)
```

In this code, we set the 'User-Agent' to "MyCustomApp/1.0" and the 'Authorization' header with an access token. The output will include the HTTP status code, response headers, and the response content. Custom headers help convey additional information to the server, such as identifying the client and providing authorization credentials.

<hr>
<br>


## Request bodies 
Used for sending data to the server, primarily in POST and PUT requests. POST requests create new resources, and PUT requests update existing resources. To send data in the request body using Python's `requests` library, format the data and include it using the `data` or `json` parameter. For example, you can send JSON data in the request body to create or update resources on the server. The format and requirements for the data in the request body depend on the API's specifications.

Example Code:

```python
import requests

# Example API endpoints
post_url = "https://api.example.com/create"
put_url = "https://api.example.com/update/123"  # Assuming 123 is the resource ID

# Data to be sent in the request body (in JSON format)
data = {
    "name": "John Doe",
    "email": "johndoe@example.com"
}

# POST request with data in the request body
post_response = requests.post(post_url, json=data)

# PUT request to update a resource with new data
put_response = requests.put(put_url, json=data)

# Handling the responses
print("POST Response:", post_response.status_code)
print("PUT Response:", put_response.status_code)
```

In this example, we format the data as a JSON object and use the `json` parameter when making POST and PUT requests. The data in the request body is sent to the respective API endpoints, allowing you to create a new resource in the case of POST and update an existing resource with PUT.

Remember that the format of the data in the request body depends on the API's requirements, which should be specified in the API's documentation.
<br>
<hr>

#### Additional Resources:

* <a href="https://www.youtube.com/watch?v=p2rQ88l0wvw">REST API Headers vs Path Parameters vs Query Parameters vs Body</a>

* <a href="https://www.geeksforgeeks.org/python-requests-post-request-with-headers-and-body/">Python requests – POST request with headers and body</a>

<hr>
<br>

<h1 align="center">CHALLENGE TIME!!!</h1>

API Endpoint: https://jsonplaceholder.typicode.com/posts

Follow the steps:

1. Set Custom Headers:
   - Construct a GET request to the API endpoint.
   - Set a custom 'User-Agent' header to identify your request as 'MyApp/1.0'.

2. Send the GET Request:
   - Send the GET request with the custom header to retrieve a list of posts.

3. Inspect the Response:
   - Display the HTTP status code, response headers, and response content.

4. Prepare Data for POST Request:
   - Create a dictionary with post information, including 'title' and 'body.'

5. Send a POST Request:
   - Construct a POST request to the API endpoint to create a new post.
   - Include the data dictionary in the request body as JSON.

6. Inspect the POST Response:
   - Display the HTTP status code and response content to confirm the post creation.
