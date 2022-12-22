from flask import Flask, jsonify, request, abort

from functions_V01 import sqlconnectors
import datetime

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/main')
def getAll():
    print("in getall")
    return "get all"


@app.route('/main/<int:id>')
def findById(id):
    print("findById")
    return "findById"


@app.route('/main', methods=['POST'])
def create():
    x = datetime.datetime.now()
    str_now = x.strftime('%Y-%m-%d %H:%M:%S')
    if not request.json:
        abort(400)
    # other checking 
    uri = {
        "url": request.json['url'], 
        "entrytime": str_now,
    }
    values =(uri['url'],uri['entrytime'])
    newId = sqlconnectors.create(values)
    uri['id'] = newId
    return jsonify(uri)


@app.route('/main/<int:id>', methods=['PUT'])
def update(id):
    print("update")
    return "update"


@app.route('/main/<int:id>' , methods=['DELETE'])
def delete(id):
    print("update")
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)