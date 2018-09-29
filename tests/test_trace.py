from unittest import TestCase
from unittest.mock import MagicMock

from suanillo import trace


class TestBase(TestCase):
    def setUp(self):
        self.log = MagicMock()
        self.log.with_id = MagicMock(return_value=self.log)
        self.decorator = trace.base(self.log)

    def test_doesnt_affect_the_decorated_function(self):
        ok_ret = "OK"
        ok_function = MagicMock(return_value=ok_ret)
        decorated = self.decorator(ok_function)
        args = (1, 2, 3)
        ans = decorated(*args)
        ok_function.assert_called_with(*args)
        self.assertEqual(ans, ok_ret)

    def test_handles_ok_function(self):
        ok_ret = "OK"
        ok_function = MagicMock(return_value=ok_ret)
        decorated = self.decorator(ok_function)
        args = (1, 2)
        decorated(*args)
        self.log.input.assert_called_with((args, {}))
        self.log.output.assert_called_with(ok_ret)

    def test_handles_err_function(self):
        err_ret = Exception("Err")
        err_function = MagicMock(side_effect=err_ret)
        decorated = self.decorator(err_function)
        args = (1, 2)
        with self.assertRaises(Exception):
            decorated(*args)
        self.log.input.assert_called_with((args, {}))
        self.log.error.assert_called_with(err_ret)

    def test_handles_recursion(self):
        @self.decorator
        def recursive_function(ctr):
            return recursive_function(ctr - 1) if ctr > 0 else 0
        recursive_function(2)
        self.assertEqual(self.log.input.call_count, 3)
        self.assertEqual(self.log.output.call_count, 3)
