# import mysql.connector as mc
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
#     cursor.execute("select name from planetarypositions;")
#     data=namecolumnsql(cursor.fetchall())
#     mycon.commit()
#     mycon.close()
#     for i in data:
#         if name==i:
#             return True
# def dataofname(name):
#     if namechecker(name):
#         mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
#         cursor=mycon.cursor(buffered=True)
#         cursor.execute("select * from planetarypositions where name=%s",(name,))
#         data=cursor.fetchall()
#         return data
# def namesindata():
#     mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
#     cursor=mycon.cursor(buffered=True)
#     cursor.execute("select name from planetarypositions;")
#     data=namecolumnsql(cursor.fetchall())
#     return data
# def deletedata(name):
#     if type(name)==type("test"):
#         name=[name,]
#     name=list(name)
#     for i in name:
#         if namechecker(i):
#             mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
#             cursor=mycon.cursor(buffered=True)
#             cursor.execute("delete from planetarypositions where name=%s",(i,))
#             mycon.commit()
#             mycon.close()
#             print("datas of {},deleted!".format(name))
# def dasachecker(name):
#     mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
#     cursor=mycon.cursor(buffered=True)
#     cursor.execute("select name from dasa;")
#     data=namecolumnsql(cursor.fetchall())
#     mycon.commit()
#     mycon.close()
#     for i in data:
#         if name==i:
#             return True
# def dasadata(name):
#     if dasachecker(name):
#         mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
#         cursor=mycon.cursor(buffered=True)
#         cursor.execute("select * from dasa where name=%s",(name,))
#         data=cursor.fetchall()
#         return data
