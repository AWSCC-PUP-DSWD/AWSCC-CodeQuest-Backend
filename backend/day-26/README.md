<h1 align="center">Defining and Creating Database Tables using SQLAlchemy and ORM</h1>

---

After integrating SQLite and Flask, it's time for an even more powerful upgrade - SQLAlchemy and ORMs.

### What is SQLAlchemy

**SQLAlchemy** is a Python library that serves as a bridge between our Python code and a relational database. It allows us to work with databases using Python, making the process more intuitive and less error-prone.

**Key Features of SQLAlchemy:**

- Abstraction of database complexities.

- Support for multiple database engines (e.g., SQLite, PostgreSQL, MySQL).

- An Object-Relational Mapping (ORM) system for interacting with databases.

### What is an ORM

**Object-Relational Mapping (ORM)** is a programming technique that lets you work with databases using objects and classes instead of writing raw SQL queries. SQLAlchemy includes a powerful ORM system that simplifies database interactions.

Advantages of ORM:

- Mapping Python objects to database tables.

- Automatic SQL generation, reducing manual query writing.

- Enhanced data abstraction and security.

### Defining and Creating Database Using SQLAlchemy

Now, let's get practical. Here's a step-by-step guide on how to define and create database tables using SQLAlchemy and ORM in Flask:

1. Install Dependencies

    We'll start by installing Flask and Flask-SQLAlchemy. Be sure to create a virtual environment for this tutorial.

    ```python
    pip install Flask
    pip install Flask-SQLAlchemy
    ```

2. Create Flask App

    ```python
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_books.db'
    db = SQLAlchemy(app)
    ```

3. Define a Model

    Next, we'll create a Python class to represent a table in our database. Recall the OOP concepts we have learned previously as it all applies in this scenario:

    ```python
    class Books(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(80), unique=True, nullable=False)
        author = db.Column(db.String(120), unique=True, nullable=False)
        published_year = db.Column(db.Integer, nullable=False)

        def __repr__(self):
            return f'<Book {self.title}-{self.author}>'
    ```

    The `db.Model` gets inherited by the newly created class `User`.

4. Create the Database

    ```python
    db.create_all()
    ```

5. Interact with the Database

    We can interact with your database using Python objects, making operations like adding, querying, and updating records straightforward. For example:

    ```python
    new_book = Book(title="To Kill a Mockingbird", author="Harper Lee", published_year=1960)
    db.session.add(new_book)
    db.session.commit()
    ```

    or get all the data in the database:

    ```python
    books = Book.query.all()
    ```

And we did it! SQLAlchemy and ORM simplify database management in our Flask application. You can try running a sample project using these tools in the `projects/day-26` folder.

---

### Additional Resources

- [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)

- [How to Use Flask-SQLAlchemy to Interact with Databases in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application)

- [Flask SQLAlchemy (with Examples)](https://pythonbasics.org/flask-sqlalchemy/)

- [Quick Start — Flask-SQLAlchemy Documentation (3.0.x)](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/)