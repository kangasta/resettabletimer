from unittest import TestCase

from FakeTimer import FakeTimer

class FakeTimerTest(TestCase):
	def test_cannot_start_twice(self):
		t = FakeTimer(0, lambda : None)
		t.start()
		with self.assertRaises(RuntimeError):
			t.start()


	def test_cannot_be_restarted_after_cancel(self):
		t = FakeTimer(0, lambda : None)
		t.start()
		t.cancel()
		with self.assertRaises(RuntimeError):
			t.start()
