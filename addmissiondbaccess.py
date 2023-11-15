
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 09:57:19 2023

@author: SWAMINATHAN
"""

from sqlite3 import *
from admissionclass import*

class AdmissionDB:
    
    def addrecord(self,e):
         conn=connect("admissiondb.db")
         sql=f"""INSERT INTO admission_info values( '{e.eid}','{e.name}','{e.gender}',
             '{e.dob}','{e.num}','{e.email}','{e.address}','{e.caf}','{e.cal}')"""
         conn.execute(sql)
         conn.commit()
         conn.close()
    
         
    def search(self,etid):
        conn=connect("admissiondb.db")
        cursor=conn.execute(f"select * from admission_info where Enrollment_Num='{etid}'")
        
        e=Adminfo()
        found=False
        
        for row in cursor:
            
            found=True
            e.eid=row[0]
            e.name=row[1]
            e.gender=row[2]
            e.dob=row[3]
            e.num=row[4]
            e.email=row[5]
            e.address=row[6]
            e.caf=row[7]
            e.cal=row[8]
            
        return found,e
    
    
    def delrecord(self,etid):
        conn=connect("admissiondb.db")
        sql=f"delete from admission_info where Enrollment_Num='{etid}'"
        conn.execute(sql) 
        conn.commit()        
        conn.close()
        return
    
    
    def updaterecord(self,e):
        conn=connect("admissiondb.db")
        sql=f"""update admission_info set Name='{e.name}',Gender='{e.gender}',DOB='{e.dob}',
        Mobile_Number='{e.num}',Email='{e.email}',Address='{e.address}',CAF='{e.caf}',CS='{e.cal}'"""
        conn.execute(sql)
        conn.commit()
        conn.close()
        return
   
    def appNum(self):
        conn=connect("admissiondb.db")
        cur=conn.cursor()
        sql=f"select Enrollment_Num from admission_info ORDER BY Enrollment_Num DESC LIMIT 1"
        cur.execute(sql)
        rs=cur.fetchone()
        num=1000
        if rs:
          num=int(rs[0])+1          
        conn.commit()
        conn.close()
        return num
