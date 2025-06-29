# import mysql.connector as mc
# import shadbalahelper as se
# mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
# cursor=mycon.cursor(buffered=True)
# cursor.execute(""" create table if not exists shadbala (name varchar(100) unique not null,suriyan varchar(100),
# chandhiran varchar(100),sevvaai varchar(100),budhan varchar(100),guru varchar(100),sukiran varchar(100),shani varchar(100));""")
# mycon.commit()
# planets=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu","maandhi"]
# plots=[]
# def shadbalamentry(name,data=None):
#     if se.namechecker(name):
#         print("data exists!")
#     else:
#         plots=[name]
#         for ele in data:
#             str1=""
#             for item in ele:
#                 str1=str1+str(item)+"-"
#             plots.append(str1)
#         cursor.execute(("insert into shadbala(name,suriyan,chandhiran,sevvaai,budhan,guru,sukiran,shani)""values(%s,%s,%s,%s,%s,%s,%s,%s)"),plots)
#         print("data entered successfully!")
#         mycon.commit()
#         mycon.close()