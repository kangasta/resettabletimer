class FakeTimer(object):
	def __init__(self, time, function, args=[], kwargs={}):
		self.__time = time
		self.__function = function
		self.__args = args
		self.__kwargs = kwargs
		self.__canceled = False
		self.__started = False
		self.__passed = 0

	def start(self):
		if self.__started:
			raise RuntimeError("threads can only be started once")
		self.__started = True
		self.__passed = 0

	def cancel(self):
		self.__canceled = True

	def reset(self):
		self.__passed = 0
		if self.__canceled:
			self.__started = False
		self.__canceled = False

	def pass_time(self, time):
		self.__passed += time
		if not self.__canceled and self.__started and self.__passed >= self.__time:
			self.__function(*self.__args, **self.__kwargs)
