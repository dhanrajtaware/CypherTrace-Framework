import requests


class GitExposure:
    def __init__(self, domain):
        self.domain = domain

        self.git_paths = [
            "/.git/",
            "/.git/config",
            "/.git/HEAD"
        ]

    def run(self):

        findings = []

        for path in self.git_paths:

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
            "module": "git_exposure",
            "target": self.domain,
            "count": len(findings),
            "findings": findings
        }