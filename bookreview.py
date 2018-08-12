import os
import pymongo
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'book_reviews'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

@app.route('/')
def home_page():
    return render_template('index.html')
    
@app.route('/book_list')
def book_list():
    books = mongo.db.books.find()
    return render_template('booklist.html',  books = books)
    
@app.route('/book_details/<books_id>')
def book_details(books_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(books_id)})
    the_author = mongo.db.authors.find_one({"name": the_book['author']})
    return render_template('bookdetails.html',  book = the_book, author = the_author)


@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    genres = ['Romance', 'Crime', 'Thriller', 'Biograpy', 'Sci-Fi']
    if request.method == 'POST':
        checked_genres = []
        for checkbox in genres:
            value = request.form.get(checkbox)
            checked_genres.append(value)
            
        title = request.form[('title')]
        author = request.form[('author')]
        date_published = request.form[('date_published')]
        synopsis = request.form[('synopsis')]
        cover_image = request.form[('cover_image')]
        checked_genres = checked_genres
            
        new_book = {'title': title, 'author': author, 'date_published': date_published, 'synopsis': synopsis, 'cover_image': cover_image, 'genre': checked_genres}
        inserted_book = mongo.db.books.insert_one(new_book)
        return redirect(url_for('book_details', books_id=inserted_book.inserted_id))
    else:
        return render_template('addbook.html', genres = genres)   
        
@app.route('/authors')
def authors():
    authors_asc = mongo.db.authors.find().sort([("l_name", pymongo.ASCENDING)])
    return render_template('authors.html', authors = authors_asc)

@app.route('/author_details/<author_id>')
def author_details(author_id):
    the_author = mongo.db.authors.find_one({"_id": ObjectId(author_id)})
    books = mongo.db.books.find({'author': the_author['name']})
    return render_template('authordetails.html', author=the_author, books = books)

@app.route('/author_details_byname/<author_name>')
def author_details_byname(author_name):
    the_author = mongo.db.authors.find_one({"name": author_name})
    books = mongo.db.books.find({'author': the_author['name']})
    return render_template('authordetails.html', author=the_author, books = books)

@app.route('/add_author', methods=['POST', 'GET'])
def add_author():
    if request.method == 'POST':
        f_name = request.form[('f_name')]
        l_name = request.form[('l_name')]
        bio = request.form[('bio')]
        name = f_name + " " + l_name
        new_author = {'f_name': f_name.lower(), 'l_name': l_name.lower(), 'bio': bio, 'name': name}
        mongo.db.authors.insert(new_author)
        return redirect(url_for('authors'))
    else:
        return render_template('addauthor.html')
        
@app.route('/add_review/<book_id>')
def add_review(book_id):
    return render_template('addreview.html', book_id=book_id)

@app.route('/submit_review', methods=['POST'])
def submit_review():
    book_id = request.form.get("book_id")
    review = request.form.get("user_review")
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    book['user_reviews'].append(review)
    mongo.db.books.update({"_id": ObjectId(book_id)}, book)
    return redirect('/')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)