import cx_Oracle

#create connection
conn = cx_Oracle.connect()
print(conn.version)


#creating cursor
cur = conn.cursor()

sql_create = """
CREATE TABLE DBS_DETAILS(
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    COMPANY VARCHAR2(50),
    JOINING DATE NUMBER
)"""

cur.execute(sql_create)
print('Table Created.')
