import psycopg2
import time
import random

host = 'ec2-54-217-228-25.eu-west-1.compute.amazonaws.com'
database = 'd2tsnet6tkloap'
user = 'pasvxoxznuqssn'
password = '1042d286011f73c4bb42320560413fe329253b97261c2f8b61bb9b885acb8bea'

conn = psycopg2.connect(host = host, dbname = database, user = user, password = password)
conn.autocommit = True

with conn.cursor() as cursor:
	cursor.execute("SELECT id, result FROM main_numbergeneratetask WHERE status='Pending'")
	GenerateTasks = cursor.fetchall()
	for GenerateTask in GenerateTasks:
   		time.sleep(2)
   		temp = random.randint(1, 100)
    	cursor.execute("UPDATE main_numbergeneratetask SET status='Done', result = %s WHERE id=%s", (temp, GenerateTask[0],))

conn.close()