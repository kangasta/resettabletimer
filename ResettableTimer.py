
from threading import Timer

class ResettableTimer(object):
	def __init__(self, time, function):
		self.__time = time
		self.__function = function
		self.__set()
		self.__running = False

	def __set(self):
		self.__timer = Timer(self.__time, self.__function)

	def start(self):
		self.__running = True
		self.__timer.start()

	def cancel(self):
		self.__running = False
		self.__timer.cancel()

	def reset(self):
		if self.__running:
			self.__timer.cancel()

		self.__set()

		if self.__running:
			self.start()

if __name__ == "__main__":
	from time import sleep
	from datetime import datetime

	print("Start 5 second timer (" + str(datetime.now().time()) + ")")
	r = ResettableTimer(5, lambda : print("Done (" + str(datetime.now().time()) + ")"))
	r.start()

	print("Sleep 3 seconds (" + str(datetime.now().time()) + ")")
	sleep(3)

	print("Reset 5 second timer (" + str(datetime.now().time()) + ")")
	r.reset()
