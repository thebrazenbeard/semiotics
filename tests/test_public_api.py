import unittest

from semiotics import Interpretation, Registry, RegistryError, Sign, Source


class PublicApiTests(unittest.TestCase):
    def test_direct_constructor_rejects_dangling_source(self):
        with self.assertRaisesRegex(RegistryError, "unknown source"):
            Registry(
                signs=[Sign(id="s", form="x", modality="visual")],
                sources=[],
                interpretations=[
                    Interpretation(id="i", sign_id="s", meaning="m", source_id="missing")
                ],
            )

    def test_query_rejects_blank_context_tag(self):
        registry = Registry(
            signs=[Sign(id="s", form="x", modality="visual")],
            sources=[Source(id="src", description="example")],
            interpretations=[
                Interpretation(id="i", sign_id="s", meaning="m", source_id="src")
            ],
        )
        with self.assertRaisesRegex(RegistryError, "context tags"):
            registry.query("s", {"   "})

    def test_query_omits_absent_optional_source_metadata(self):
        registry = Registry(
            signs=[Sign(id="s", form="x", modality="visual")],
            sources=[Source(id="src", description="example")],
            interpretations=[
                Interpretation(id="i", sign_id="s", meaning="m", source_id="src")
            ],
        )
        source = registry.query("s")[0]["source"]
        self.assertNotIn("citation", source)
        self.assertNotIn("published_year", source)


if __name__ == "__main__":
    unittest.main()
