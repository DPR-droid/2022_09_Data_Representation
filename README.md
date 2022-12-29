# 2022_09_Data_Representation
2022_09_Data_Representation


## Introduction
The purpose of this repository is to demonstrate the learning outcomes of the Data Representation module. 

## Assessment

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

## Overview of Project Functionality

### Login Page
The user will arrive at the login landing page:

![Login_01.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/Login_01.PNG?raw=true)

The **flask_server_V01.py "login"** function is called which handles a login request made to a web application. The function first checks to see if the request method is "POST". If it is, it retrieves the user's username and password from the request form, and calls **URLfunctions.py** module **"login"** function with these values as arguments. 

**URLfunctions.py "login"** function receives an email and password as input, and uses them to query a database table called "user" for a matching email. If no match is found, it returns False. If a match is found, it checks if the stored password for that email matches the provided password. If they match, it returns True. If they don't match, it returns False. If an exception occurs during the execution of the SQL query or the fetching of the results, it is caught and printed.

- If the **flask_server_V01.py "login"** function returns **True**, the user's session is set with the value of the user and a message is returned indicating that the user was logged in successfully. 
    - The user is brought to the index page
- If the  **flask_server_V01.py "login"** function returns **False**, a message is returned indicating that the login request was invalid.
    - The user is returned to login landing page.

### URL DB Page
After successfully login the user will arrive at URL DB page performing CRUD operations

CRUD stands for Create, Read, Update, and Delete. These are the four basic functions of persistent storage, and are commonly used to describe the basic database operations.

- **Create**: Inserting a new record or object into the database.
- **Read**: Retrieving a record or object from the database.
- **Update**: Modifying an existing record or object in the database.
- **Delete**: Removing a record or object from the database.

## Read

The user will be first introduced to **Read**: This retrieves all the records stored in the urls database and displays them.

![CRUD_01.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_01.PNG?raw=true)

## Create
The user can select the **Create** button

![CRUD_04.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_04.PNG?raw=true)

- Note: **Create a URL Link** is hidden on the index.html page until the **Create** button is clicked.

The user enters the details URL, Type, Score

![CRUD_06.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_06.PNG?raw=true)

Then clicks the **Create** button

The page is updated to reflect the changes made to the urls database with the newly creates entry displayed Example: **id : 60, URL : daiscool.com** 

![CRUD_05.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_05.PNG?raw=true)

## Update
The user can select the **Update** button: This retrieves the record stored at **id** in the urls database and display it on a form **update URL Link**.

Then user selects the **Update** button for the entry example **id : 57, URL : dogslife.com.com, Type : excel, Score 10** 

### HTML View

![CRUD_02.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_02.PNG?raw=true)

### SQL View

![CRUD_09.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_09.PNG?raw=true)

- Note: **update URL Link** is hidden on the index.html page until the **Update** button is clicked.

### HTML View

![CRUD_03.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_03.PNG?raw=true)

Then clicks the **Update** button

The page is updated to reflect the changes made to the urls database with the newly updated entry displayed Example: **id : 57, URL : dogslife.com.com, Type : PDF, Score 50** 

![CRUD_05.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_05.PNG?raw=true)

### SQL View

![CRUD_10.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_10.PNG?raw=true)

## Delete

The user can select the **Delete** button: This retrieves the record stored at **id** in the urls database and deletes the entry.

Example: **id : 60, URL : daiscool.com**

### HTML View

![CRUD_05.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_05.PNG?raw=true)

### SQL View

![CRUD_07.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_07.PNG?raw=true)

The page is updated to reflect the changes made to the urls database with the deleted entry no longer displayed 

### HTML View

![CRUD_08.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_08.PNG?raw=true)

### SQL View

