class FakeTimer(object):
    def __init__(self, time, function, args=None, kwargs=None):
        self._time = time
        self._function = function
        self._args = args if args is not None else []
        self._kwargs = kwargs if kwargs is not None else {}
        self._canceled = False
        self._started = False
        self._passed = 0

    def start(self):
        if self._started:
            raise RuntimeError("threads can only be started once")
        self._started = True
        self._passed = 0

    def cancel(self):
        self._canceled = True

    def reset(self):
        self._passed = 0
        if self._canceled:
            self._started = False
        self._canceled = False

    def pass_time(self, time):
        self._passed += time
        if not self._canceled and self._started and self._passed >= self._time:
            self._function(*self._args, **self._kwargs)
