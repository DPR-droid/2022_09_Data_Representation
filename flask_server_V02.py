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
# This code defines a route for the '/index' URL in the application. When a user navigates to this URL, the function index() is executed. 
# The function index() returns the HTML template 'index_V02.html' which is rendered in the user's web browser.
@app.route('/index')
def index():
    return render_template('index_V02.html')

# Get all
# curl "http://127.0.0.1:5000/urls"
# The @app.route('/urls') decorator in the code defines a route for the Flask web application. 
# When a client makes a GET request to the '/urls' endpoint, the getAll() function will be executed.
# The getAll() function calls the getAll() method of the URLfunctions class and stores the returned value in the results variable. 
# The jsonify() function is then used to convert the results variable to a JSON object, which is returned to the client as the response to the request.
@app.route('/urls')
def getAll():
    #print("in getall")
    results = URLfunctions.getAll()
    return jsonify(results)

# Get all
# curl "http://127.0.0.1:5000/urls"
# Updated version to getAll to allow for 2 extra variables
@app.route('/urls_v02')
def getAll_V02():
    #print("in getall")
    results = URLfunctions.getAll_V02()
    return jsonify(results)

# Find by ID
# curl "http://127.0.0.1:5000/urls/22"
# The code is a Flask route decorator. It is used to bind a function to a URL route in the Flask web application. 
# When a user navigates to the specified URL in their web browser, the function associated with the route is executed.
# In this case, the route decorator @app.route('/urls/<int:id>') binds the findById function to the /urls/<id> URL route. 
# The <int:id> part of the route indicates that the id variable in the function will be an integer type. 
# When the user navigates to a URL that matches this route, for example /urls/123,
# the findById function will be executed and the value 123 will be passed as the id argument to the function.
@app.route('/urls/<int:id>')
def findById(id):
    foundURL = URLfunctions.findByID(id)

    return jsonify(foundURL)

# Create new entry
# curl -i -H "Content-Type:application/json" -X POST -d "{\"URL\":\"www.askjeves.com\",\"Type\":\"someone\",\"Score\":50}" http://127.0.0.1:5000/urls
# This is a Flask route that listens for HTTP POST requests sent to the '/urls' endpoint. When a POST request is received, 
# the function first checks if there is any JSON data included in the request body. If there is no JSON data, 
# it aborts the request and returns an HTTP status code of 400 (Bad Request).
# If the request includes JSON data, the function creates a dictionary called 'url' with keys 'URL', 'Type', and 'Score', 
# and sets their values to the corresponding values from the request body. Then it creates a tuple called 'values' that contains the values
# for the keys in the same order as they appear in the database table.
# Next, the function calls the 'create' method from the 'URLfunctions' class and passes it the 'values' tuple as an argument. 
# This method inserts a new row into the 'links' table in the database with the values provided in the tuple. 
# The 'create' method returns the ID of the newly inserted row, which the function assigns to the 'id' key in the 'url' dictionary. 
# Finally, the function returns the 'url' dictionary as a JSON object to the client.
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
# This is a Flask route decorated with @app.route that listens for a PUT request to the /urls/<int:id> URL path. When the route receives a PUT request, it will execute the update function.
# The update function uses the findByID function to retrieve the URL data from the links table that matches the given id passed in the URL path. 
# If the URL data is not found, the function will return a 404 error. If the request does not contain a JSON payload, the function will return a 400 error.
# The function will then check if the JSON payload includes a Score field and whether its value is an integer. If not, it will return a 400 error.
# If the URL, Type, or Score field is present in the JSON payload, the function will update the corresponding field in the foundURL dictionary with the new value. 
# It will then create a tuple called values with the updated URL data and the id of the URL.
# Finally, the function will call the update function in the URLfunctions class and pass it the values tuple as an argument. 
# It will then return the updated foundURL dictionary in a JSON response.
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
# GET requests sent to the '/check/int:id' URL. When a request is made to this URL, the 'check' function is executed and the 'id' parameter is passed to it. 
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
# Function deletes the SQL record using the URLfunctions.delete with the specified ID, 
# When a DELETE request is made to the /urls/<id> URL, where <id> is the ID of the URL record.
@app.route('/urls/<int:id>' , methods=['DELETE'])
def delete(id):
    URLfunctions.delete(id)
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)