![CRUD_09.PNG](https://raw.githubusercontent.com/DPR-droid/2022_09_Data_Representation/main/data/CRUD_09.PNG?raw=true)



## Github Folder structure

1. Project
    - Contains Big Project Description

2. Project Version 
    - Contains Zip Files of each iteration: ***.zip in gitignore**

3. Template
    Contain HTML files
    - index.html: Main file CRUD
    - login.html: logging in page with authorization

4. venv
    - Contains python venv **venv in gitignore**
        - python -m venv venv
        - venv\Scripts\activate.bat
        - deactivate

5. Project_Create
    - createdb.py 
        A Python script, you can use the mysql-connector-python library to execute the CREATE DATABASE statement and then creating the required tables on the MySQL server.

    - createsqlcfg.py
        A Python script that will request a user's input to create a dbconfig.py file with MySQL connection details.

    - createvtcfg.py
        A Python script that will request input from the user and create a config.py file with the API key from Virustotal. 

6. Main folder files
    Contains
    - config.py  **config.py in gitignore**
    - dbconfig.py  **dbconfig.py in gitignore**
    - flask_server_V01.py: contain flask app run "python flask_server_V01.py"
    - URLfunctions.py: contains functions
    - requirements.txt: required for running in venv or pythonanywhere.com run "pip install -r requirments.txt"


## Config Files structure
Below is the structure of the config files, use createsqlcfg.py and createvtcfg.py to create these files. If you intend to run this project locally or on another hosted platform, the Flask server will not work without these file. Place the file in your root directory after creation.

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

### Virustotal API Key
You do not need to ask for a public API key, in order to get one you just have to [register](https://www.virustotal.com/gui/join-us) in VirusTotal Community (top right hand side of VirusTotal). Once registered, sign in into your account and you will find your public API in the corresponding menu item under your user name.

[click here](https://support.virustotal.com/hc/en-us/articles/115002088769-Please-give-me-an-API-key)

## SQL
Below is the structure of the Database and tables, use createdb.py to create. If you intend to run this project locally or on another hosted platform, the Flask server will not work without these Database and tables.

## SQL Database

    CREATE DATABASE datareprentation;

## SQL tables

To create a table in MySQL with an id column that is an auto-incrementing primary key and three additional columns, url, type, and score, you can use the following SQL statement:

**links table**

    CREATE TABLE links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(2048),
    type VARCHAR(250),
    score INT
    );

This will create a table called links with four columns:

- id: an integer column that is set as the primary key and has the AUTO_INCREMENT attribute, which means that the value of this column will be automatically incremented whenever a new row is inserted into the table.
- url: a string column with a maximum length of 2048 characters.
- type: a string column with a maximum length of 250 characters.
- score: an integer column.

**url_checked table**

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

This will create a table called url_checked with the following columns:

- id: an integer column that is set as the primary key and has the AUTO_INCREMENT attribute, which means that the value of this column will be automatically incremented whenever a new row is inserted into the table.
- cid: an integer column.
- VT_First_scan_date: a datetime column.
- Total_sites_checked: an integer column.
- Unrated_site_count: an integer column.
- suspicious_site: an integer column.
- site_list: a string column with a maximum length of 2048 characters.
- Date_checked: a datetime column.

**user table**

    CREATE TABLE `user` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NULL,
    `email` varchar(50) NULL,
    `pwd` varchar(255) NULL,
    `admin` tinyint DEFAULT 0,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

## Example of SQL insert

**links table**

    INSERT INTO links (url, type, score) VALUES 
    ('http://example.com', 'pdf', 10),
    ('http://example.org', 'word', 20),
    ('http://example.net', 'excel', 30);


**url_checked table**

    INSERT INTO url_checked (cid, VT_First_scan_date, Total_sites_checked, Unrated_site_count, suspicious_site, site_list, Date_checked) VALUES (36, '2022-12-22 11:25:07', 91, 14, 4, "['Fortinet', 'alphaMountain.ai', 'Seclookup', 'Heimdal Security']", '2022-12-28 01:29:04');


## CURL Tested

**Get all**
- curl "http://127.0.0.1:5000/urls"

**Find by ID**
- curl "http://127.0.0.1:5000/urls/22"

**Create new entry**
- curl -i -H "Content-Type:application/json" -X POST -d "{\"URL\":\"www.askjeves.com\",\"Type\":\"someone\",\"Score\":50}" http://127.0.0.1:5000/urls

**Update**
- curl -i -H "Content-Type:application/json" -X PUT -d "{\"URL\":\"www.askjeves.com\",\"Type\":\"PDF\",\"Score\":100}" http://127.0.0.1:5000/urls/23

**Check**
- curl -X GET "http://127.0.0.1:5000/check/18"

**Delete**
- curl -X DELETE "http://127.0.0.1:5000/urls/18"

## www.pythonanywhere.com
Version 6 currently available on pythonanywhere.com

http://daveg00398318.pythonanywhere.com/

Update files:

templates/index.html
- update requirments.txt
- uncomment/comment pythonanywhere code
- Do not upload "dbconfig.py" **pythonanywhere DB config file setup**



