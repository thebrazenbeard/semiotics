import json
import subprocess
import sys
import unittest
from pathlib import Path

from semiotics import Context, Interpretation, Sign, Source, interpret


class EngineTests(unittest.TestCase):
    def setUp(self):
        self.sign = Sign("s", "red", "visual")
        self.source = Source("e", "observed convention")

    def test_context_selects_competing_readings(self):
        items = [
            Interpretation("a", "s", "stop", "e", frozenset({"road"})),
            Interpretation("b", "s", "recording", "e", frozenset({"studio"})),
            Interpretation("c", "s", "generic", "e"),
        ]
        result = interpret(self.sign, Context(frozenset({"road"})), items, [self.source])
        self.assertEqual([r.interpretation.id for r in result], ["a", "c"])

    def test_exclusion_and_missing_evidence(self):
        item = Interpretation("a", "s", "stop", "e", excluded_tags=frozenset({"studio"}))
        self.assertEqual(interpret(self.sign, Context(frozenset({"studio"})), [item], [self.source]), [])
        with self.assertRaisesRegex(ValueError, "unknown source"):
            interpret(self.sign, Context(), [item], [])

    def test_duplicate_ids_rejected(self):
        item = Interpretation("a", "s", "stop", "e")
        with self.assertRaisesRegex(ValueError, "duplicate"):
            interpret(self.sign, Context(), [item, item], [self.source])

    def test_cli_example(self):
        example = Path(__file__).resolve().parents[1] / "examples" / "registry.json"
        result = subprocess.run(
            [sys.executable, "-m", "semiotics.cli", str(example), "red-light", "--tag", "studio"],
            capture_output=True, text=True, check=True,
        )
        self.assertEqual([row["id"] for row in json.loads(result.stdout)], ["studio-recording"])


if __name__ == "__main__":
    unittest.main()
