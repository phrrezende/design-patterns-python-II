from connection_factory import Connection_factory

connection = Connection_factory().get_connection()

cursor = connection.cursor()

cursor.execute("Select * from cursos")


for linha in cursor:
	print linha

connection.close()