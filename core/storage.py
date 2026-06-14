import json
from pathlib import Path


class Storage:
    def __init__(self):
        self.base_dir = Path("investigations")
        self.base_dir.mkdir(exist_ok=True)

    def create_investigation_dir(self, investigation_id):
        investigation_dir = self.base_dir / investigation_id
        investigation_dir.mkdir(exist_ok=True)
        return investigation_dir

    def save_json(self, filepath, data):
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_json(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)