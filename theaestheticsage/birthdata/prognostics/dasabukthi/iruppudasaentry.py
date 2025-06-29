import mysql.connector as mc
import sys
from birthdata.prognostics.astrologic.planetary_positions.chart_workspace import sqlhelpers

def dasaentry(dcname=None):
    mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
    cursor=mycon.cursor(buffered=True)
    planetaries=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu"]
    cursor.execute("""create table if not exists dasa (name char(100) unique not null,
    iruppuplanet char(100) not null,iruppudasa varchar(100) not null,dateofbirth varchar(100) not null,
    timeofbirth varchar(100) not null);""")
    mycon.commit()
    if dcname!=None:
        dname=dcname
    else:
        dname=input("enter the name of the person:")
    if not sqlhelpers.dasachecker(dname):
        while True:
            askpl=input("enter the iruppudasa planet:")
            if askpl in planetaries:
                break
        cursor.execute(("insert into dasa(name,iruppuplanet,iruppudasa,dateofbirth,timeofbirth)""values (%s,%s,%s,%s,%s)"),[dname,askpl,input("enter the person iruppudasa:"),input("enter the date of birth:"),input("enter the time of birth:")])
        mycon.commit()
    else:
        print("data already exists")
    mycon.close()