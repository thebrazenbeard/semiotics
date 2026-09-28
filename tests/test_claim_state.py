import unittest

from semiotics import Context, Interpretation, Sign, Source, interpret


class ClaimStateTests(unittest.TestCase):
    def setUp(self):
        self.sign = Sign("s", "smoke", "visual")
        self.source = Source("obs", "observed smoke", evidence_class="observation")

    def test_rejected_interpretation_is_preserved_but_not_returned_live(self):
        rejected = Interpretation(
            "fire", "s", "fire is present", "obs",
            status="rejected", theory_tags=frozenset({"peirce:index"}), support=0.2,
        )
        live = Interpretation(
            "machine", "s", "machine emitted vapor", "obs",
            status="unresolved", theory_tags=frozenset({"peirce:index"}), support=0.6,
        )
        result = interpret(self.sign, Context(), [rejected, live], [self.source])
        self.assertEqual([r.interpretation.id for r in result], ["machine"])

    def test_support_is_metadata_not_ranking_authority(self):
        high = Interpretation("z-high", "s", "high score", "obs", support=0.99)
        low = Interpretation("a-low", "s", "low score", "obs", support=0.01)
        result = interpret(self.sign, Context(), [high, low], [self.source])
        self.assertEqual([r.interpretation.id for r in result], ["a-low", "z-high"])

    def test_support_must_be_probability_when_present(self):
        with self.assertRaisesRegex(ValueError, "support"):
            Interpretation("bad", "s", "bad", "obs", support=1.01)

    def test_unknown_status_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "status"):
            Interpretation("bad", "s", "bad", "obs", status="certain")


class IntegrityTests(unittest.TestCase):
    def test_source_evidence_class_must_not_be_empty(self):
        with self.assertRaisesRegex(ValueError, "evidence class"):
            Source("s", "source", evidence_class="")

    def test_rejected_interpretation_still_requires_valid_source(self):
        item = Interpretation("i", "s", "old reading", "missing", status="rejected")
        with self.assertRaisesRegex(ValueError, "unknown source"):
            interpret(Sign("s", "x", "text"), Context(), [item], [])

    def test_duplicate_source_ids_fail_closed(self):
        item = Interpretation("i", "s", "reading", "src")
        sources = [Source("src", "one"), Source("src", "two")]
        with self.assertRaisesRegex(ValueError, "duplicate source"):
            interpret(Sign("s", "x", "text"), Context(), [item], sources)


if __name__ == "__main__":
    unittest.main()
