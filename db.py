import pymysql
import csv
conn = pymysql.connect(host="localhost", user="root",passwd="15352113",db="reviews")
mycursor = conn.cursor()   
mycursor.execute ("select comment from opinions")     
data = mycursor.fetchall()
with open('dataset.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    header = ['comment']
    writer.writerow(header)
    for row in data:
        writer.writerow(row)
conn.commit()
conn.close()
