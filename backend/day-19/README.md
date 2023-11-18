<h1 align="center">Request and Response Handling</h1>

<hr>

## Recap of Day 18:

On Day 18, we delved into the intricacies of crafting more sophisticated API requests. We explored the role of query string parameters in customizing requests to filter, sort, and paginate data. Additionally, we discovered how to set custom headers in requests, conveying information like the user agent and authentication. The day also covered the handling of request bodies, especially for methods like POST and PUT, to send data to the server for resource creation and updates.

<hr>
<br>

### Handling Requests in the Requests Library:

Today is all about understanding how to handle requests in the `requests` library and how to modify and customize those requests according to specific needs. Here's an overview of how to do this:

1. Sending Requests: To send a request using the `requests` library, you use one of the HTTP methods like GET, POST, PUT, or DELETE. These methods correspond to the action you want to perform on a resource, such as retrieving data (GET), creating data (POST), updating data (PUT), or deleting data (DELETE).

2. Customizing Requests: You can customize your requests by adding various elements to them, including:
   - Headers: Headers are used to convey additional information about the request. You can set custom headers to specify details like the user agent or authentication information.
   - Query Parameters: Query parameters are used to filter or sort data in the request. You can add query parameters to the URL to refine your request's results.
   - Request Body: For methods like POST and PUT, you can send data in the request body. This is often used to create or update resources.

Example Code:

```python
import requests

# API endpoint (example using JSONPlaceholder API)
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# Custom headers
headers = {"User-Agent": "MyApp/1.0"}

# Query parameters
params = {"_format": "json"}

# Request body (for POST or PUT requests)
data = {"title": "New Post", "body": "This is a new post."}

# Sending a GET request with custom headers and query parameters
response = requests.get(api_url, headers=headers, params=params)

# Sending a POST request with a request body (commented out)
# response = requests.post(api_url, json=data)

# Handling the response
print(f"Response Status Code: {response.status_code}")
print("Response Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")
print("Response Content:")
print(response.text)
```

In this example, a GET request is sent to the JSONPlaceholder API endpoint with custom headers and query parameters. There's also a commented-out section for making a POST request with a request body. The response is then handled, and various elements, including the status code, headers, and content, are printed.

<hr>
<br>

### Response Handling:

Handling API responses is a crucial aspect of interacting with web services and APIs. Here are the key steps and considerations for response handling:

1. Accessing the Response:
   - After sending a request using the `requests` library, the response is obtained as an object. You can access this response object to retrieve various components, including the HTTP status code, headers, and the response content.

2. Response Status Code:
   - The HTTP status code is a three-digit number that indicates the outcome of the request. A status code in the 200s typically signifies a successful request, while codes in the 400s and 500s indicate errors.

3. Response Headers:
   - Response headers contain metadata about the response, such as the content type and server information. You can access and process these headers as needed.

4. Response Content:
   - The response content is often the most critical part of the response. It contains the data returned by the API, usually in JSON, XML, HTML, or other formats.

5. JSON Parsing:
   - JSON is a common data format used in API responses. You can parse JSON content using Python's `json` module to convert it into Python data structures (e.g., dictionaries or lists) for further processing.

6. Handling Errors:
   - API responses may include error information in the content or headers. It's important to handle errors gracefully, such as by checking for non-200 status codes and taking appropriate actions.

7. Extracting Data:
   - Extracting specific data from the response content is essential. You can use Python's data manipulation techniques to access the data elements you need for your application.

Example Code:

```python
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
```

In this example, we send a GET request to the JSONPlaceholder API, access the response content as JSON, and extract specific data (title and body) from the response. We also check for errors by examining the status code.

<br>
<hr>

#### Additional Resources:

* <a href="https://realpython.com/python-requests/">Python’s Requests Library (Guide)</a>

* <a href="https://www.geeksforgeeks.org/response-methods-python-requests/">Response Methods – Python requests</a>

<hr>
<br>

<h1 align="center">CHALLENGE TIME!!!</h1>

- API: SpaceX API
- Documentation: https://github.com/r-spacex/SpaceX-API
- Endpoint: https://api.spacexdata.com/v5/launches/latest


Create a Python program that interacts with the SpaceX API to retrieve information about the latest SpaceX launch. You can send a GET request to the API endpoint mentioned above to get details about the latest SpaceX launch. Remember to handle the response, parse the JSON content, and display the launch information in a user-friendly format.


