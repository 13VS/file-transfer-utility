import os
import  pandas as pd
import numpy as np
import datetime
import time
from project1 import copy
from mail import send_mail
import csv
now = datetime.datetime.now()
s=now.strftime("%A")
for files in os.walk('./REPORTS\\CDW\\EMEA'):
    list=files
l=list[2]
print(l)
l1=[]
df=pd.read_csv("details.csv")
x=np.array(df)
data=[]
myData = [["partnerid", "region", "report name","creation_ts","sent_ts","status"]]
for i in range(df.shape[0]):
    if x[i][2]== s and x[i][1]=="emea":
        l1.append(x[i][0])
        data = [x[i][0], x[i][1],"na", "na", "na","report not generated"]
        myData.append(data)

i=1
for l1i in l1:
    a=""
    m=0
    m1=0
    temp=0
    for li in l:
        if li.find(l1i)!=-1 and li[-5:]==".xlsx":
            copy(li)
            temp=os.path.getctime(os.path.join(os.path.dirname(__file__),"REPORTS/CDW/EMEA/"+li))
            if\
                            m<temp :
                m=temp
                m1=datetime.datetime.now()
                a=li

    if m!=0:
        myData[i][2] = a
        myData[i][3]=datetime.datetime.fromtimestamp(m)
        myData[i][4]=m1
        myData[i][5]="report generated"
    i=i+1
ts = time.time()
st = "CDW_REPORT_AUDITSTAUS_"+datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d')+".csv"
print(myData)
myFile = open(st, 'w',newline="")
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
#send_mail("viswanathsrikanthbathina@gmail.com", ["vaishnavibathina@gmail.com"], "AUTOMATIC REPORT MAIL", "Hi, This mail is generated to give today's report", files=[st],server="smtp.gmail.com",password="",port=587)
