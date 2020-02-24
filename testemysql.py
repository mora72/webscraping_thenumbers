import mysql.connector

connection = mysql.connector.connect(host='127.0.0.1', port='3308', user='root', password='',
                                     database='cadastro', charset='utf8mb4')
cursor = connection.cursor(dictionary=True)
# query = "select * from cursos"
query = "select totaulas,count(*) from cursos where totaulas > 20 group by totaulas having count(*) >=2 " \
        "order by totaulas desc;"
cursor.execute(query)

# connection.commit()
for x in cursor:
    print(x)
