import unittest

from task_tracker.parser import build_parser


class ParserTests(unittest.TestCase):
    def test_add_command_parses_description(self) -> None:
        args = build_parser().parse_args(["add", "Write tests"])

        self.assertEqual(args.action, "add")
        self.assertEqual(args.description, "Write tests")
        self.assertFalse(args.details)

    def test_list_command_parses_optional_status(self) -> None:
        args = build_parser().parse_args(["list", "done"])

        self.assertEqual(args.action, "list")
        self.assertEqual(args.status_filter, "done")


if __name__ == "__main__":
    unittest.main()
