# 2022_09_Data_Representation
2022_09_Data_Representation


## SQL dbconfig.py file

    mysql = {
        'host':"",
        'user':"",
        'password':"",
        'database':"datareprentation"
    }

## SQL Database 

    CREATE DATABASE datareprentation;

## SQL Creation table
To create a table in MySQL with an id column that is an auto-incrementing primary key and three additional columns, url, type, and score, you can use the following SQL statement:

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

## SQL insert values

    INSERT INTO links (url, type, score) VALUES 
    ('http://example.com', 'pdf', 10),
    ('http://example.org', 'word', 20),
    ('http://example.net', 'excel', 30);


## CURL Tested

**Get all**
- curl "http://127.0.0.1:5000/urls"

**Find by ID**
- curl "http://127.0.0.1:5000/urls/22"

**Create new entry**
- curl -i -H "Content-Type:application/json" -X POST -d "{\"URL\":\"www.askjeves.com\",\"Type\":\"someone\",\"Score\":50}" http://127.0.0.1:5000/urls

**Update**
- curl -i -H "Content-Type:application/json" -X PUT -d "{\"URL\":\"www.askjeves.com\",\"Type\":\"PDF\",\"Score\":100}" http://127.0.0.1:5000/urls/23

**Delete**
- curl -X DELETE "http://127.0.0.1:5000/urls/18"


## www.pythonanywhere.com

http://daveg00398318.pythonanywhere.com/


