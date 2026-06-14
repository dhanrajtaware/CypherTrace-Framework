from pathlib import Path


class HTMLReportGenerator:

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

        report_file = (
            reports_dir /
            f"{investigation_id}.html"
        )

        html = f"""
        <html>
        <head>
            <title>
                CypherTrace Report
            </title>
        </head>

        <body>

        <h1>
            CypherTrace Investigation
        </h1>

        <h2>
            Risk Score: {score}
        </h2>

        <h2>
            Severity: {severity}
        </h2>

        <hr>
        """

        for finding in findings:

            html += f"""
            <h3>
                {finding.get('module')}
            </h3>

            <pre>
{finding}
            </pre>
            """

        html += """
        </body>
        </html>
        """

        with open(
            report_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)

        return report_file