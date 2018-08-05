import os
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# from flask_images import resized_img_src

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'book_reviews'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)

# images = resized_img_src(app)

@app.route('/')
def home_page():
    return render_template('index.html')
    
@app.route('/book_list')
def book_list():
    books = mongo.db.books.find()
    return render_template('booklist.1.html',  books = books)

@app.route('/authors')
def authors():
    return render_template('authors.html', authors = mongo.db.authors.find())
    # return render_template('authors.html', authors = mongo.db.authors.find().sort({"l_name":1}))

    
@app.route('/book_details/<books_id>')
def book_details(books_id):
    the_book = mongo.db.books.find_one({"_id": ObjectId(books_id)})
    the_author = mongo.db.authors.find_one({"name": the_book['author']})
    return render_template('bookdetails.html',  book = the_book, author = the_author)

@app.route('/add_book', methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        new_book = mongo.db.books.insert_one(request.form.to_dict())
        return redirect(url_for('book_details', books_id=new_book.inserted_id))
    else:
        return render_template('addbook.html')
        
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
        mongo.db.authors.insert_one(request.form.to_dict())
        return redirect(url_for('authors'))
    else:
        return render_template('addauthor.html')
        

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)