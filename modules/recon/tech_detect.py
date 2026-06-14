import builtwith


class TechDetect:
    def __init__(self, domain):
        self.domain = domain

    def run(self):
        try:
            technologies = builtwith.parse(
                f"https://{self.domain}"
            )

            return {
                "module": "tech_detect",
                "target": self.domain,
                "technologies": technologies
            }

        except Exception as e:
            return {
                "module": "tech_detect",
                "target": self.domain,
                "error": str(e)
            }