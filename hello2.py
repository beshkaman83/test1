class Laptop:
	def __init__(self, model_name):
		self.model = model_name
		self.harakteristiki = {'model':model_name}
		self.processor()
		self.ram()
		self.video_card()
		self.hdd()
		self.motherboard()
		self.display_size()

	def processor(self):
		self.harakteristiki['processor'] = 'Core,i 8'

	def ram(self):
		self.harakteristiki['ram'] =  '32gb'

	def video_card(self):
		self.harakteristiki['video_card'] = '16gb'

	def hdd(self):
		self.harakteristiki['hdd'] = '3072gb'

	def motherboard(self):
		self.harakteristiki['motherboard'] = 'Intel'

	def display_size(self):
		self.harakteristiki['display_size'] = '32"'

laptop = Laptop(model_name='Asus')
print(laptop.model)
print(laptop.harakteristiki)	