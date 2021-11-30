from threading import Timer

class ResettableTimer(object):
	def __init__(self, time, function, args=[], kwargs={}):
		self.__time = time
		self.__function = function
		self.__args = args
		self.__kwargs = kwargs
		self.__set()
		self.__running = False

	def __set(self):
		self.__timer = Timer(self.__time, self.__function, self.__args, self.__kwargs)

	def start(self):
		self.__running = True
		self.__timer.start()

	def cancel(self):
		self.__running = False
		self.__timer.cancel()

	def reset(self, start=False):
		if self.__running:
			self.__timer.cancel()

		self.__set()

		if self.__running or start:
			self.start()
