API_URL = 'https://api.milesplit.com/'

class Athlete:
	def __init__(self, id, name = None):
		self.id = id
		self.name = name
	def get_info(self, callback = 'received_json'):
		url = API_URL + '?callback=' + callback

yichen = Athlete(9356110, "Yichen Sun")
