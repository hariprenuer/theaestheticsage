# import mysql.connector as mc
# shadbalaplanets=["suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani"]
# def namecolumnsql(data):
#     data=str(data).replace("(","").replace(")","").replace("'","").replace("[","").replace("]","").split(",")
#     for i in range(data.count("")):
#         data.remove("")
#     for i in range(len(data)):
#         data[i]=data[i].strip()
#     return data
# def namechecker(name):
#     mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
#     cursor=mycon.cursor(buffered=True)
#     cursor.execute("select name from shadbala;")
#     data=namecolumnsql(cursor.fetchall())
#     mycon.commit()
#     mycon.close()
#     for i in data:
#         if name==i:
#             return True
# def datacollector(name):
#     if namechecker(name):
#         mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
#         cursor=mycon.cursor(buffered=True)
#         cursor.execute("select * from shadbala;")
#         data=namecolumnsql(cursor.fetchall())
#         mycon.commit()
#         mycon.close()
#         data=[[float(i) for i in ele.split("-")[:-1]] for ele in data[1:]]
#         planetdic={shadbalaplanets[ind]:(data[ind][2])/100 for ind in range(len(data))}
#         planetdic["rahu"]=1.00
#         planetdic["kethu"]=1.00
#         return planetdic.copy()