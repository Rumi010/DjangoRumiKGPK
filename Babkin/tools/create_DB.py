import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="111", host="127.0.0.1")
cursor = conn.cursor()

conn.autocommit = True
sql = "CREATE DATABASE Babkin_webb"

cursor.execute(sql)
print("БД успешно создана")

cursor.close()
conn.close()