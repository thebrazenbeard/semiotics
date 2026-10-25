"""Static editor-startup defenses; never execute workspace task payloads."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class WorkspaceStartupSafetyTests(unittest.TestCase):
    def test_tasks_configuration_is_valid_json_without_folder_open_execution(self):
        raw = (ROOT / ".vscode" / "tasks.json").read_text(encoding="utf-8")
        tasks = json.loads(raw)
        self.assertNotIn('"runOn": "folderOpen"', raw)
        self.assertNotRegex(raw, r"\bnode\s+[^\n]*public/fonts/")
        self.assertFalse(any(
            task.get("runOptions", {}).get("runOn") == "folderOpen"
            for task in tasks.get("tasks", [])
        ))

    def test_automatic_workspace_tasks_are_disabled(self):
        settings = json.loads(
            (ROOT / ".vscode" / "settings.json").read_text(encoding="utf-8")
        )
        self.assertIs(settings.get("task.allowAutomaticTasks"), False)
        self.assertNotIn("tasks", settings)

    def test_no_disguised_executable_asset(self):
        self.assertFalse((ROOT / "public/fonts/fa-solid.lkf").exists())


if __name__ == "__main__":
    unittest.main()
