# Data Representation
# Lecturer: Andrew Beatty
# Author: David Ryan
# Student ID: G00398318

import mysql.connector

# Connect to the MySQL server
# Make sure you update your_username, your_password, localhost, your_database with the correct settings
cnx = mysql.connector.connect(user='root', password='', host='localhost')
cursor = cnx.cursor()


# Create the 'datarepresentation' database
# Change name if required
cursor.execute("CREATE DATABASE datarepresentation")

# Connect to the 'datarepresentation' database
# Change name if required
cnx.database = 'datarepresentation'

# Create the 'links' table
table1 = """
CREATE TABLE links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(2048),
    type VARCHAR(250),
    score INT
);
"""
cursor.execute(table1)

# Create the 'url_checked' table
table2 = """
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
"""
cursor.execute(table2)

# Create the 'user' table
table3 = """
CREATE TABLE `user` (
    `id` int unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(50) NULL,
    `email` varchar(50) NULL,
    `pwd` varchar(255) NULL,
    `admin` tinyint DEFAULT 0,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
"""
cursor.execute(table3)

# Close the connection to the MySQL server
cnx.close()