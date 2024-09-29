import psycopg

from queries import queries

conn = psycopg.connect(dbname="sensordata",
                       host="85.215.48.7",
                       user="postgres",
                       password="admin123",
                       port="5432")
cursor = conn.cursor()

cursor.execute(queries.hourly_query)

print(cursor.fetchall())

conn.close()