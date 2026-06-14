from pathlib import Path


class InvestigationSearch:

    def search(
        self,
        keyword
    ):

        investigations_dir = Path(
            "investigations"
        )

        investigations_dir.mkdir(
            exist_ok=True
        )

        matches = []

        for file in (
            investigations_dir.glob(
                "*.json"
            )
        ):

            content = (
                file.read_text(
                    encoding="utf-8"
                )
            )

            if keyword.lower() in (
                content.lower()
            ):

                matches.append(
                    file.stem
                )

        if not matches:

            print(
                "[!] No matches found"
            )

            return

        print(
            "\nMatches Found:\n"
        )

        for match in matches:

            print(
                f" - {match}"
            )