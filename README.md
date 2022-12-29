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



