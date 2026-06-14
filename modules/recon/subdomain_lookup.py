import requests


class SubdomainLookup:
    def __init__(self, domain):
        self.domain = domain

    def run(self):
        try:
            url = (
                f"https://crt.sh/?q=%25.{self.domain}&output=json"
            )

            response = requests.get(
                url,
                timeout=15
            )

            data = response.json()

            subdomains = set()

            for entry in data:

                name = entry.get(
                    "name_value",
                    ""
                )

                for subdomain in name.split("\n"):

                    subdomain = (
                        subdomain.strip()
                    )

                    if self.domain in subdomain:
                        subdomains.add(
                            subdomain
                        )

            return {
                "module": "subdomain_lookup",
                "target": self.domain,
                "count": len(subdomains),
                "subdomains": sorted(
                    list(subdomains)
                )
            }

        except Exception as e:
            return {
                "module": "subdomain_lookup",
                "target": self.domain,
                "error": str(e)
            }