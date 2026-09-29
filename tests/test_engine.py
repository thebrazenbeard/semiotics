import unittest

from semiotics.engine import Registry, RegistryError


def registry_payload():
    return {
        "signs": [{"id": "s", "form": "x", "modality": "visual"}],
        "sources": [{"id": "src", "description": "example"}],
        "interpretations": [
            {
                "id": "general",
                "sign_id": "s",
                "meaning": "general",
                "source_id": "src",
            },
            {
                "id": "specific",
                "sign_id": "s",
                "meaning": "specific",
                "source_id": "src",
                "required_tags": ["a"],
                "excluded_tags": ["b"],
            },
        ],
    }


class RegistryTests(unittest.TestCase):
    def test_more_specific_matches_sort_first(self):
        registry = Registry.from_dict(registry_payload())
        result = registry.query("s", {"a"})
        self.assertEqual(
            [item["interpretation"]["id"] for item in result],
            ["specific", "general"],
        )

    def test_excluded_tag_blocks_match(self):
        registry = Registry.from_dict(registry_payload())
        result = registry.query("s", {"a", "b"})
        self.assertEqual(
            [item["interpretation"]["id"] for item in result],
            ["general"],
        )

    def test_unknown_source_fails_explicitly(self):
        payload = registry_payload()
        payload["interpretations"][0]["source_id"] = "missing"
        with self.assertRaisesRegex(RegistryError, "unknown source"):
            Registry.from_dict(payload)

    def test_duplicate_interpretation_id_fails(self):
        payload = registry_payload()
        payload["interpretations"].append(dict(payload["interpretations"][0]))
        with self.assertRaisesRegex(RegistryError, "duplicate interpretation"):
            Registry.from_dict(payload)

    def test_same_tag_cannot_be_required_and_excluded(self):
        payload = registry_payload()
        payload["interpretations"][0]["required_tags"] = ["x"]
        payload["interpretations"][0]["excluded_tags"] = ["x"]
        with self.assertRaisesRegex(RegistryError, "requires and excludes"):
            Registry.from_dict(payload)


if __name__ == "__main__":
    unittest.main()
