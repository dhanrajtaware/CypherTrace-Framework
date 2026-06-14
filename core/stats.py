from pathlib import Path


class Stats:

    def show(self):

        investigations = len(
            list(
                Path(
                    "investigations"
                ).iterdir()
            )
        )

        reports = len(
            list(
                Path(
                    "reports"
                ).glob("*")
            )
        )

        exports = len(
            list(
                Path(
                    "exports"
                ).glob("*")
            )
        )

        print(
            "\nCypherTrace Statistics\n"
        )

        print(
            f"Investigations : "
            f"{investigations}"
        )

        print(
            f"Reports        : "
            f"{reports}"
        )

        print(
            f"Exports        : "
            f"{exports}"
        )