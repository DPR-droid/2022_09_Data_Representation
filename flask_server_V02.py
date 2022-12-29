# Data Representation
# Lecturer: Andrew Beatty
# Author: David Ryan
# Student ID: G00398318

from flask import Flask, jsonify, request, abort, render_template, session, redirect, url_for
from URLfunctions import URLfunctions

app = Flask(__name__, static_url_path='', static_folder='templates')


app.secret_key = "IlikeWednesdaybutnotfridays24152"

# Login
# https://roytuts.com/jquery-ajax-based-login-logout-using-python-flask-mysql/
# https://github.com/PrettyPrinted/youtube_video_code/blob/master/2020/02/10/Creating%20a%20Login%20Page%20in%20Flask%20Using%20Sessions/flask_session_example/app.py
# curl -X POST http://127.0.0.1:5000/  -H "Content-Type: application/x-www-form-urlencoded" -d "username=dave@123.com&password=chicken" 
# When a user submits a request to this route with the POST method, the code will check the provided username and password against the login function in the URLfunctions module. 
# If the login function returns True, the user's session will be set and they will be redirected to the 'index' page. 
# If the login function returns False, the user will be redirected back to the login page with an error message. 
# If the request method is not POST, the login page template will be rendered and displayed to the user.
@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        session.pop('username', None)
        

        username = request.form['username']
        password = request.form['password']

        user = URLfunctions.login(username, password)

        #print(user)

        if user == True:
            session['username'] = user
            resp =  jsonify({'message' : 'User logged in successfully'})
            resp.status_code = 200
            print(resp)
            return redirect(url_for('index'))

        else:
            resp = jsonify({'message' : 'Bad Request - invalid credendtials'})
            resp.status_code = 400
            print(resp)
            return redirect(url_for('login'))
                
    return render_template('login.html')

# Logout
# When a request is made to this endpoint, the code checks if there is a 'username' key in the session dictionary. 
# If there is, it removes the key and its associated value from the session dictionary. 
# Finally, the code redirects the user to the login page. 
# This effectively logs the user out of the application by removing their session information.
@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username', None)
	return redirect(url_for('login'))

# Main page
# https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
@app.route('/index')
def index():
    return render_template('index_V02.html')

# Get all
# curl "http://127.0.0.1:5000/urls"
@app.route('/urls')
def getAll():
    #print("in getall")
    results = URLfunctions.getAll()
    return jsonify(results)

# Get all
# curl "http://127.0.0.1:5000/urls"
@app.route('/urls_v02')
def getAll_V02():
    #print("in getall")
    results = URLfunctions.getAll_V02()
    return jsonify(results)

# Find by ID
# curl "http://127.0.0.1:5000/urls/22"
@app.route('/urls/<int:id>')
def findById(id):
    foundURL = URLfunctions.findByID(id)

    return jsonify(foundURL)

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
    foundURL = URLfunctions.findByID(id)
    if not foundURL:
        abort(404)    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Score' in reqJson and type(reqJson['Score']) is not int:
        abort(400)

    if 'URL' in reqJson:
        foundURL['URL'] = reqJson['URL']
    if 'Type' in reqJson:
        foundURL['Type'] = reqJson['Type']
    if 'Score' in reqJson:
        foundURL['Score'] = reqJson['Score']
    values = (foundURL['URL'],foundURL['Type'],foundURL['Score'],foundURL['id'])

    print("#######values#######")
    print(values)
    print("######################")

    URLfunctions.update(values)
    return jsonify(foundURL)
    # return jsonify({"done":True})

# Check
# curl -X GET "http://127.0.0.1:5000/check/18"
# HTTP GET requests sent to the '/check/int:id' URL. When a request is made to this URL, the 'check' function is executed and the 'id' parameter is passed to it. 
# The function then calls the 'check_sql' method of the 'URLfunctions' object, passing in the 'id' parameter. 
# The 'check_sql' method returns a dictionary containing the data for the URL with the specified 'id', 
# which is then converted to a JSON object using the 'jsonify' function and returned in the response to the client.
@app.route('/check/<int:id>' , methods=['GET'])
def check(id):
    foundURL = URLfunctions.check_sql(id)
    print("#######foundURL#######")
    print(foundURL)
    print("######################")
    return jsonify(foundURL)

    
# Delete
# curl -X DELETE "http://127.0.0.1:5000/urls/18"
@app.route('/urls/<int:id>' , methods=['DELETE'])
def delete(id):
    URLfunctions.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)