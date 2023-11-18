<h1 align="center">Introduction to SQLite</h1>

On Day 24, we're finally getting our hands dirty with the database. 

As you progress in *CodeQuest: 30 Days of Cosmic Coding*, you've likely covered a lot of ground in Python and Flask. Today's lesson opens the door to a fundamental aspect of backend development: **working with databases**.

### Database

**Databases** are the backbone of most web applications, storing and managing data, and allowing you to retrieve and manipulate information efficiently.

### Why SQLite?

Before we dive into SQLite, it's essential to understand the variety of database management systems available. There are several DBMS options out there, each with its strengths and weaknesses. Let's take a brief look at why we've chosen SQLite for your journey:

##### Pros of SQLite:

1. Ease of Use: SQLite is known for its simplicity. You don't need a separate server or complex setup; it's just a library that you can link to your Python project.

2. Serverless: Unlike some DBMS options, SQLite is serverless, which means it's self-contained and doesn't require an external process running.

3. Zero Configuration: You don't need to perform any extensive configuration or maintenance tasks. It's nearly hassle-free.

##### Cons of SQLite:

1. Limited Concurrent Access: SQLite is suitable for small to medium-sized projects but may not handle high levels of concurrent access as well as some other DBMS systems.

2. No User Management: It lacks built-in user management features, which can be a limitation in multi-user applications.

3. Not Ideal for Large Datasets: It's not the best choice for massive datasets due to performance limitations.

---

### SQLite

If you haven't installed SQLite yet, you can watch [this video](https://www.youtube.com/watch?v=XA3w8tQnYCA).

Now that we've chosen SQLite, it's time to learn the basics. Here are some key points to get us started:

#### Basic Operations in SQLite:

- Creating a Database

Before we can perform any operations in SQLite, we first need to connect to a database or create a new one:

```sh
sqlite3 new_db.db;
```

This will connect us to the `new_db` database.

To show the list of databases, use the `.databases` command.

- Creating tables

Tables are the structures that hold our data. We define the table schema when creating it. Here's how you create a simple table to store information about books:

```sql
-- Create a table to store book information
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    published_year INTEGER NOT NULL
);
```

The `CREATE TABLE` command is used to create a new table named `books`. The columns (id, title, author, published_year) are declared with their respective data types, the `id` being the primary key of the table to ensure that each row has a unique identifier.

- Inserting Data

To add data to our newly created table, you can use the `INSERT INTO` statement:

```sql
-- Insert a new book record
INSERT INTO books (title, author, published_year) VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960);
```

- Retrieving Data

You can query your database to retrieve data using the `SELECT` statement:

```sql
SELECT * FROM books;
```

The `SELECT` statement returns all records from the books table. You can customize your query with conditions, sorting, and more.

- Updating Data

To modify existing records, use the UPDATE statement:

```sql
-- Update a book's author
UPDATE books SET author = 'Harper Lee, Jr.' WHERE title = 'To Kill a Mockingbird';
```

In this example, the author's name is updated for the book with the specified title.

- Deleting Data

To remove records from the database, use the DELETE statement:

```sql
-- Delete a book record
DELETE FROM books WHERE title = 'To Kill a Mockingbird';
```

This statement deletes the book record with the specified title from the books table.

These are the fundamental SQL operations you'll commonly use when working with SQLite. Learning how to create tables, insert, retrieve, update, and delete data is a must-know for building and maintaining databases. For the next day, we'll be integrating our SQLite knowledge to Python's Flask!

### Additional Resources

- [What is SQLite? And When to Use it?](https://www.simplilearn.com/tutorials/sql-tutorial/what-is-sqlite)

- [Introduction to SQLite](https://www.geeksforgeeks.org/introduction-to-sqlite/)

- [SQLite Tutorial - A Step-by-step SQLite Tutorial](https://www.sqlitetutorial.net)