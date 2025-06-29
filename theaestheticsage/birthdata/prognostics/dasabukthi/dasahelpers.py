import datetime
import math
dasaduration={"suriyan":6,"chandhiran":10,"sevvaai":7,"rahu":18,"guru":16,"shani":19,"budhan":17,"kethu":7,"sukiran":20}
dasaplanetaries=['suriyan','chandhiran','sevvaai','rahu','guru','shani','budhan','kethu','sukiran']
duration={"months":12,"days":30,"hours":24,"minutes":60,"seconds":60,"milliseconds":1000}
timeunits=['months', 'days', 'hours', 'minutes', 'seconds', 'milliseconds']
multipliers=[12,30,24,60,60,1000]
def dasahelper(date):
    data=[]
    if type(date)==type("string"):
        for i in date.split("-"):
                data.append(int(i))
        return data
def dateconftolist(date):
    if type(date)==type("string"):
        date=dasahelper(date)
        date=datetime.datetime(date[2],date[1],date[0])
    if type(date)==type(datetime.datetime(2020,2,3)):
        date=str(date.year)+"-"+str(date.month)+"-"+str(date.day)
        date=dasahelper(date)
    return date
def deltatodate(data):
    if type(data)==type(datetime.datetime(2020,2,3)-datetime.datetime(2021,2,3)):
        diff=int((data).days)
        age=[int(diff/365),int((diff%365)/30),int((diff%365)%30)]
        age=[int(diff/365),int(((diff%365)-int(diff/365))*365/12),int((diff%365)%30)]
        return datetime.datetime(age[0],age[1],age[2])
def listtodate(data):
    if type(data)==type([""]):
        data=datetime.datetime(data[0],data[1],data[2])
    if type(data)==type("string"):
        data=datetime.datetime(dasahelper(data)[0],dasahelper(data)[1],dasahelper(data)[2]) 
    return data   
def diffdaycal(date1,date2,date3=None):
    date1=listtodate(date1)
    date2=listtodate(date2)   
    if date1>date2:
        temp=date1
        date1=date2
        date2=temp     
    if date3!=None:
        diff2=deltatodate(date2-date1)
        date3=datetime.datetime(dasahelper(date3)[0],dasahelper(date3)[1],dasahelper(date3)[2])
        return deltatodate(date3-diff2)
    elif date3==None:
        return deltatodate(date2-date1)
def agecal(data,timedata):
    cur=[datetime.datetime.today().year,datetime.datetime.today().month,datetime.datetime.today().day]
    data=listtodate(dateconftolist(data))
    dob=[data.year,data.month,data.day]
    data=listtodate(dateconftolist(data))
    if cur[2]<dob[2]:
        cur[2]+=30
        cur[1]-=1
    if cur[1]<dob[1]:
        cur[1]+=12
        cur[0]-=1
    age=[cur[0]-dob[0],cur[1]-dob[1],cur[2]-dob[2]]
    count=0   
    for leap in range(dob[0],cur[0]):
        if (leap%100!=0 and leap%4==0) or (leap%400==0):
            count+=1
    age[2]+=count
    if age[2]>30:
        age[2]-=30
        age[1]+=1
    if age[1]==0:
        age[0]-=1
        age[1]+=12
    if age[2]==0:
        age[1]-=1
        age[2]+=30
    timedata=dasahelper(timedata)
    try:
        timedata[2]
    except:
        timedata.append(0)
    accurate=datetime.datetime.now()
    if accurate.hour<timedata[0]:
        hour=timedata[0]-accurate.hour
    else:
        hour=accurate.hour-timedata[0]
    if accurate.minute<timedata[1]:
        minute=timedata[1]-accurate.minute
    else:
        minute=accurate.minute-timedata[1]
    if accurate.second<timedata[2]:
        second=timedata[2]-accurate.second
    else:
        second=accurate.second-timedata[2]
    return datetime.datetime(age[0],age[1],age[2],hour=hour,minute=minute,second=second,microsecond=accurate.microsecond)
def actualdiff(data1,data2):
    days1=(data1[0]*12+data1[1])*30+data1[2]
    days2=(data2[0]*12+data2[1])*30+data2[2]
    return math.fabs(days1-days2)
def dateadder(date1,date2):
    return deltatodate(date1+date2)
def listchanger(data):
    listafchange=[]
    samp=[]
    if data in dasaplanetaries:
        for i in range(len(dasaplanetaries)):
            if i>=dasaplanetaries.index(data):
                listafchange.append(dasaplanetaries[i])
            else:
                samp.append(i)
        for i in samp:
            listafchange.append(dasaplanetaries[i])
        return listafchange
    if data in multipliers:
        for i in range(len(multipliers)):
            if i>=multipliers.index(data):
                listafchange.append(multipliers[i])
        return listafchange
def product(index):
    value=1
    multiplier=[30,24,60,60,1000]
    if index==0:
        return 1
    for iter in range(0,index):
        value=value*multiplier[iter]
    return value
def latestelement(data):
    for ele in data:
        if ele==None:
            return data[data.index(None)-1]
    if None not in data:
        return data[len(data)-1]
def influenceduration(data):
    count=0
    for ele in data:
        if ele in dasaplanetaries:
            count=count+1
    value=1
    for ele in data:
        if ele in dasaplanetaries:
            value=value*dasaduration[ele]
    value=value/math.pow(120,count-1)
    value=value*31104000000.0
    return value