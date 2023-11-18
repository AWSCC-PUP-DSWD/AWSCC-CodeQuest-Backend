from flask import Blueprint, render_template
from .model import Book
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    books = Book.query.all()
    return render_template("home.html", books=books)