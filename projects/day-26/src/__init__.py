from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "new_books.db"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .views import views
    app.register_blueprint(views, url_prefix="/")

    return app



