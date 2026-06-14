import requests


class BackupScanner:
    def __init__(self, domain):
        self.domain = domain

        self.backup_files = [
            "/backup.zip",
            "/website.zip",
            "/site.zip",
            "/db.sql",
            "/database.sql",
            "/backup.tar.gz",
            "/backup.rar"
        ]

    def run(self):

        findings = []

        for path in self.backup_files:

            url = f"https://{self.domain}{path}"

            try:

                response = requests.get(
                    url,
                    timeout=5,
                    stream=True
                )

                if response.status_code == 200:

                    findings.append({
                        "url": url,
                        "status": response.status_code
                    })

            except:
                pass

        return {
            "module": "backup_scanner",
            "target": self.domain,
            "count": len(findings),
            "findings": findings
        }