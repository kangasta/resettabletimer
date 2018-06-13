from unittest import TestCase
from unittest.mock import Mock

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

	def test_calls_function_after_time_has_passed(self):
		m = Mock(return_value=None)
		t = FakeTimer(5, m)
		t.pass_time(5)
		m.assert_called_once_with()

	def test_does_not_call_function_before_time_has_passed(self):
		m = Mock(return_value=None)
		t = FakeTimer(5, m)
		t.pass_time(3)
		m.assert_not_called()
