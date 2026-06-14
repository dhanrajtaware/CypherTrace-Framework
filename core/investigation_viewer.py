import json
from pathlib import Path


class InvestigationViewer:

    def view(
        self,
        investigation_id
    ):

        file_path = (
            Path(
                "investigations"
            )
            /
            investigation_id
            /
            "findings.json"
        )

        if not file_path.exists():

            print(
                "[!] Investigation not found"
            )

            return

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(
                file
            )

        print(
            json.dumps(
                data,
                indent=4
            )
        )