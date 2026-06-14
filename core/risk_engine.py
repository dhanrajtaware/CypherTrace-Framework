class RiskEngine:

    MODULE_SCORES = {
        "panel_discovery": 15,
        "robots_analyzer": 5,
        "env_scanner": 50,
        "backup_scanner": 40,
        "git_exposure": 60,
        "subdomain_lookup": 5
    }

    def calculate_score(self, findings):

        score = 0

        for finding in findings:

            module = finding.get("module")

            if finding.get("count", 0) > 0:

                score += self.MODULE_SCORES.get(
                    module,
                    0
                )

        return min(score, 100)

    def get_severity(self, score):

        if score < 20:
            return "LOW"

        elif score < 50:
            return "MEDIUM"

        elif score < 80:
            return "HIGH"

        return "CRITICAL"