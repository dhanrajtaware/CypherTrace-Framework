from pathlib import Path
import json


class TimelineExporter:

    def export(
        self,
        timeline,
        filename
    ):

        exports_dir = Path(
            "exports"
        )

        exports_dir.mkdir(
            exist_ok=True
        )

        output_file = (
            exports_dir /
            f"{filename}_timeline.json"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                timeline,
                file,
                indent=4
            )

        return output_file