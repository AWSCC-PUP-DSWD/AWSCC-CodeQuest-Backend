<h1 align="center">HTTP Methods, Status Codes, Endpoints</h1>

From Day 17 - 19 we'll be learning about the Requests library and API interaction. For today, we will be focusing on HTTP Methods, Status Codes, and Endpoints.

<hr>

## What is HTTP (Hypertext Transfer Protocol)?

HTTP is like a language that computers use to talk to each other on the internet. It's the foundation of how web pages and information are sent from a server (a powerful computer) to your web browser (like Chrome or Firefox).

## How Does It Work?

Imagine you want to visit a web page, like your favorite news site. When you type the web address in your browser and hit "Enter," your browser sends a message to the news site's server using HTTP. This message is called an "HTTP request." It says, "Hey, I'd like to see your web page, please."

The server gets your request, finds the web page you want, and sends it back to your browser as an "HTTP response." Your browser then takes that response and shows you the web page on your screen.

### Key Points:

- HTTP is a way for your browser to ask for web pages and for servers to give them to you.
- It's like a conversation: your browser asks (HTTP request), and the server answers (HTTP response).
- HTTP is how the internet works, and it helps you see web pages, images, videos, and more.

<hr>
<br>

### Common HTTP Methods:

1. GET: The GET method is used to retrieve data from the server. It is safe and idempotent, meaning it should not modify server data and can be repeated without changing the result. GET requests are typically used for reading or fetching information. For example, when you visit a website, your browser sends a GET request to retrieve the web page.

2. POST: The POST method is used to send data to the server to create a new resource. It is not idempotent, meaning multiple requests may result in different outcomes. POST requests are commonly used when you submit forms or create new records. For example, when you fill out a registration form on a website, your data is sent to the server using a POST request.

3. PUT: The PUT method is used to update an existing resource on the server or create it if it doesn't exist. It should be idempotent, meaning making the same request multiple times should have the same result as making it once. PUT requests are often used to update information, such as modifying a user's profile.

4. DELETE: The DELETE method is used to request the removal of a resource from the server. It should also be idempotent, meaning multiple DELETE requests for the same resource won't change the result. DELETE requests are used to delete data, such as removing a user's account.

Example Code:
```python
import requests

# Example GET request to fetch user data
response = requests.get("https://api.example.com/users/123")
print("GET Response:", response.text)

# Example POST request to create a new user
new_user_data = {"username": "new_user", "email": "new@example.com"}
response = requests.post("https://api.example.com/users", json=new_user_data)
print("POST Response:", response.text)

# Example PUT request to update user information
updated_data = {"email": "updated@example.com"}
response = requests.put("https://api.example.com/users/123", json=updated_data)
print("PUT Response:", response.text)

# Example DELETE request to remove a user
response = requests.delete("https://api.example.com/users/123")
print("DELETE Response:", response.text)
```

<hr>
<br>

### HTTP Status Codes:

HTTP status codes are three-digit numbers that the server sends as part of an HTTP response to inform the client (e.g., a web browser or an API consumer) about the outcome of a request. These status codes help convey whether the request was successful, encountered an error, or requires further action. They are grouped into five classes, each with a specific meaning:

1. 1xx (Informational): These codes provide information about the request's progress, such as 100 (Continue), indicating that the request was received and the client can continue.

2. 2xx (Successful): These codes indicate that the request was received, understood, and processed successfully. For example, 200 (OK) signifies a successful request.

3. 3xx (Redirection): These codes inform the client that further action is needed to complete the request. For example, 301 (Moved Permanently) tells the client that the resource has moved to a different URL.

4. 4xx (Client Error): These codes indicate that the client has made an error or the request cannot be fulfilled. For instance, 404 (Not Found) is returned when the requested resource doesn't exist.

5. 5xx (Server Error): These codes signal that the server has encountered an error while processing the request. For instance, 500 (Internal Server Error) is a generic indication of server failure.

```python
import requests

# Checking the status code
response = requests.get('https://api.example.com/data')
if response.status_code == 200:
    print('Request was successful.')
```

<hr>
<br>

## API Endpoints:
	
API endpoints are like website addresses for specific tasks or information in a web service. They're URLs that let you do things or get data from the service.

### Structuring Endpoint URLs:

1. Base URL: 
The base URL represents the root of the API. It often includes the domain and the version of the API. For example, `https://api.example.com/v1`.

2. Resource Path: 
The resource path identifies the specific resource or action you want to access. It comes after the base URL and provides a clear indication of what the endpoint does. For example, `/users` might represent a collection of user data.

3. Parameters: 
Parameters are additional information that can be included in the endpoint URL to filter, sort, or customize the request. These parameters are typically added as query parameters using a question mark (?) and an ampersand (&) to separate multiple parameters. For example, `/users?status=active&sort=desc` might retrieve a list of active users sorted in descending order.

Example Code:

```python
import requests

# Base URL
base_url = "https://api.example.com/v1"

# Resource Path
resource_path = "/users"

# Parameters
parameters = {"status": "active", "sort": "desc"}

# Construct the complete endpoint URL
endpoint_url = base_url + resource_path

# Adding parameters to the URL
if parameters:
    endpoint_url += "?" + "&".join([f"{key}={value}" for key, value in parameters.items()])

# Sending a GET request to the constructed endpoint URL
response = requests.get(endpoint_url)

# Handle the response as needed
print("API Response:", response.text)
```

<hr>

### Additional Resources:

* <a href="https://www.geeksforgeeks.org/http-request-methods-python-requests/">Http Request methods – Python requests</a>
* <a href="https://www.tutorialspoint.com/http/index.htm">HTTP Tutorial</a>

<hr>
<br>

<h1 align="center">CHALLENGE TIME!!!</h1>

API endpoint: `https://jsonplaceholder.typicode.com/`

Perform the following tasks:
1. Make a GET request to the provided endpoint to fetch user information.
2. Check the status code of the response. If it's 200, print "Request successful." Otherwise, print "Request failed."

