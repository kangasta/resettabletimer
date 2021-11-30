from threading import Timer


class ResettableTimer(object):
    def __init__(self, time, function, args=None, kwargs=None):
        self._time = time
        self._function = function
        self._args = args
        self._kwargs = kwargs
        self._set()
        self._running = False

    def _set(self):
        self._timer = Timer(
            self._time,
            self._function,
            self._args,
            self._kwargs)

    def start(self):
        self._running = True
        self._timer.start()

    def cancel(self):
        self._running = False
        self._timer.cancel()

    def reset(self, start=False):
        if self._running:
            self._timer.cancel()

        self._set()

        if self._running or start:
            self.start()
