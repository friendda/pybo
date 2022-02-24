import sqlite3 as db
import pandas as pd

##con = db.connect('db.sqlite3')
##
##query = 'select * from jumun_T limit 1000'
##df = pd.read_sql(query, con = con)

##print(df)

conn= db.connect("test.db")
##c = conn.cursor()

##c.execute('select *From test')
##one = c.fetchone()
##print(one)

##c.execute('''CREATE TABLE jumun_T(id integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
##eng_flag varchar(10) NULL, jumun_date varchar(30) NULL, jumun_id varchar(30
##) NULL, jumun_name varchar(30) NULL, jumun_con varchar(30) NULL, brand var
##char(30) NULL, prd_name text NULL, prd_color text NULL, quantity smallint
##NULL, wholesale varchar(30) NULL, whole_pr varchar(30) NULL, note text NUL
##L, sup_pr varchar(30) NULL, name varchar(30) NULL, phone varchar(30) NULL,
## address text NULL, jumun_id2 varchar(30) NULL, date2 varchar(30) NULL)''')
##c.execute("SELECT * FROM jumun_T")

##print(c.fetchone())

df = pd.read_excel(r"C:\projects\mysite\jumun.xlsx", header = 0)


df.to_sql('test3',conn, chunksize=1000)
