import mysql.connector
import dbconfig as cfg
import vt # imported the virustotal.
from config import config as configcfg
import requests
import json
import datetime


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


    def check(self, id):
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
        # print(result)
        if result['response_code'] == 0:
            print('Resource does not exist in the dataset')
            exit()
        elif result['positives'] != 0:
            for key, value in result['scans'].items():
                if value['result'] == "unrated site":
                    count = count + 1
                elif value['result'] != "clean site":
                    susurl.append(str(key)) 
        else:
            print('Maybe an error with the code')
        
        print("\n\n################## VirusTotal Stats ##################")
        print("First scan date: " + result['scan_date'])
        print("Total sites checked: " + str(result['total']))
        print("Unrated site count: " + str(count))
        print("\n##################VirusTotal Verdict##################")
        print("Malicious/suspicious site count: " + str(result['positives']))

        vtScan = result['scan_date']
        TSC = result['total']
        USC = count
        SSCount = len(susurl)
        finallist = str(susurl)


        x = datetime.datetime.now()
        str_now = x.strftime('%Y-%m-%d %H:%M:%S')

        print(len(susurl))
        print(finallist)

        values = (id, vtScan ,TSC, USC, SSCount, finallist, str_now)

        sql="INSERT INTO url_checked (cid, VT_First_scan_date, Total_sites_checked, Unrated_site_count, suspicious_site, site_list, Date_checked) values (%s,%s,%s,%s,%s,%s,%s)"
        
        print(sql, values)
        
        cursor.execute(sql, values)
        
        self.connection.commit()
        # #newid = cursor.lastrowid
        self.closeAll()

        return results


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