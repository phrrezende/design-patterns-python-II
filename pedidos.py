from datetime import date
from abc import ABCMeta, abstractmethod

class Pedido(object):

	def __init__(self, cliente, valor):
		self.__cliente = cliente
		self.__valor = valor
		self.__status = "NOVO"
		self.__data_finalizacao = None

	def paga(self):
		self.__pago = 'PAGO'

	def finaliza(self):
		self.__data_finalizacao = date.today()
		self.__status = 'Entregue'

	@property
	def cliente(self):
		return self.__cliente

	@property
	def valor(self):
		return self.__valor
	
	@property
	def status(self):
		return self.__status

	@property
	def data_finalizacao(self):
		return self.__data_finalizacao


class Comando(metaclass=ABCMeta):

	@abstractmethod
	def executa(self):
		pass

class Conclui_pedido(Comando):

	def __init__(self, pedido):

		self.__pedido = pedido

	def executa(self):
		self.__pedido.finaliza()

class Paga_pedido(Comando):

	def __init__(self,pedido):
		self.__pedido = pedido

	def executa(self):
		self.__pedido.paga()

class Fila_de_trabalho(object):

	def __init__(self):

		self.__comandos = []
	
	def adiciona(self, comando):
		self.__comandos.append(comando)

	def processa(self):
		for comando in self.__comandos:
			comando.executa()

if __name__ == '__main__':

	pedido1 = Pedido('Paulo', 200)
	pedido2 = Pedido('Monica', 300)

	print('Status do pedido 1: '+ pedido1.status)
	print('Status do pedido 2: '+ pedido2.status)
	fila = Fila_de_trabalho()
	fila.adiciona(Conclui_pedido(pedido1))
	fila.adiciona(Paga_pedido(pedido1))
	fila.adiciona(Conclui_pedido(pedido2))

	
	fila.processa()
	
	print('Status do pedido 1: '+ pedido1.status)
	print('Status do pedido 2: '+ pedido2.status)