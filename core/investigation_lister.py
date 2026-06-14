from pathlib import Path


class InvestigationLister:

    def list_investigations(self):

        investigations_dir = Path(
            "investigations"
        )

        investigations_dir.mkdir(
            exist_ok=True
        )

        files = [
            item
            for item in investigations_dir.iterdir()
            if item.is_dir()
        ]

        if not files:

            print(
                "[!] No investigations found"
            )

            return

        print(
            "\nInvestigations:\n"
        )

        for file in files:

            print(
                f" - {file.name}"
            )