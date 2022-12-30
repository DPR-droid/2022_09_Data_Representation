# 2022_09_Data_Representation
2022_09_Data_Representation

## Introduction
The purpose of this repository is to demonstrate the learning outcomes of the Data Representation module.

**README Table of Contents**

1. GitHub Repository
2. Assessment
3. Overview of Project Functionality
    - 3.1 Login Page **login.html**
    - 3.2 URL DB Page **index.html**
        - 3.2.1 Read
        - 3.2.2 Create
        - 3.2.3 Update
        - 3.2.4 Delete
    - 3.3 Virustotal API **index_V02.html**
    - 3.4 60 second video of the Big Project 
    - 3.5 Biggest challenge

4. How Run the Assessment
    - 4.1 Try at home
    - 4.2 Pythonanywhere - **The site will be automatically disabled on Monday 27 March 2023**
5. Acknowledgement
6. References

# 1. GitHub Folder structure

1.1 Project
    - Contains Big Project Description

1.2. Project Version 
    - Contains Zip Files of each iteration: ***.zip in gitignore**

1.3. Template
    Contain HTML files
    - index_V02.html: **Latest version**
    - index.html
    - login.html: logging in page with authorization
    - style.css: CSS used for describing the presentation of index_V02.html and login.html

1.4. venv
    - Contains python venv **venv in gitignore**
        - python -m venv venv
        - venv\Scripts\activate.bat
        - deactivate

1.5. Project_Create
    - createdb.py 
        A Python script, you can use the MySQL-connector-python library to execute the CREATE DATABASE statement and then creating the required tables on the MySQL server.

    - createsqlcfg.py
        A Python script that will request a user's input to create a dbconfig.py file with MySQL connection details.

    - createvtcfg.py
        A Python script that will request input from the user and create a config.py file with the API key from Virustotal. 

1.6. Main folder files
    Contains
    - config.py  **config.py in gitignore**
    - dbconfig.py  **dbconfig.py in gitignore**
    - flask_server_V01.py: contain flask app run "python flask_server_V01.py"
    - flask_server_V02.py: **Latest version** contain flask app run "python flask_server_V02.py"
    - URLfunctions.py: contains functions
    - requirements.txt: required for running in venv or pythonanywhere.com run "pip install -r requirments.txt"
    - gitignore: Tells Git which files to ignore when committing your project to the GitHub repository
    - DA_Big_Project.7z: Files required to run a local version. See section **4.1 Try at home**


# 2. Assessment

This project is based on **Topic09-linking to db** 

1. A flask server
2. REST API, (to perform CRUD operations) 
3. Database table **links table**
4. Web interface, using AJAX
5. Logging in page with authorization
6. Second Database to store users credentials  **user table**
7. Server Links to some third party API 
8. The third party API requires authentication
9. Third Database to store results of third party API **url_checked table**
10. Hosted online Pythonanywhere.com

# 3. Overview of Project Functionality
This display the users experience from login to CRUD to logout

## 3.1 Login Page **login.html**

**Note:** Screenshots foe section **3.1 Login Page** are from **login.html**

5. Logging in page with authorization
6. Second Database to store users credentials  **user table**

The user will arrive at the login landing page:

![Login_01.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/Login_01.PNG?raw=true)

The **flask_server_V01.py "login"** function is called which handles a login request made to a web application. The function first checks to see if the request method is "POST". If it is, it retrieves the user's username and password from the request form, and calls **URLfunctions.py** module **"login"** function with these values as arguments. 

**URLfunctions.py "login"** function receives an email and password as input, and uses them to query a database table called "user" for a matching email. If no match is found, it returns False. If a match is found, it checks if the stored password for that email matches the provided password. If they match, it returns True. If they don't match, it returns False. If an exception occurs during the execution of the SQL query or the fetching of the results, it is caught and printed.

- If the **flask_server_V01.py "login"** function returns **True**, the user's session is set with the value of the user and a message is returned indicating that the user was logged in successfully. 
    - The user is brought to the index page
