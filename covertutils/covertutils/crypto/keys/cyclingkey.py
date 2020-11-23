from abc import ABCMeta, abstractmethod



class CyclingKey(metaclass=ABCMeta) :

	def __init__( self, passphrase, **kw ) :
		pass

	@abstractmethod
	def cycle( self, rounds = 1) :
		pass


	@abstractmethod
	def getUUIDBytes( self, length ) :
		pass


	@abstractmethod
	def getKeyBytes( self, length ) :
		pass


	@abstractmethod
	def getKeyLength( self ) :
		"""
:rtype: int
:return: Returns the key length.
		"""
		pass


	@abstractmethod
	def reset( self ) : 	pass


	@abstractmethod
	def setCycle( self, cycle ) :	pass


	@abstractmethod
	def getCycles( self ) : pass
