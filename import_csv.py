import pathlib
import csv
import mysql.connector

csv_path = pathlib.Path.cwd() / "FINAL.csv"

dict_list = list()
with csv_path.open(mode="r") as csv_reader:
    csv_reader = csv.reader(csv_reader)
    for rows in csv_reader:
        dict_list.append({'Column1':rows[0], 'Column2':rows[1], 'Column3':rows[2], 'Column4':rows[3], 'Column5':rows[4]})


mydatabase = mysql.connector.connect(
    username = 'root',
    password = 'root',
    host = 'localhost',
    database = 'test',
)

mycursor = mydatabase.cursor()

mycursor.execute("DROP TABLE IF EXISTS uni")
mycursor.execute("CREATE TABLE uni (Column1 TEXT, Column2 TEXT, Column3 TEXT, Column4 TEXT, Column5 TEXT)")

for item in dict_list:
    sql = "INSERT INTO uni VALUES (%s, %s, %s, %s, %s)"
    val = item['Column1'], item['Column2'], item['Column3'], item['Column4'], item['Column5']
    mycursor.execute(sql, val)
mydatabase.commit()


mycursor.execute('SELECT * FROM emptable')
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mydatabase.close()

