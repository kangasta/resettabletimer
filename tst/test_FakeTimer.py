from unittest import TestCase
from unittest.mock import Mock

from resettabletimer import FakeTimer


class FakeTimerTest(TestCase):
    def test_wont_call_without_start(self):
        m = Mock(return_value=None)
        t = FakeTimer(5, m)
        t.pass_time(5)
        m.assert_not_called()

    def test_cannot_start_twice(self):
        t = FakeTimer(0, lambda: None)
        t.start()
        with self.assertRaises(RuntimeError):
            t.start()

    def test_cannot_be_restarted_after_cancel(self):
        t = FakeTimer(0, lambda: None)
        t.start()
        t.cancel()
        with self.assertRaises(RuntimeError):
            t.start()

    def test_calls_function_after_time_has_passed(self):
        m = Mock(return_value=None)
        t = FakeTimer(5, m)
        t.start()
        t.pass_time(5)
        m.assert_called_once_with()

    def test_does_not_call_function_before_time_has_passed(self):
        m = Mock(return_value=None)
        t = FakeTimer(5, m)
        t.start()
        t.pass_time(3)
        m.assert_not_called()

    def test_timer_supports_args_and_kwargs(self):
        m = Mock(return_value=None)

        t = FakeTimer(3, m, ["args"], {"kwarg": "kwarg"})
        t.start()
        t.pass_time(3)
        m.assert_called_once_with("args", kwarg="kwarg")

    def test_timer_can_be_reset(self):
        m = Mock(return_value=None)

        t = FakeTimer(5, m)
        t.start()

        t.pass_time(3)
        m.assert_not_called()
        t.reset()

        t.pass_time(3)
        m.assert_not_called()

        t.pass_time(3)
        m.assert_called_once_with()

    def test_timer_can_be_reset_after_cancel(self):
        m = Mock(return_value=None)

        t = FakeTimer(5, m)
        t.start()

        t.pass_time(3)
        m.assert_not_called()
        t.cancel()
        t.reset()
        t.start()

        t.pass_time(6)
        m.assert_called_once_with()