- If the  **flask_server_V01.py "login"** function returns **False**, a message is returned indicating that the login request was invalid.
    - The user is returned to login landing page.

## 3.2 URL DB Page **index_V02.html**

2. REST API, (to perform CRUD operations) 
3. Database table **links table**
4. Web interface, using AJAX

After successfully login the user will arrive at URL DB page performing CRUD operations

CRUD stands for Create, Read, Update, and Delete. These are the four basic functions of persistent storage, and are commonly used to describe the basic database operations.

- **Create**: Inserting a new record or object into the database.
- **Read**: Retrieving a record or object from the database.
- **Update**: Modifying an existing record or object in the database.
- **Delete**: Removing a record or object from the database.

### 3.2.1 Read

The user will be first introduced to **Read**: This retrieves all the records stored in the urls database and displays them.

![CRUD_01.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_01.PNG?raw=true)

### 3.2.2 Create
The user can select the **Create** button

![CRUD_04.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_04.PNG?raw=true)

- Note: **Create a URL Link** is hidden on the index.html page until the **Create** button is clicked.

The user enters the details URL, Type, Score

![CRUD_06.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_06.PNG?raw=true)

Then clicks the **Create** button

The page is updated to reflect the changes made to the urls database with the newly creates entry displayed Example: **id : 60, URL : daiscool.com** 

![CRUD_05.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_05.PNG?raw=true)

### 3.2.3 Update
The user can select the **Update** button: This retrieves the record stored at **id** in the urls database and display it on a form **update URL Link**.

Then user selects the **Update** button for the entry example **id : 57, URL : dogslife.com.com, Type : excel, Score 10** 

#### HTML View

![CRUD_02.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_02.PNG?raw=true)

#### SQL View

![CRUD_09.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_09.PNG?raw=true)

- Note: **update URL Link** is hidden on the index.html page until the **Update** button is clicked.

#### HTML View

![CRUD_03.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_03.PNG?raw=true)

Then clicks the **Update** button

The page is updated to reflect the changes made to the urls database with the newly updated entry displayed Example: **id : 57, URL : dogslife.com.com, Type : PDF, Score 50** 

![CRUD_05.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_05.PNG?raw=true)

#### SQL View

![CRUD_10.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_10.PNG?raw=true)

### 3.2.4 Delete

The user can select the **Delete** button: This retrieves the record stored at **id** in the urls database and deletes the entry.

Example: **id : 60, URL : daiscool.com**

#### HTML View

![CRUD_05.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_05.PNG?raw=true)

#### SQL View

![CRUD_07.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_07.PNG?raw=true)

The page is updated to reflect the changes made to the urls database with the deleted entry no longer displayed 

#### HTML View

![CRUD_08.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_08.PNG?raw=true)

#### SQL View

![CRUD_09.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_09.PNG?raw=true)


## 3.3 Virustotal API index_V02.html
The project requested the following:
7. Server Links to some third party API 
8. The third party API requires authentication
9. Third Database to store results of third party API **url_checked table**

To add extra functionality to the project the project uses an Virustotal authenticate API KEY. 

![VT_LOOKUP_03.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/VT_LOOKUP_03.PNG?raw=true)

When the user onclick of the **Check** button

![VT_LOOKUP_04.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/VT_LOOKUP_04.PNG?raw=true)

This function performs a VirusTotal scan on a given URL. VirusTotal is a service that analyses files and URLs for the presence of viruses, worms, trojans, and other types of malicious content.

The function first retrieves the URL from the "links" table in the database using the given id. It then uses the VirusTotal API to request a report on the URL and receives the report in JSON format.

The function then processes the report to determine the number of "unrated" sites, which are sites that have not yet been analysed by VirusTotal, and the number of "suspicious" sites, which are sites that have been flagged as potentially malicious. 

The function also creates a list of the names of the suspicious sites.

The function then stores the scan date, the total number of sites checked, the number of unrated sites, the number of suspicious sites, and the list of suspicious sites in the "url_checked" table in the database.

