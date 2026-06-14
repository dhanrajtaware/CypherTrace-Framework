import requests


class RobotsAnalyzer:
    def __init__(self, domain):
        self.domain = domain

    def run(self):
        url = f"https://{self.domain}/robots.txt"

        try:
            response = requests.get(
                url,
                timeout=5
            )

            if response.status_code != 200:
                return {
                    "module": "robots_analyzer",
                    "target": self.domain,
                    "found": False
                }

            disallowed = []

            for line in response.text.splitlines():

                if line.lower().startswith(
                    "disallow:"
                ):
                    disallowed.append(
                        line.split(
                            ":", 1
                        )[1].strip()
                    )

            return {
                "module": "robots_analyzer",
                "target": self.domain,
                "found": True,
                "disallowed_paths": disallowed
            }

        except Exception as e:
            return {
                "module": "robots_analyzer",
                "target": self.domain,
                "error": str(e)
            }