<h1 align="center">Building REST APIs with Flask</h1>
<hr>

## What is a REST API?

- REST (Representational State Transfer) is an architectural style for designing networked applications. A RESTful API is a set of rules and conventions for building and interacting with web services. It uses standard HTTP methods (GET, POST, PUT, DELETE) to perform CRUD operations (Create, Read, Update, Delete) on resources.

<hr>

### HTTP Methods
- HTTP methods define the actions a client can perform on a resource. In the context of REST APIs:
  - `GET`: Used to retrieve data from the server. It is safe and idempotent, meaning it doesn't modify the server's state.
  - `POST`: Used to create new data on the server. It is not idempotent as it creates a new resource with each request.
  - `PUT`: Used to update existing data on the server. It is idempotent as subsequent requests don't change the resource differently.
  - `DELETE`: Used to remove data from the server. It is idempotent as it consistently deletes the resource.

<br>

### Status Codes
- HTTP status codes are three-digit numbers returned by the server to indicate the result of a client's request. Some common status codes are:
  - `200 OK`: The request was successful, and the server returns data.
  - `201 Created`: The request was successful, and the server created a new resource.
  - `400 Bad Request`: The client's request is invalid or malformed.
  - `404 Not Found`: The requested resource does not exist.
  - `500 Internal Server Error`: An unexpected error occurred on the server.

<hr>
<br>

## Creating a Simple REST API in Flask

Let's create a basic REST API for managing tasks using Flask:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (list of tasks)
tasks = []

# Route to get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks}), 200

# Route to create a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' in data:
        task = {'title': data['title']}
        tasks.append(task)
        return jsonify({'message': 'Task created successfully'}, 201)
    else:
        return jsonify({'message': 'Title is required'}, 400)

# Route to update a task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id < len(tasks):
        data = request.get_json()
        if 'title' in data:
            tasks[task_id]['title'] = data['title']
            return jsonify({'message': 'Task updated successfully'})
        else:
            return jsonify({'message': 'Title is required'}, 400)
    else:
        return jsonify({'message': 'Task not found'}, 404)

# Route to delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Task not found'}, 404)

if __name__ == '__main__':
    app.run()
```

<br>

Let's break down the example code step by step:

1. Importing Dependencies:
   ```python
   from flask import Flask, request, jsonify
   ```
   - Here, we import the necessary modules from Flask. `Flask` is the main class for creating a Flask application, `request` is used to handle incoming requests, and `jsonify` is used to create JSON responses.

2. Creating a Flask Application:
   ```python
   app = Flask(__name__)
   ```
   - This line creates a Flask application instance.

3. Sample Data:
   ```python
   tasks = []
   ```
   - We define an empty list called `tasks` to store task data. In a real application, this would typically be a database.

4. Getting All Tasks:
   ```python
   @app.route('/api/tasks', methods=['GET'])
   def get_tasks():
       return jsonify({'tasks': tasks}), 200
   ```
   - We define a route for handling GET requests to retrieve all tasks. When the `/api/tasks` URL is accessed with a GET request, the `get_tasks` function is executed.
   - The function returns a JSON response containing the list of tasks along with the HTTP status code `200 OK`.

5. Creating a New Task:
   ```python
   @app.route('/api/tasks', methods=['POST'])
   def create_task():
       data = request.get_json()
       if 'title' in data:
           task = {'title': data['title']}
           tasks.append(task)
           return jsonify({'message': 'Task created successfully'}, 201)
       else:
           return jsonify({'message': 'Title is required'}, 400)
   ```
   - We define a route for handling POST requests to create a new task. When a POST request is made to `/api/tasks`, the `create_task` function is called.
   - The function first extracts JSON data from the request using `request.get_json()`.
   - It checks if the JSON data contains a 'title' field. If it does, a new task is created and added to the `tasks` list.
   - The function returns a JSON response with a success message and the HTTP status code `201 Created` if the task is created successfully. If the 'title' is missing, it returns a JSON response with an error message and the HTTP status code `400 Bad Request`.

6. Updating a Task:
   ```python
   @app.route('/api/tasks/<int:task_id>', methods=['PUT'])
   def update_task(task_id):
       if task_id < len(tasks):
           data = request.get_json()
           if 'title' in data:
               tasks[task_id]['title'] = data['title']
               return jsonify({'message': 'Task updated successfully'})
           else:
               return jsonify({'message': 'Title is required'}, 400)
       else:
           return jsonify({'message': 'Task not found'}, 404)
   ```
   - We define a route for handling PUT requests to update an existing task. When a PUT request is made to `/api/tasks/<task_id>`, the `update_task` function is called.
   - The `<int:task_id>` part in the URL captures the `task_id` as an integer parameter.
   - The function first checks if the provided `task_id` is within the valid range (i.e., it's a valid index in the `tasks` list).
   - It then extracts JSON data from the request and checks if it contains a 'title' field. If both conditions are met, the task's title is updated.
   - The function returns a JSON response with a success message. If the `task_id` is out of range or the 'title' is missing, it returns the appropriate error response with the corresponding status code.

7. Deleting a Task:
   ```python
   @app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
   def delete_task(task_id):
       if task_id < len(tasks):
           del tasks[task_id]
           return jsonify({'message': 'Task deleted successfully'})
       else:
           return jsonify({'message': 'Task not found'}, 404)
   ```
   - We define a route for handling DELETE requests to delete a task. When a DELETE request is made to `/api/tasks/<task_id>`, the `delete_task` function is called.
   - Like in the previous example, `<int:task_id>` captures the `task_id` as an integer parameter.
   - The function checks if the provided `task_id` is within the valid range. If it is, it deletes the task from the `tasks` list.
   - The function returns a JSON response with a success message. If the `task_id` is out of range, it returns an error response with the status code `404 Not Found`.

8. Running the Flask Application:
   ```python
   if __name__ == '__main__':
       app.run()
   ```
   - This code block ensures that the Flask application runs when this script is executed directly. It's a common practice to include this in Flask applications.

In summary, this Flask application provides a basic REST API for managing tasks, including creating, retrieving, updating, and deleting tasks. It demonstrates how to define routes, handle different HTTP methods, and return appropriate JSON responses with status codes. This is a foundational example that can be extended to build more complex APIs.

<hr>

### Additional Resource:

* <a href="https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24">Creating RESTful Web APIs using Flask and Python</a>

* <a href="https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/">Python | Build a REST API using Flask</a>