Finally, the function returns the list of suspicious sites. If the URL does not exist in the VirusTotal dataset or if there is an error with the code, the function returns a string indicating this. 

![VT_LOOKUP_05.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/VT_LOOKUP_05.PNG?raw=true)


## 3.4 60 second video of the Big Project 

https://user-images.githubusercontent.com/77699514/210022600-ccbd791b-f8b1-4b68-9caa-e079fd63cda0.mp4

## 3.5 Biggest challenge

1. Debugging issues with the data being sent in the ajax request or received in the Flask app. It can be helpful to use tools such as the browser's developer console or a tool like Postman to inspect the request and response data or curl commands. 
2. That all the necessary dependencies are installed
3. Ensuring that the code is correctly implemented
4. Testing and deploying the application on Pythonanywhere **Pythonanywhere Errors below**

# 4. How Run the Assessment

## 4.1 Try at home

1. Download DA_Big_Project.7z and unzip to a folder and run the following python commands.
    - python -m venv venv
    - venv\Scripts\activate.bat

    - To exit type
        - deactivate

2. [Install wampserver](https://www.wampserver.com/en/) or [mysql server](https://www.mysql.com/downloads/)

3. Generate the required mySQL tables using createdb.py. If you intend to run this project locally or on another hosted platform, the Flask server will not work without these Database and tables. Alternatively use the commands below:

- SQL Database

    CREATE DATABASE datareprentation;

- SQL tables

To create a table in MySQL with an id column that is an auto-incrementing primary key and three additional columns, url, type, and score, you can use the following SQL statement:

- **links table**

    CREATE TABLE links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(2048),
    type VARCHAR(250),
    score INT
    );

- **url_checked table**

    CREATE TABLE url_checked (
        id INT AUTO_INCREMENT PRIMARY KEY,
        cid INT,
        VT_First_scan_date DATETIME,
        Total_sites_checked INT,
        Unrated_site_count INT,
        suspicious_site INT,
        site_list VARCHAR(2048),
        Date_checked DATETIME
    );

- **user table**

    CREATE TABLE `user` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NULL,
    `email` varchar(50) NULL,
    `pwd` varchar(255) NULL,
    `admin` tinyint DEFAULT 0,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

- To test the tables are functioning as required the following insert test can be applied:

- **links table INSERT Test**

    INSERT INTO links (url, type, score) VALUES 
    ('example.com', 'pdf', 10),
    ('example.org', 'word', 20),
    ('example.net', 'excel', 30);

- **url_checked table INSERT Test**

    INSERT INTO url_checked (cid, VT_First_scan_date, Total_sites_checked, Unrated_site_count, suspicious_site, site_list, Date_checked) VALUES (1, '2022-12-22 11:25:07', 91, 14, 4, "['Fortinet', 'alphaMountain.ai', 'Seclookup', 'Heimdal Security']", '2022-12-28 01:29:04');

- **user table INSERT Test**

    INSERT INTO`user`(`id`,`name`,`email`,`pwd`,`admin`) VALUES 
    (1,'123','123@123.com','password',1);

4. Create dbconfig.py and config.py using the scripts createsqlcfg.py and createvtcfg.py. If you intend to run this project locally or on another hosted platform, the Flask server will not work without these file. Place the file in your root directory after creation.

**dbconfig.py**
    mysql = {
        'host':"",
        'user':"",
        'password':"",
        'database':""
    }

**config.py**
    config = {
    "virustotal":""
    }

