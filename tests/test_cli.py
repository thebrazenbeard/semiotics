import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "-m", "semiotics.cli", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_example_studio_context(self):
        proc = self.run_cli("examples/registry.json", "red-light", "--tag", "studio")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload[0]["interpretation"]["meaning"], "Recording in progress")

    def test_road_context_returns_road_reading(self):
        proc = self.run_cli("examples/registry.json", "red-light", "--tag", "road")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(payload[0]["interpretation"]["meaning"], "Stop at the signal")

    def test_unknown_sign_is_structured_error(self):
        proc = self.run_cli("examples/registry.json", "missing")
        self.assertEqual(proc.returncode, 2)
        self.assertEqual(proc.stdout, "")
        self.assertEqual(json.loads(proc.stderr)["error"], "unknown sign 'missing'")

    def test_no_context_yields_empty_for_example(self):
        proc = self.run_cli("examples/registry.json", "red-light")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(proc.stdout), [])


if __name__ == "__main__":
    unittest.main()
