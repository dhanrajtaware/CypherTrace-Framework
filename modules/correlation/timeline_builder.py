from datetime import datetime


class TimelineBuilder:

    def build(
        self,
        findings
    ):

        timeline = []

        timestamp = (
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        for finding in findings:

            timeline.append({

                "time":
                    timestamp,

                "module":
                    finding.get(
                        "module"
                    )
            })

        return timeline