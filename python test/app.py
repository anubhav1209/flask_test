from flask import Flask,jsonify


app = Flask(__name__)
            
books = [
    {"id": 1,"title": "1st book","author": "anubhav"},
    {"id": 2, "title": "2nd book" , "author":"aftab"},
    {"id": 3, "title": "3rd book", "author": "ashish"}
]

@app.route('/', methods=['GET'])
def homePage():
    return 'HOME PAGE'

@app.route('/books',methods=['GET'])
def getAllBooks():
    return jsonify(books)

if(__name__ == '__main__'):
    app.run(debug=True)