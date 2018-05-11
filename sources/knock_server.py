from twisted.internet import protocol, reactor

class Knock(protocol.Protocol):
	def dataReceived(self, data):
		print 'Client:', data
		if data.startswith("Knock knock"):
			response = "Who's there"
		else:
			response = data + " who?"

		print 'Server:', response
		self.transport.write(response)

class KnockFactor(protocol.Factory):
	def buildProtocol(self, addr):
		return Knock()


reactor.listenTCP(18000, KnockFactor())
reactor.run()