5. Virustotal API Key
You do not need to ask for a public API key, in order to get one you just have to [register](https://www.virustotal.com/gui/join-us) in VirusTotal Community (top right hand side of VirusTotal). Once registered, sign in into your account and you will find your public API in the corresponding menu item under your user name.

[click here](https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key)

**NOTE**: There is a Request rate 4 lookups / min for standard free public API

![VT_LOOKUP_01.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/VT_LOOKUP_01.PNG?raw=true)

**NOTE**: This will cause an error if to many requests when using the check button on multiple sites

![VT_LOOKUP_02.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/VT_LOOKUP_02.PNG?raw=true)


6. CURL Test commands

**Get all**
- curl "http://127.0.0.1:5000/urls"

**Create new entry**
- curl -i -H "Content-Type:application/json" -X POST -d "{\"URL\":\"www.askjeves.com\",\"Type\":\"someone\",\"Score\":50}" http://127.0.0.1:5000/urls

**Find by ID** This requires data in the MySQL url table
- curl "http://127.0.0.1:5000/urls/1"

**Update**
- curl -i -H "Content-Type:application/json" -X PUT -d "{\"URL\":\"www.askjeves.com\",\"Type\":\"PDF\",\"Score\":10}" http://127.0.0.1:5000/urls/1

**Check**
- curl -X GET "http://127.0.0.1:5000/check/1"

**Delete**
- curl -X DELETE "http://127.0.0.1:5000/urls/1"

# 4.2 Pythonanywhere
Version 8 currently available on pythonanywhere.com

http://daveg00398318.pythonanywhere.com/

**Note** This site will be automatically disabled on Monday 27 March 2023

Update files:

templates/index_V02.html
- update requirments.txt
- uncomment/comment pythonanywhere code to not reference localhost 127.0.0.1
- Do not upload "dbconfig.py" **pythonanywhere DB config file setup**

## Pythonanywhere Error 1 
Fix wsgi.py file using Pythonanywhere error.log

![PYTHONANYWHERE_06.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/PYTHONANYWHERE_06.PNG?raw=true)

![PYTHONANYWHERE_05.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/PYTHONANYWHERE_05.PNG?raw=true)

![PYTHONANYWHERE_01.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/PYTHONANYWHERE_01.PNG?raw=true)

## Pythonanywhere Error 2
Fix Ajax reference comment out //"url": "http://127.0.0.1:5000/check/"+encodeURI(id), 

![PYTHONANYWHERE_02.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/PYTHONANYWHERE_02.PNG?raw=true)

## Pythonanywhere Error 3
Update flask_server_V02.py **getAll_V02**
Update URLfunctions.py **getAll_V02**
Update URLfunctions.py **convertToDictionary_V02**

![PYTHONANYWHERE_03.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/PYTHONANYWHERE_03.PNG?raw=true)

![PYTHONANYWHERE_04.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/PYTHONANYWHERE_04.PNG?raw=true)

## Pythonanywhere Error 4
Logout to Login 
Page redirects to 127.0.0.1 after logging out.

![PYTHONANYWHERE_07.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/PYTHONANYWHERE_07.PNG?raw=true)

![PYTHONANYWHERE_08.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/PYTHONANYWHERE_08.PNG?raw=true)


# 5. Acknowledgement
Lecturer Andrew Beatty Data Representation

Family and friends for their support

# 6. References

[1] Beatty, A. (n.d.). datarepresentation: Data Representation course material.

[2] (N.d.). Virustotal.com. Retrieved December 30, 2022, from https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key

[3] Application not picking up .css file (flask/python). (n.d.). Stack Overflow. Retrieved December 30, 2022, from https://stackoverflow.com/questions/22259847/application-not-picking-up-css-file-flask-python

[4] (dcode), D. (2020, July 20). Creating beautiful HTML tables with CSS. DEV Community 👩‍💻👨‍💻. https://dev.to/dcodeyt/creating-beautiful-html-tables-with-css-428l

[5] Flask raises TemplateNotFound error even though template file exists. (n.d.). Stack Overflow. Retrieved December 30, 2022, from https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists

[6] Printed, P. (n.d.-a). app.py at master · PrettyPrinted/youtube_video_code.

[7] Soumitra. (2019, November 18). jQuery AJAX based Login Logout using Python Flask MySQL. Roy Tutorials. https://roytuts.com/jquery-ajax-based-login-logout-using-python-flask-mysql/
