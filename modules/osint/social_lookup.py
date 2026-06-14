import requests


class SocialLookup:

    def __init__(self, username):

        self.username = username

        self.platforms = {
            "GitHub":
                f"https://github.com/{username}",

            "Reddit":
                f"https://www.reddit.com/user/{username}",

            "LinkedIn":
                f"https://www.linkedin.com/in/{username}",

            "Instagram":
                f"https://www.instagram.com/{username}/"
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

        results = []

        for platform, url in (
            self.platforms.items()
        ):

            results.append(
                self.check_profile(
                    platform,
                    url
                )
            )

        return {
            "module":
                "social_lookup",

            "username":
                self.username,

            "results":
                results
        }