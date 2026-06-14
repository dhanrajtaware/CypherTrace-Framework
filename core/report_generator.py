from pathlib import Path
import json
from core.findings_formatter import (
    FindingsFormatter
)

class ReportGenerator:

    def generate(
        self,
        investigation_id,
        findings,
        score,
        severity
    ):

        reports_dir = Path("reports")

        reports_dir.mkdir(
            exist_ok=True
        )

        report_path = (
            reports_dir /
            f"{investigation_id}.json"
        )

        report = {
            "investigation_id":
                investigation_id,
            "risk_score":
                score,
            "severity":
                severity,
            "findings":
                findings
        }

        with open(
            report_path,
            "w",
            encoding="utf-8"
        ) as file:

            formatter = (
                FindingsFormatter()
            )

            formatted = (
                formatter.format(
                    findings
                )
            )

        return report_path