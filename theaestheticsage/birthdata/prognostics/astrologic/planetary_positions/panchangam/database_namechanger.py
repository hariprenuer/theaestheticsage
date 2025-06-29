# import mysql.connector as mc
# mycon=mc.connect(host="localhost",user="root",database="horoscope",passwd="080104201057sql#")
# cursor=mycon.cursor(buffered=True)
# cursor.execute("select * from planetarypositions;")
# data=cursor.fetchall()
# mycon1=mc.connect(host="localhost",user="root",database="theaestheticsage",passwd="080104201057sql#")
# cursor1=mycon1.cursor(buffered=True)
# cursor1.execute("""create table if not exists planetarypositions (name char(100) unique not null,
# lagnam varchar(100),suriyan varchar(100),chandhiran varchar(100),sevvaai varchar(100),budhan varchar(100),
# guru varchar(100),sukkiran varchar(100),shani varchar(100),rahu varchar(100),ketu varchar(100),
# maandhi varchar(100));""")
# planets=["lagnam","suriyan","chandhiran","sevvaai","budhan","guru","sukiran","shani","rahu","kethu","mandhi"]
# for i in range(len(data)):
#    cursor1.execute(("insert into planetarypositions(name,lagnam,suriyan,chandhiran,sevvaai,budhan,guru,sukkiran,shani,rahu,ketu,maandhi)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"),data[i])
# mycon.commit()
# mycon1.commit()
# mycon.close()
# mycon1.close()