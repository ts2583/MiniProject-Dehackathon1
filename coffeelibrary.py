
import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


@app.route("/", methods=["GET", "POST"])
def home():
    books = Book.query.all()
    # result = books_schema.dump(books)

    return render_template("home.html", book_list = books)


@app.route("/reciept", methods=["GET", "POST"])
def receipt():

    return render_template("admin.html")

@app.route("/admin", methods=["GET", "POST"])
def admin():

    return render_template("admin.html")


class Book(db.Model):
    title = db.Column(db.String(100), unique=True)
    author = db.Column(db.String(100))
    year = db.Column(db.String(30))
    ISBN = db.Column(db.String(30), primary_key=True)
    copies = db.Column(db.Integer)

    def __init__(self, title, author, year, ISBN, copies):
        self.title = title
        self.author = author
        self.year = year
        self.ISBN = ISBN
        self.copies = copies


class BookSchema(ma.Schema):
    class Meta:
        fields = ('ISBN', 'title', 'author', 'year', 'copies')


book_schema = BookSchema()
books_schema = BookSchema(many=True)

if __name__ == '__main__':
    app.run(debug=True)
