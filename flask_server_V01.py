from flask import Flask, jsonify, request, abort, render_template, session
from URLfunctions import URLfunctions

app = Flask(__name__, static_url_path='', static_folder='templates')


app.secret_key = "secret key"

# Main page
# https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
@app.route('/')
def index():
    return render_template('index.html')

# # Login Page
# @app.route('/login/page')
# def login_page():
# 	return render_template('login.html')

# Get all
# curl "http://127.0.0.1:5000/urls"
@app.route('/urls')
def getAll():
    #print("in getall")
    results = URLfunctions.getAll()
    return jsonify(results)

# Find by ID
# curl "http://127.0.0.1:5000/urls/22"
@app.route('/urls/<int:id>')
def findById(id):
    foundBook = URLfunctions.findByID(id)

    return jsonify(foundBook)

# Creat new entry
# curl -i -H "Content-Type:application/json" -X POST -d "{\"URL\":\"www.askjeves.com\",\"Type\":\"someone\",\"Score\":50}" http://127.0.0.1:5000/urls
@app.route('/urls', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    url = {
        "URL": request.json['URL'],
        "Type": request.json['Type'],
        "Score": request.json['Score'],
    }
    values =(url['URL'],url['Type'],url['Score'])
    newId = URLfunctions.create(values)
    url['id'] = newId
    return jsonify(url)

# Update
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"URL\":\"www.askjeves.com\",\"Type\":\"PDF\",\"Score\":100}" http://127.0.0.1:5000/urls/23
@app.route('/urls/<int:id>', methods=['PUT'])
def update(id):
    foundBook = URLfunctions.findByID(id)
    if not foundBook:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Score' in reqJson and type(reqJson['Score']) is not int:
        abort(400)

    if 'URL' in reqJson:
        foundBook['URL'] = reqJson['URL']
    if 'Type' in reqJson:
        foundBook['Type'] = reqJson['Type']
    if 'price' in reqJson:
        foundBook['Score'] = reqJson['Score']
    values = (foundBook['URL'],foundBook['Type'],foundBook['Score'],foundBook['id'])
    URLfunctions.update(values)
    return jsonify(foundBook)
        

    
# Delete
# curl -X DELETE "http://127.0.0.1:5000/urls/18"
@app.route('/urls/<int:id>' , methods=['DELETE'])
def delete(id):
    URLfunctions.delete(id)
    return jsonify({"done":True})


# @app.route('/login', methods=['POST'])
# def login():
# 	_json = request.json
# 	#print(_json)
# 	_username = _json['username']
# 	_password = _json['password']
	
# 	if _username and _password:
# 		user = URLfunctions.login(_username, _password)
		
# 		if user != None:
# 			session['username'] = user
# 			return jsonify({'message' : 'User logged in successfully'})

# 	resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
# 	resp.status_code = 400
# 	return resp

# @app.route('/logout')
# def logout():
# 	if 'username' in session:
# 		session.pop('username', None)
# 	return jsonify({'message' : 'You successfully logged out'})




if __name__ == '__main__' :
    app.run(debug= True)