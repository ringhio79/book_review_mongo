import os
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'book_reviews'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)

@app.route("/")
def home_page():
    return render_template('index.html', authors = mongo.db.authors.find())
    
@app.route('/book_list')
def book_list():
    return render_template('booklist.html',  books = mongo.db.books.find())


# @app.route('/book_list/<books_author>')
# def books_by_author(author):
#     if author == mongo.db.books.find()
#     return render_template(booklist.html, )
    
    
    
@app.route('/book_details/<books_id>')
def book_details(books_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(books_id)})
    return render_template('bookdetails.html',  book = the_book)

@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        new_book = mongo.db.books.insert_one(request.form.to_dict())
        return redirect(url_for('book_details', books_id=new_book.inserted_id))
    else:
        return render_template('addbook.html')
    
@app.route('/add_author', methods=['POST', 'GET'])
def add_author():
    if request.method == 'POST':
        mongo.db.authors.insert_one(request.form.to_dict())
        return redirect(url_for('home_page'))
    else:
        return render_template('addauthor.html')
        

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)