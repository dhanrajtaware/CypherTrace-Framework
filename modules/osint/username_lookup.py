import requests


class UsernameLookup:

    def __init__(self, username):

        self.username = username

        self.platforms = {
            "GitHub":
                f"https://github.com/{username}",

            "Reddit":
                f"https://www.reddit.com/user/{username}",

            "Instagram":
                f"https://www.instagram.com/{username}/",

            "TikTok":
                f"https://www.tiktok.com/@{username}",

            "X":
                f"https://x.com/{username}"
        }

    def check_profile(
        self,
        platform,
        url
    ):

        try:

            response = requests.get(
                url,
                timeout=5,
                headers={
                    "User-Agent":
                    "Mozilla/5.0"
                }
            )

            return {
                "platform": platform,
                "url": url,
                "exists":
                    response.status_code == 200
            }

        except Exception:

            return {
                "platform": platform,
                "url": url,
                "exists": False
            }

    def run(self):

        findings = []

        for platform, url in (
            self.platforms.items()
        ):

            findings.append(
                self.check_profile(
                    platform,
                    url
                )
            )

        return {
            "module":
                "username_lookup",

            "username":
                self.username,

            "results":
                findings
        }