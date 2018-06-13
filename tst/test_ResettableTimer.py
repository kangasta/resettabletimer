from unittest import TestCase

try:
	from unittest.mock import Mock, patch
except ImportError:
	from mock import Mock, patch

from FakeTimer import FakeTimer
from ResettableTimer import ResettableTimer

class ResettableTimerTest(TestCase):
	def test_dummy(self):
		self.assertTrue(True)

	@patch("ResettableTimer.Timer", new=FakeTimer)
	def test_timer_can_be_reset(self):
		m = Mock(return_value=None)

		t = ResettableTimer(5, m)
		t.start()

		t._ResettableTimer__timer.pass_time(3)
		m.assert_not_called()
		t.reset()

		t._ResettableTimer__timer.pass_time(3)
		m.assert_not_called()

		t._ResettableTimer__timer.pass_time(3)
		m.assert_called_once_with()

	@patch("ResettableTimer.Timer", new=FakeTimer)
	def test_timer_can_be_reset_after_cancel(self):
		m = Mock(return_value=None)

		t = ResettableTimer(5, m)
		t.start()

		t._ResettableTimer__timer.pass_time(3)
		m.assert_not_called()
		t.cancel()
		t.reset()
		t.start()

		t._ResettableTimer__timer.pass_time(6)
		m.assert_called_once_with()
