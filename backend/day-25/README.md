<h1 align="center">Setting up SQLite in Flask</h1>

---

Now that we've learned about SQLite, let's go straight ahead to Flask and integrate these two powerful tools together!

### Setting Up SQLite in Flask


1. Import SQLite and Flask

    The first step is to import Flask and SQLite into your Python script. You can do this with the following code:

    ```python
    from flask import Flask
    import sqlite3
    ```

2. Create a Flask App

    Next, create a Flask app and specify a configuration setting to tell Flask where to find your SQLite database file. The code looks like this:

    ```python
    app = Flask(__name__)
    app.config["DB_NAME"] = "books.db"
    ```

3. Initialize a Database

    Before we connect to the database, we first need to initialize it by creating a new table in our `books.db`.

    In a new python file called `init_db.py`, we will create a script that will drop the table if it is already existing and create a new table:

    ```python
    import sqlite3

    conn = sqlite3.connect('books.db')

    with open("schema.sql") as f:
        conn.executescript(f.read())

    cur = conn.cursor()

    cur.execute('''
                INSERT INTO books (title, author, published_year) 
                VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960);
                ''')

    conn.commit()
    conn.close()
    ```

    Now, create a new file called `schema.sql` that will contain the following SQL commands that we have learned in the previous lesson:

    ```sql
    DROP TABLE IF EXISTS books;

    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        published_year INTEGER NOT NULL
    );
    ```

    Then run the `init_db.py`:

    ```python
    python init_db.py
    ```

4. Connect to the Database

    Next, we'll create a function that will connect us to the SQLite database:

    ```python
    def get_db():
        db = sqlite3.connect(app.config["DB_NAME"])
        db.row_factory = sqlite3.Row
        return db
    ```

5. Create a New Route

    ```python
    @app.route("/") 
    def index():    
        conn = get_db()
        books = conn.execute("SELECT * FROM books").fetchall()
        conn.close()
        return render_template('index.html', books=books)
    ```
6. Create an HTML File to Render the Data using Jinja

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Books:</h1>
        <ul>
            {% for book in books %}
            <li><b>{{ book.title }}</b> written by {{ book.author }}</li>        
            {% endfor %}
        </ul>
    </body>
    </html>
    ```

And the output should look like this:

![Day 25 Output Image](image.png)

To try the program that we created, you can check the `projects` folder from our root directory and you should see the `day-25` folder inside it that contains the files used in this lesson.


### Additional Resources

- [Using SQLite 3 with Flask](https://flask.palletsprojects.com/en/3.0.x/patterns/sqlite3/)