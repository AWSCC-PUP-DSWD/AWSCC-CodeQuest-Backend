from flask import Blueprint, render_template, request, redirect, url_for
from .model import Book
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    books = Book.query.all()
    return render_template("home.html", books=books)

@views.route("/add", methods=["POST"])
def add_book():
    author = request.form.get('author')
    title = request.form.get('title')
    published_year = request.form.get('published_year')
    new_book = Book(title=title, author=author, published_year=published_year)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('views.home'))

@views.route("/update/<id>", methods=["PATCH"])
def update_book(id):
    
    # get data from form
    author = request.json.get('author')
    title = request.json.get('title')
    published_year = request.json.get('publishedYear')
    
    # updates
    book = Book.query.get(id)
    book.author = author
    book.title = title
    book.published_year = published_year
    db.session.commit()
    return ({"result": "success"})

@views.route("/delete/<id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return ({"results": "success"})
    return ({"results": "error"})
    