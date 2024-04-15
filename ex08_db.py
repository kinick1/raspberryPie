# import pymysql as  ps
import spidevRead as sr
import databas as db

# conn=ps.connect(host='localhost',user='root', passwd='1234', db='test')
# curs=conn.cursor()

read=sr.analog_read(0)

sql=f"insert into sensordb(sensing) values({read})"
# curs.execute(sql)
# conn.commit()
db.db_insert(sql)

# 서술형 2개 객관식 5개 