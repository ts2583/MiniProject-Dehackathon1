import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

"""
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        """"""
            Within index.html there should be a post form, that is
            designed to take inputs from the user and those inputs
            should be (I don't know at the moment), but flask should
            recieve the book that the user decided to rent, and it
            should then redirect to display provided with the book
            infomation and also updating the database to confirm
            that someone has rented a book and there's one less copy
            of it.
        """"""
        return redirect(url_for('display')) #this will display it, as well as pass a Book Information
    else: #our gets
        """"""
            This section should work with the database to creates
            a list of Books, and pushes within
            render_template function, and showcase it using jinja
            on a html file.
        """"""
        return render_template("index.html" )


@app.route('/display', methods=["GET"])
def display():



    """"""
        This is very simple, more or less what it's doing is acting as a receipt window to confirm
        to the user that everything is ok, and he's good to take the book home.

         More or Less this is tricky, because I don't have a concise way of passing data here,
         unless I add an parameter and set it to null by default, meaning that this page only
         exist whenever the main page has a result to display, but first I need to understand
         how to implement SQL

    """"""
    return render_template("display.html") #

@app.route('/admin', methods=["GET", "POST"])
def admin():
    """"""
    This is a bit interesting, we want to be able
    learn how to use POST or UPDATE through request
    this I really don't have a concise understanding but we can hack something
    and ask for advice for people who understand flask.

    But basically here we should have a page that is able to
    add new books, this is really easy to do just create
    a layout for the admin to do that, however in order for him
    to delete books we need to showcase a list of books he can
    delete or choose this is something I'm a bit stuck at understanding..

    :return:
    """"""

    if request.method == "POST":

    elif request.method == "UPDATE":

    else:
        return render_template("admin.html")
"""


# CRUD EXAMPLE
# Create Post
# Read GET
# Update PUT
# Delete Delete

# I've coded a basic layout
# of What I believe our backend
# should be, It it will provide
# a concise idea of how

@app.route('/addbook', methods=['POST'])
def add_book():
    author = request.json['author']
    title = request.json['title']
    year = request.json['year']
    ISBN = request.json['ISBN']
    copies = request.json['copies']

    new_book = Book(title, author, year, ISBN, copies)

    db.session.add(new_book)
    db.session.commit()

    return book_schema.jsonify(new_book)


@app.route('/getbook/<isbn>', methods=['GET'])
def get_book(isbn):
    book = Book.query.get(isbn)
    return book_schema.jsonify(book)


@app.route('/getbooks', methods=['GET'])
def get_books():
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result)


@app.route('/updatebook/<isbn>', methods=['PUT'])
def update_book(isbn):
    # We get a section of the database
    book = Book.query.get(isbn)

    book.author = request.json['author']
    book.title = request.json['title']
    book.year = request.json['year']
    book.ISBN = request.json['ISBN']
    book.copies = request.json['copies']
    # We get the new contents sent from as an PUT request
    db.session.commit()

    return book_schema.jsonify(book)


@app.route('/deletebook/<isbn>', methods=['DELETE'])
def delete_product(isbn):
    book = Book.query.get(isbn)
    db.session.delete(book)
    db.session.commit()


# init db
db = SQLAlchemy(app)

# init ma
ma = Marshmallow(app)


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
