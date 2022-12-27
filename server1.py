from flask import Flask, jsonify, request, abort, render_template
from bookDAO import bookDAO

app = Flask(__name__, static_url_path='', static_folder='templates')

#app = Flask(__name__)

# https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
@app.route('/')
def index():
    return render_template('bookviewer.html')

#curl "http://127.0.0.1:5000/books"
@app.route('/books')
def getAll():
    #print("in getall")
    results = bookDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/books/<int:id>')
def findById(id):
    foundBook = bookDAO.findByID(id)

    return jsonify(foundBook)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    book = {
        "title": request.json['title'],
        "author": request.json['author'],
        "price": request.json['price'],
    }
    values =(book['title'],book['author'],book['price'])
    newId = bookDAO.create(values)
    book['id'] = newId
    return jsonify(book)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBook = bookDAO.findByID(id)
    if not foundBook:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'price' in reqJson and type(reqJson['price']) is not int:
        abort(400)

    if 'title' in reqJson:
        foundBook['title'] = reqJson['title']
    if 'Author' in reqJson:
        foundBook['author'] = reqJson['author']
    if 'price' in reqJson:
        foundBook['price'] = reqJson['price']
    values = (foundBook['title'],foundBook['author'],foundBook['price'],foundBook['id'])
    bookDAO.update(values)
    return jsonify(foundBook)
        

    

@app.route('/books/<int:id>' , methods=['DELETE'])
def delete(id):
    bookDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)