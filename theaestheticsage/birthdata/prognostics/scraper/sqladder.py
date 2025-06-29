import datascraper
import datetime
import time
from birthdata.prognostics.astrologic.planetary_positions.chart_workspace import positionentry
from birthdata.prognostics.astrologic.karagam.grahabalam import shadbalamentry

import mysql.connector as mc 
mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
cursor=mycon.cursor(buffered=True)
elements=["Ar","Ta","Ge","Cn","Le","Vi","Li","Sc","Sa","Cp","Aq","Pi"]
plt=["Lagna","Sun","Moon","Mars","Mercury","Venus","Rahu","ketu","Saturn","Jupiter","Maandi"]
name="hariprasath"
save=name+str(datetime.datetime.now()).replace(" ","-").replace(":","-").replace(".","-")
datascraper.dataentry(name,"9-6-2005","14-5-0",save)
save=save+".txt"
cursor.execute("insert into entries(code,filename)""values(%s,%s)",[save.replace(name,""),save])
mycon.commit()
mycon.close()
def planetpositions():
    with open(f"prognostics//scraper//data//{save}","r+") as f:
        f.seek(750)
        f.readline()
        f.readline()
        data=[]
        for i in range(11):
            data.append(f.readline().split('"')[0])
    for ind in range(len(data)):
        dt=data[ind]
        for i in range(dt.count(" ")):
            dt=dt.replace(" ","")
        for i in plt:
            if i in dt: 
                dt=dt.replace(i,"")
        length=len(dt)
        for i in range(length):
            if dt[i].isdigit():
                break
            else:
                if dt.count(dt[i])==1:
                    dt=dt.replace(dt[i],"_")
        for i in range(dt.count("_")):
            dt=dt.replace("_","")
        dt=dt.replace("'","-")
        dt=dt[:-3]
        length=len(dt)
        while True:
            if dt[0].isalpha():
                dt=dt[1:]
            else:
                break
        if dt[1].isalpha():
            dt="0"+dt
        for ele in elements:
            if ele in dt:
                val=(elements.index(ele))*30
                dig=int(dt[0:2])+val
                dt=str(dig)+"-"+dt[4:]
        data[ind]=dt
    return data
positionentry.postionentry(name,planetpositions())
time.sleep(5)
def shadbala():
    with open(f"prognostics//scraper//data//{save}","r+") as f:
        for i in range(121):
            f.readline()
        data=[]
        for i in range(9):
            data.append(f.readline())
        [data.remove("\n") for i in range(data.count("\n"))]
        shadbaladic={}
        for ind in range(len(data)):
            ele=data[ind].replace("\n","")
            ele=ele.split("   ")
            for pl in plt:
                if pl in ele[0] and len(ele[0])>len(pl):
                    ele=[pl]+[ele[0].replace(pl,"")]+ele[1:]
                for itm in ele:
                    if itm=="":
                        ele.remove(itm)
                        continue
                    ele[ele.index(itm)]=itm.strip()
            shadbaladic[ele[0]]=[eval(i) for i in ele[1:]]
    return shadbaladic.copy()
shadbalamentry.shadbalamentry(name,list(shadbala().values()))
