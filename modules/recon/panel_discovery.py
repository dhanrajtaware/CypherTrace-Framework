import requests


class PanelDiscovery:
    def __init__(self, domain):
        self.domain = domain

        self.common_panels = [
            "/admin",
            "/login",
            "/dashboard",
            "/wp-admin",
            "/phpmyadmin",
            "/admin/login",
            "/administrator",
            "/cpanel"
        ]

    def run(self):
        findings = []

        for path in self.common_panels:

            url = f"https://{self.domain}{path}"

            try:
                response = requests.get(
                    url,
                    timeout=5,
                    allow_redirects=True
                )

                if response.status_code in [200, 301, 302, 403]:

                    findings.append({
                        "url": url,
                        "status": response.status_code
                    })

            except:
                pass

        return {
            "module": "panel_discovery",
            "target": self.domain,
            "count": len(findings),
            "findings": findings
        }