<h1 align="center">Jinja</h1>
<hr>

Jinja2 is a powerful and user-friendly templating engine used in Flask, a Python web framework. It allows you to create dynamic and interactive web pages by embedding Python code within HTML templates. 

<br>

## What Is Jinja2?

Think of Jinja2 as a magic tool that helps you generate web pages with dynamic content. Instead of writing plain HTML, you can use Jinja2 to mix HTML with Python-like code. This means you can create web pages that display different content based on data from your Python application.

### Using Jinja2 in Flask:

1. Template Files:

   First, you create HTML templates that contain placeholders for dynamic content. These placeholders are enclosed in double curly braces `{{ }}`.

   ```html
   <html>
   <head>
       <title>{{ title }}</title>
   </head>
   <body>
       <h1>Welcome, {{ user }}!</h1>
   </body>
   </html>
   ```

   In this example, `{{ title }}` and `{{ user }}` are placeholders for dynamic data.

2. Rendering Templates:

   In your Python code (your Flask application), you render these templates using Jinja2. You pass data to the templates using these placeholders.

   ```python
   from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       title = "My Web App"
       user = "Alice"
       return render_template('index.html', title=title, user=user)
   ```

   The `render_template` function takes the template name ('index.html') and the data ('title' and 'user') as arguments.

3. Dynamic Content:

   When a user visits your web page, Jinja2 replaces the placeholders with the actual data. In this case, the page title becomes "My Web App," and the user sees "Welcome, Alice!"

   This allows you to create web pages that adapt to different users and display real-time data.

<br>

Example Output:

If you run your Flask application and visit the root URL (http://localhost:5000/), you'll see a web page with the title "My Web App" and a welcome message customized for the user Alice.

### Additional Features:

- Jinja2 supports conditional statements, loops, and filters, enabling you to create complex web pages.
- You can include other templates within your templates for reusability.
- Jinja2 provides an escape mechanism to prevent code injection, making your web application more secure.

In summary, Jinja2 in Flask is a fantastic tool that allows you to create dynamic, personalized, and interactive web pages by embedding Python-like code within HTML templates. It's a fundamental part of Flask that makes web development more accessible and powerful.

<hr>
<br>


## Static and Templates Folder:

In Flask, the "static" and "templates" folders serve different purposes and are essential for organizing web applications:

1. Static Folder:
   - The "static" folder is used to store static assets, such as stylesheets (CSS), client-side JavaScript, images, and other files that do not change dynamically. These assets are typically served directly to the client's web browser.
   - When a web page is loaded, the HTML content may reference external static assets, like CSS and JavaScript files. The "static" folder provides a convenient location to store these files. Flask can serve these static assets using the `url_for('static', filename='...')` function, making it easy to reference them in your HTML templates.
     
Example:
```python
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

2. Templates Folder:
   - The "templates" folder is used to store HTML templates that define the structure and layout of web pages. These templates can contain placeholders and dynamic content, which Flask can fill in with actual data when rendering web pages.
   - HTML templates are a fundamental part of web development. They allow you to create reusable layouts for your web pages, separating the structure from the content. Flask uses a templating engine, such as Jinja2, to render these templates dynamically. When you render a template, you can pass data from your Python code to fill in the placeholders in the HTML.
     
Example:
```python
from flask import Flask, render_template

@app.route('/about')
def about():
    title = 'About Us'
    content = 'Welcome to our About Us page!'
    return render_template('about.html', title=title, content=content)
```
```html
<!-- templates/about.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
</body>
</html>
```

In summary, the "static" folder is used for storing static assets like CSS, JavaScript, and images, while the "templates'' folder is used for storing HTML templates that define the structure of web pages. Flask serves static assets directly to the client, and it uses templates to render dynamic web pages by filling in placeholders with data provided by the server.

<hr>

## Additional Resource:

* <a href="https://www.geeksforgeeks.org/templating-with-jinja2-in-flask/">Templating With Jinja2 in Flask</a>


