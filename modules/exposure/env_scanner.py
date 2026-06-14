import requests


class EnvScanner:
    def __init__(self, domain):
        self.domain = domain

        self.env_paths = [
            "/.env",
            "/.env.bak",
            "/.env.old",
            "/.env.local"
        ]

    def run(self):

        findings = []

        for path in self.env_paths:

            url = f"https://{self.domain}{path}"

            try:
                response = requests.get(
                    url,
                    timeout=5
                )

                if response.status_code == 200:

                    findings.append({
                        "url": url,
                        "status": response.status_code
                    })

            except:
                pass

        return {
            "module": "env_scanner",
            "target": self.domain,
            "count": len(findings),
            "findings": findings
        }