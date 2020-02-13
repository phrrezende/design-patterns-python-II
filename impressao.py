class Impressao(object):

	def visita_soma(self, soma):
		print('(', end="")
		soma.expressao_esquerda.aceita(self)
		print('+', end="")
		soma.expressao_direita.aceita(self)
		print(')', end="")

	def visita_subtracao(self, subtracao):
		print('(', end="")
		subtracao.expressao_esquerda.aceita(self)
		print('-', end="")
		subtracao.expressao_esquerda.aceita(self)
		print(')', end="")

	def visita_numero(self,numero):
		print(numero.avalia(), end="")


class Prefixa_visitor(object):

	def visita_soma(self,soma):
		print('+', end="")
		print('(', end="")
		soma.expressao_esquerda.aceita(self)
		soma.expressao_direita.aceita(self)
		print(')', end="")

	def visita_subtracao(self, subtracao):
		print('-', end="")
		print('(', end="")
		subtracao.expressao_esquerda.aceita(self)
		subtracao.expressao_esquerda.aceita(self)
		print(')', end="")

	def visita_numero(self,numero):
		print(numero.avalia(), end="")