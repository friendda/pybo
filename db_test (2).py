import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
##import sqlalchemy as db
import pandas as pd
import MySQLdb

##host = "127.0.0.1"
##port = "3306"
##database = "jumundb"
##username = "taeel"
##password = "friend4647"

##conn = pymysql.connect(host='127.0.0.1', user='taeel', passwd='friend4647', db='jumundb', charset='utf8')
##cur= conn.cursor()
engine = create_engine("mysql+pymysql://taeel:"+"friend4647"+"@127.0.0.1:3306/jumundb",encoding='utf-8')
conn = engine.connect()



##data = pd.read_sql_query('select *from jumun_t',conn)


##query = "select *from jumun_t"

##test = cur.execute(query) 쿼리된 갯수만 들어감.

##data = pd.read_sql_query(query, conn)


df =pd.read_excel('jumun100.xlsx')
##
df.to_sql(name='jumun_t',con=engine, if_exists='append',index=False )

conn.close()

##query = db.select([table])
##print(query) index_label='jumun_t_id'




