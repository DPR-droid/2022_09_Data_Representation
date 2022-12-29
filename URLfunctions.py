import mysql.connector
import dbconfig as cfg
from config import config as configcfg
import requests
import datetime
import json


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

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def create(self, values):
        cursor = self.getcursor()
        sql="insert into links (URL,Type, Score) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        cursor = self.getcursor()
        sql="select * from links"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from links where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def update(self, values):
        cursor = self.getcursor()
        sql="update links set URL= %s,Type=%s, Score=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()


    # Check if entry already exist in table
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

    def login(self, email, pwd):
        cursor = self.getcursor()
        sql="SELECT email, pwd FROM user WHERE email=%s"

        values = (email,)

        try:
            cursor.execute(sql, values)

            results = cursor.fetchone()

            # print("SQL Password: " + str(results[1]))
            # print("Entered password: " + pwd)

            if results[1] == pwd:
                print("This matches")
                return True
                
            self.connection.commit()
            self.closeAll()
        
        except Exception as e:
            print(e)



    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from links where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','URL','Type', "Score"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
URLfunctions = URLfunctions()