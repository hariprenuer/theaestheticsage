# import mysql.connector as mc
# import positiongetter
# import sqlhelpers
# mycon=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
# cursor=mycon.cursor(buffered=True)
# cursor.execute("""create table if not exists planetarypositions (name char(100) unique not null,
# lagnam varchar(100),suriyan varchar(100),chandhiran varchar(100),sevvaai varchar(100),budhan varchar(100),
# guru varchar(100),sukkiran varchar(100),shani varchar(100),rahu varchar(100),kethu varchar(100),
# maandhi varchar(100));""")
# mycon.commit()
# planets=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu","maandhi"]
# plots=[]
# def postionentry(name,data=None):
#     if sqlhelpers.namechecker(name):
#         print("data exists!")
#     else:
#         plots=[]
#         if data is None:
#             print("data {} doesnt exist!".format(name))
#             print(f"enter the horoscope detials of {name}")
#             plots.append(name)
#             for i in range(len(planets)):
#                 plots.append(input("enter the position of the {}:".format(planets[i])))
#         else:
#             plots=[]
#             plots=[name]+data
#         cursor.execute(("insert into planetarypositions(name,lagnam,suriyan,chandhiran,sevvaai,budhan,guru,sukkiran,shani,rahu,ketu,maandhi)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"),plots)
#         print("data entered successfully!")
#         mycon.commit()
#         print(positiongetter.horoscopeblueprint(name).data)
#         mycon.close()