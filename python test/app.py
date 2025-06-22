from flask import Flask,jsonify,request

# This is a simple Flask application that provides a RESTful API for managing books.
app = Flask(__name__)
            
books = [
    {"id": 1,"title": "1st book","author": "anubhav"},
    {"id": 2, "title": "2nd book" ,"author":"aftab"},
    {"id": 3, "title": "3rd book","author": "ashish"}
]

@app.route('/', methods=['GET'])
def homePage():
    return 'HOME PAGE'

@app.route('/books',methods=['GET'])
def getAllBooks():
    return jsonify(books)

# fetch a book by id
@app.route('/books/<int:book_id>',methods=['GET'])
def getBook(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({'error': 'book not found'})


# add a new book
@app.route('/books', methods=['POST'])
def addBook():
    new_Book= {
        'id': request.json['id'],
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_Book)
    return jsonify("message : Book added successfully")

# route to update existing book

@app.route('/books/<int:book_id>', methods=['PUT'])
def updateBook():
    book_id = request.json['id']
    for book in books:
        if book['id'] == book_id:
            book['title'] = request.josn['title']
            book['author'] = request.json['author']
            return jsonify("message : Book updated successfully")
    return jsonify({'error': 'book not found'})

# route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def deleteBook():
    book_id = request.json['id']
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return jsonify("message : Book Deleted successfully")
    return jsonify({'error': 'book not found'})


if(__name__ == '__main__'):
    app.run(debug=True)
