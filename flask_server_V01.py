from flask import Flask, jsonify, request, abort, render_template

from functions_V01 import urlCheck
import datetime

app = Flask(__name__, static_url_path='', static_folder='templates')

# https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
@app.route('/')
def index():
    return render_template('index.html')

# @app.route("/about/")
# def about():
#     return render_template('about.html')

# get All
# curl http://127.0.0.1:5000/
@app.route('/main')
def getAll():
    # print("in getall")
    # return "get all"
    results = urlCheck.getAll()
    return jsonify(results)

# Find by ID
# curl http://127.0.0.1:5000/1
@app.route('/main/<int:id>')
def findById(id):
    print("findById")
    return "findById"

# Create
# curl  -i -H "Content-Type:application/json" -X POST -d "{\"url\":\"www.google.com\", \"type\":\"word\"}" http://127.0.0.1:5000/
@app.route('/', methods=['POST'])
def create_link():
    x = datetime.datetime.now()
    str_now = x.strftime('%Y-%m-%d %H:%M:%S')
    if not request.json:
        abort(400)
    # other checking 
    uri = {
        "url": request.json['url'], 
        "type": request.json['type'], 
        "datetime": str_now,
    }
    values =(uri['url'],uri['type'],uri['datetime'])
    newId = urlCheck.create(values)
    uri['id'] = newId
    return jsonify(uri)

# Update
# curl -X PUT http://127.0.0.1:5000/1
@app.route('/<int:id>', methods=['PUT'])
def update(id):
    print("Update")
    return "Return Id number" + str(id)

# Delete
# curl -X DELETE http://127.0.0.1:5000/1
@app.route('/<int:id>' , methods=['DELETE'])
def delete(id):
    print("Delete")
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)