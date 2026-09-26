import unittest

from minagi import tools
import corpora.tool_use as tu


class ToolUseLaneTests(unittest.TestCase):
    def test_render_balances_markers(self):
        import random
        rng = random.Random(0)
        for _ in range(200):
            s = tu.render_turn(rng)
            self.assertEqual(s.count(tu.T0), s.count(tu.T1))
            self.assertEqual(s.count(tu.R0), s.count(tu.R1))
            # every rendered turn is a parseable tool call
            self.assertEqual(len(tools.parse_tool_calls(s)), 1)


if __name__ == "__main__":
    unittest.main()
