from datetime import datetime

from core.storage import Storage


class InvestigationManager:
    def __init__(self):
        self.storage = Storage()

    def create_investigation(self, target, target_type):
        investigation_id = (
            f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        )

        metadata = {
            "id": investigation_id,
            "target": target,
            "target_type": target_type,
            "created": datetime.now().isoformat()
        }

        investigation_dir = (
            self.storage.create_investigation_dir(
                investigation_id
            )
        )

        self.storage.save_json(
            investigation_dir / "metadata.json",
            metadata
        )

        self.storage.save_json(
            investigation_dir / "findings.json",
            []
        )

        return investigation_id

    def add_finding(self, investigation_id, finding):
        investigation_dir = (
            self.storage.base_dir / investigation_id
        )

        findings_file = (
            investigation_dir / "findings.json"
        )

        findings = self.storage.load_json(
            findings_file
        )

        findings.append(finding)

        self.storage.save_json(
            findings_file,
            findings
        )

    def get_findings(self, investigation_id):
        investigation_dir = (
            self.storage.base_dir / investigation_id
        )

        return self.storage.load_json(
            investigation_dir / "findings.json"
        )