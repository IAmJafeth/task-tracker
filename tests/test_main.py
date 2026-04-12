from io import StringIO
import unittest

from task_tracker.main import run
from task_tracker.tasklist import TaskList


class FakeStorage:
    def __init__(self, task_list: TaskList | None = None, load_error: ValueError | None = None) -> None:
        self._task_list = task_list or TaskList()
        self._load_error = load_error
        self.saved = False

    def load(self) -> TaskList:
        if self._load_error is not None:
            raise self._load_error
        return self._task_list

    def save(self, task_list: TaskList) -> None:
        self._task_list = task_list
        self.saved = True


class MainRunTests(unittest.TestCase):
    def test_add_uses_injected_storage_and_output(self) -> None:
        storage = FakeStorage()
        out = StringIO()
        err = StringIO()

        exit_code = run(["add", "Testable command"], storage=storage, out=out, err=err)

        self.assertEqual(exit_code, 0)
        self.assertIn("Task added", out.getvalue())
        self.assertTrue(storage.saved)
        self.assertEqual(len(storage._task_list.list_tasks()), 1)
        self.assertEqual(err.getvalue(), "")

    def test_list_does_not_save(self) -> None:
        storage = FakeStorage()
        out = StringIO()
        err = StringIO()

        exit_code = run(["list"], storage=storage, out=out, err=err)

        self.assertEqual(exit_code, 0)
        self.assertIn("No tasks saved yet!", out.getvalue())
        self.assertFalse(storage.saved)
        self.assertEqual(err.getvalue(), "")

    def test_domain_error_goes_to_err_stream(self) -> None:
        storage = FakeStorage()
        out = StringIO()
        err = StringIO()

        exit_code = run(["delete", "10"], storage=storage, out=out, err=err)

        self.assertEqual(exit_code, 1)
        self.assertIn("Task 10 does not exist", err.getvalue())
        self.assertEqual(out.getvalue(), "")
        self.assertFalse(storage.saved)

    def test_storage_load_error_is_explicit(self) -> None:
        storage = FakeStorage(load_error=ValueError("broken file"))
        out = StringIO()
        err = StringIO()

        exit_code = run(["list"], storage=storage, out=out, err=err)

        self.assertEqual(exit_code, 1)
        self.assertIn("broken file", err.getvalue())
        self.assertEqual(out.getvalue(), "")
        self.assertFalse(storage.saved)


if __name__ == "__main__":
    unittest.main()
