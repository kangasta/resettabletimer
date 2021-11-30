from unittest import TestCase

try:
	from unittest.mock import Mock, patch
except ImportError:
	from mock import Mock, patch

from resettabletimer import FakeTimer, ResettableTimer

class ResettableTimerTest(TestCase):
	def test_dummy(self):
		self.assertTrue(True)

	@patch("resettabletimer._resettabletimer.Timer", new=FakeTimer)
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

	@patch("resettabletimer._resettabletimer.Timer", new=FakeTimer)
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

	@patch("resettabletimer._resettabletimer.Timer", new=FakeTimer)
	def test_timer_supports_args_and_kwargs(self):
		m = Mock(return_value=None)

		t = ResettableTimer(3, m, ["args"], {"kwarg":"kwarg"})
		t.start()
		t._ResettableTimer__timer.pass_time(3)
		m.assert_called_once_with("args", kwarg="kwarg")

	@patch("resettabletimer._resettabletimer.Timer", new=FakeTimer)
	def test_timer_can_be_started_with_reset(self):
		m = Mock(return_value=None)

		t = ResettableTimer(3, m)
		t._ResettableTimer__timer.pass_time(3)
		m.assert_not_called()

		t.reset(start=True)
		t._ResettableTimer__timer.pass_time(3)
		m.assert_called_once_with()