import unittest
from pathlib import Path

from semiotics import load_registry


ROOT = Path(__file__).resolve().parents[1]


class CorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = load_registry(ROOT / "corpus/foundations.json")

    def test_sign_keeps_peirce_and_saussure_readings_separate(self):
        peirce = self.registry.query("sign", {"framework:peirce"})
        saussure = self.registry.query("sign", {"framework:saussure"})
        self.assertEqual(peirce[0]["interpretation"]["id"], "sign-peirce-triadic")
        self.assertEqual(
            saussure[0]["interpretation"]["id"],
            "sign-saussure-differential",
        )

    def test_peirce_classification_is_queryable(self):
        result = self.registry.query("index", {"framework:peirce"})
        self.assertEqual(result[0]["interpretation"]["id"], "index-peirce")
        self.assertEqual(result[0]["source"]["published_year"], 2022)

    def test_morris_dimensions_are_queryable(self):
        result = self.registry.query("pragmatics", {"framework:morris"})
        self.assertEqual(result[0]["interpretation"]["id"], "pragmatics-morris")
        self.assertEqual(result[0]["source"]["published_year"], 1938)

    def test_framework_specific_readings_do_not_match_without_context(self):
        self.assertEqual(self.registry.query("sign"), [])


if __name__ == "__main__":
    unittest.main()
