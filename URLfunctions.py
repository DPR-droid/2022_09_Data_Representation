import mysql.connector
import dbconfig as cfg
from config import config as configcfg
import requests
import datetime
import json

# The URLfunctions class is a utility class that has methods for performing various operations on the links table in a MySQL database
class URLfunctions:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    
    # getcursor: This method establishes a connection to the MySQL database and returns a cursor object that can be used to execute SQL statements.
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    # closeAll: This method closes the MySQL connection and cursor.
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

     # create: This method inserts a new row into the links table with the specified URL, Type, and Score values. It returns the id of the inserted row.
    def create(self, values):
        cursor = self.getcursor()
        sql="insert into links (URL,Type, Score) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    # getAll: This method retrieves all rows from the links table and returns them as a list of dictionaries, where each dictionary represents a
    # row with keys being the column names and values being the column values.
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from links order by id desc"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    # findByID: This method retrieves the row from the links table with the specified id and returns it as a dictionary with keys being the column names and values being the column values.
    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from links where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()

        print("Found done")

        return returnvalue

    # update: This method updates the row in the links table with the specified id and sets the URL, Type, and Score values to the specified values.
    def update(self, values):
        cursor = self.getcursor()
        sql="update links set url= %s, type=%s, score=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
        print("update done")


    # This function is responsible for checking whether a given URL with the specified id has already been checked or not. 
    # It does this by executing an SQL SELECT statement on the url_checked table to see if a record exists with the given id. 
    # If a record does not exist, it means the URL has not been checked and the function calls the find_vt function to retrieve the URL data. 
    # If a record does exist, the function returns the cid value for that record. The function also closes the cursor and connection to the database when it is finished.
    def check_sql(self, id):
        cursor = self.getcursor()
        sql="SELECT cid FROM url_checked WHERE cid = '%s'"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        
        if not result:
            added = URLfunctions.find_vt(id)
            return added
        else:
            
            self.closeAll()
            return result[0]
    
    # This function performs a VirusTotal scan on a given URL. VirusTotal is a service that analyzes files and URLs for the presence of viruses, worms, trojans, and other types of malicious content.
    # The function first retrieves the URL from the "links" table in the database using the given id. It then uses the VirusTotal API to request a report on the URL and receives the report in JSON format.
    # The function then processes the report to determine the number of "unrated" sites, which are sites that have not yet been analyzed by VirusTotal, and the number of "suspicious" sites, 
    # which are sites that have been flagged as potentially malicious. 
    # The function also creates a list of the names of the suspicious sites.
    # The function then stores the scan date, the total number of sites checked, the number of unrated sites, the number of suspicious sites, and the list of suspicious sites in the "url_checked" table in the database.
    # Finally, the function returns the list of suspicious sites. If the URL does not exist in the VirusTotal dataset or if there is an error with the code, the function returns a string indicating this. 
    def find_vt(self, id):
        cursor = self.getcursor()
        sql="select url from links where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        results = cursor.fetchone()

        print(results[0])
        domain = results[0]
 
        vtapi = configcfg["virustotal"]
        url = 'https://www.virustotal.com/vtapi/v2/url/report'
        params = {'apikey': vtapi , 'resource':domain, 'allinfo':True}
        response = requests.get(url, params=params)
        result = response.json()
        count = 0
        susurl = []

        try: 

            
            if result['response_code'] == 0:
                print('Resource does not exist in the dataset')
                x = datetime.datetime.now()
                str_now = x.strftime('%Y-%m-%d %H:%M:%S')

                vtScan = str_now
                TSC = 0
                USC = 0
                SSCount = 0
                finallist = "response_code"

                values = (id, vtScan ,TSC, USC, SSCount, finallist, str_now)

                sql="INSERT INTO url_checked (cid, VT_First_scan_date, Total_sites_checked, Unrated_site_count, suspicious_site, site_list, Date_checked) values (%s,%s,%s,%s,%s,%s,%s)"
                
                cursor.execute(sql, values)
                
                self.connection.commit()
                self.closeAll()
                return str("response_code")



            elif result['positives'] != 0:
                for key, value in result['scans'].items():
                    if value['result'] == "unrated site":
                        count = count + 1
                    elif value['result'] != "clean site":
                        susurl.append(str(key)) 
            else:
                print('Maybe an error with the code')
                x = datetime.datetime.now()
                str_now = x.strftime('%Y-%m-%d %H:%M:%S')

                vtScan = str_now
                TSC = 0
                USC = 0
                SSCount = 0
                finallist = "Error 1"

                values = (id, vtScan ,TSC, USC, SSCount, finallist, str_now)

                sql="INSERT INTO url_checked (cid, VT_First_scan_date, Total_sites_checked, Unrated_site_count, suspicious_site, site_list, Date_checked) values (%s,%s,%s,%s,%s,%s,%s)"
                
                cursor.execute(sql, values)
                
                self.connection.commit()
                self.closeAll()
                return str("Clear with error")
            

            vtScan = result['scan_date']
            TSC = result['total']
            USC = count
            SSCount = len(susurl)
            finallist = str(susurl)


            x = datetime.datetime.now()
            str_now = x.strftime('%Y-%m-%d %H:%M:%S')

            # print(len(susurl))
            # print(finallist)

            values = (id, vtScan ,TSC, USC, SSCount, finallist, str_now)

            sql="INSERT INTO url_checked (cid, VT_First_scan_date, Total_sites_checked, Unrated_site_count, suspicious_site, site_list, Date_checked) values (%s,%s,%s,%s,%s,%s,%s)"
            
            # print(sql, values)
            
            cursor.execute(sql, values)
            
            self.connection.commit()
            self.closeAll()

            return finallist
        
        except Exception as e:
            print(e)

    # The login function for a user. It takes in two arguments: email and pwd, which represent the email and password of the user attempting to login.
    # The function first creates a cursor using the getcursor method and then defines an SQL query that selects the email and password from the user 
    # table where the email is equal to the provided email argument. The function then executes this query with the provided email as the argument, and retrieves the resulting row.
    # If the resulting row is empty (i.e., no user with the provided email was found in the table), the function returns False, indicating that the login was unsuccessful. 
    # Otherwise, the function compares the password in the retrieved row with the provided password argument. If they match, the function returns True, indicating a successful login. 
    # If the passwords do not match, the function returns False indicating an unsuccessful login.
    def login(self, email, pwd):
        cursor = self.getcursor()
        sql="SELECT email, pwd FROM user WHERE email=%s"

        values = (email,)

        try:
            cursor.execute(sql, values)

            results = cursor.fetchone()

            if not results:
                print("Incorrect Username and Password")
                return False
            
            if results[1] == pwd:
                print("This matches")
                return True
                
            self.connection.commit()
            self.closeAll()
        
        except Exception as e:
            print(e)

    
    # getAll_V02: This method retrieves all rows from the links table and returns them as a list of dictionaries, where each dictionary represents a
    # row with keys being the column names and values being the column values.
    def getAll_V02(self):
        cursor = self.getcursor()
        sql="SELECT links.id, links.url, links.type, links.score, suspicious_site, site_list FROM links JOIN url_checked ON links.id = url_checked.cid order by links.id DESC"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    # This function is intended to be used to delete a record from the links table in the database.
    # a single parameter id, which is an integer representing the ID of the record to be deleted in the links table in the database. 
    # The function uses an SQL DELETE statement to delete the record with the specified id from the links table. 
    # The function then commits the delete operation to the database and closes the cursor and connection to the database
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from links where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")
    
    # The convertToDictionary function converts a database query result represented as a tuple to a dictionary object. The colnames variable is a list of column names for the database table. 
    # The item variable is an empty dictionary that will be used to store the key-value pairs for the dictionary object.
    # The function first checks if the result variable is not None. If it's not None, the function iterates over the colnames list, 
    # using the enumerate function to get the index and value for each element in the list. 
    # The value variable stores the element of the result tuple that corresponds to the current index. The item dictionary is then updated with a key-value pair, 
    # where the key is the column name and the value is the value from the tuple. Finally, the item dictionary is returned.
    def convertToDictionary(self, result):
        colnames=['id','URL','Type', "Score"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

    # The convertToDictionary_V02 function converts a database query result represented as a tuple to a dictionary object. The colnames variable is a list of column names for the database table. 
    # The item variable is an empty dictionary that will be used to store the key-value pairs for the dictionary object.
    # The function first checks if the result variable is not None. If it's not None, the function iterates over the colnames list, 
    # using the enumerate function to get the index and value for each element in the list. 
    # The value variable stores the element of the result tuple that corresponds to the current index. The item dictionary is then updated with a key-value pair, 
    # where the key is the column name and the value is the value from the tuple. Finally, the item dictionary is returned.
    def convertToDictionary_V02(self, result):
        colnames=['id','URL','Type', "Score", "Suspicious", "List"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
URLfunctions = URLfunctions()