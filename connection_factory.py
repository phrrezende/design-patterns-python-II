import Mysqldb

class Conection_factory(object):

	def get_connection(self):
		connection = Mysqldb.connect(host="localhost",user="root", passwd="", db="teste")
		return connection
