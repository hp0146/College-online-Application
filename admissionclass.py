# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:29:29 2023

@author: SWAMINATHAN
"""

class Adminfo:
    def setadm(self,etid,n,g,d,mn,eml,add,ca,cabl):
        self.eid=etid
        self.name=n
        self.gender=g
        self.dob=d
        self.num=mn
        self.email=eml
        self.address=add
        self.caf=ca
        self.cal=cabl
    
    def __str__(self):
       return f"""Enrollment Num:'{self.eid}'\nName:'{self.name}'\nGender:'{self.gender}'\nDOB:'{self.dob}'
        \nMobile Number:'{self.num}'\nEmail:'{self.email}'\nAddress:'{self.address}'
        \nCourse Applied For:'{self.caf}'\nSelected Courses:'{self.cal}'"""