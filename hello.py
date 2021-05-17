print('Hello world!')

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