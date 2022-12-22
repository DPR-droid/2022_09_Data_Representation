# 2022_09_Data_Representation
2022_09_Data_Representation



## SQL dbconfig.py file

    mysql = {
        'host':"",
        'user':"",
        'password':"",
        'database':"urlcheck"
    }

## SQL Creation

    create database urlcheck;
    Query OK, 1 row affected (0.00 sec)

    create table urlcheck (
    id int NOT NULL AUTO_INCREMENT,
    url varchar(2048),
    entrytime datetime,
    PRIMARY KEY(id)
    );

## SQL insert

    insert into urlcheck (url,entrytime) values ('www.google.com', '2022-12-22 13:23:44');

    
