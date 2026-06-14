import urllib.parse


class DorkURLGenerator:

    def generate(
        self,
        dorks
    ):

        urls = []

        for dork in dorks:

            url = (
                "https://www.google.com/search?q="
                +
                urllib.parse.quote(
                    dork
                )
            )

            urls.append(
                {
                    "dork": dork,
                    "url": url
                }
            )

        return urls