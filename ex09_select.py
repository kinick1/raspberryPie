# import pymysql as ps
# conn=ps.Connect(host='localhost',user='root', passwd='1234', db='test')
# curs=conn.cursor();
# 
# sql='select *from sensordb'
# curs.execute(sql)
# result=curs.fetchall()
# print(result)
# 
# for s,t in result:
#     print(f'sensing :{s} / ts : {t}')
#     
#     
    
import pymysql as ps
import databas as db
conn=ps.Connect(host='localhost',user='root', passwd='1234', db='test')
curs=conn.cursor();

def select_db():
    sql='select *from sensordb'
    result=db.db_select(sql)
    r='<br>'.join(map(str,result))
    return r

select_db()
# for s,t in result:
#     print(f'sensing :{s} / ts : {t}')