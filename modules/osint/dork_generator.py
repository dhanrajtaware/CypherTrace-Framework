class DorkGenerator:

    def __init__(
        self,
        target,
        target_type
    ):

        self.target = target
        self.target_type = target_type

    def run(self):

        dorks = {}

        if self.target_type == "domain":

            dorks = {

                "general": [

                    f"site:{self.target}",
                    f"site:{self.target} \"index of\"",
                    f"site:{self.target} intitle:index.of"
                ],

                "documents": [

                    f"site:{self.target} ext:pdf",
                    f"site:{self.target} ext:doc",
                    f"site:{self.target} ext:docx",
                    f"site:{self.target} ext:xls",
                    f"site:{self.target} ext:xlsx",
                    f"site:{self.target} ext:ppt",
                    f"site:{self.target} ext:pptx",
                    f"site:{self.target} ext:csv",
                    f"site:{self.target} ext:txt"
                ],

                "admin_panels": [

                    f"site:{self.target} inurl:admin",
                    f"site:{self.target} inurl:login",
                    f"site:{self.target} intitle:login",
                    f"site:{self.target} inurl:dashboard",
                    f"site:{self.target} inurl:portal",
                    f"site:{self.target} inurl:cpanel"
                ],

                "backups": [

                    f"site:{self.target} ext:bak",
                    f"site:{self.target} ext:old",
                    f"site:{self.target} ext:zip",
                    f"site:{self.target} ext:rar",
                    f"site:{self.target} ext:7z",
                    f"site:{self.target} ext:tar",
                    f"site:{self.target} ext:gz"
                ],

                "source_code": [

                    f"site:{self.target} ext:sql",
                    f"site:{self.target} ext:log",
                    f"site:{self.target} ext:conf",
                    f"site:{self.target} ext:ini",
                    f"site:{self.target} ext:yml",
                    f"site:{self.target} ext:yaml",
                    f"site:{self.target} ext:json"
                ],

                "sensitive_files": [

                    f"site:{self.target} \".env\"",
                    f"site:{self.target} \".git\"",
                    f"site:{self.target} \".git/config\"",
                    f"site:{self.target} \"config.php\"",
                    f"site:{self.target} \"web.config\"",
                    f"site:{self.target} \"database.yml\"",
                    f"site:{self.target} \"credentials\"",
                    f"site:{self.target} \"secret_key\""
                ],

                "cloud_storage": [

                    f"site:{self.target} inurl:s3.amazonaws.com",
                    f"site:{self.target} inurl:blob.core.windows.net",
                    f"site:{self.target} inurl:storage.googleapis.com"
                ],

                "wordpress": [

                    f"site:{self.target} inurl:wp-admin",
                    f"site:{self.target} inurl:wp-content",
                    f"site:{self.target} inurl:wp-includes",
                    f"site:{self.target} \"wp-config\""
                ]
            }

        elif self.target_type == "email":

            dorks = {

                "email": [

                    f"\"{self.target}\"",
                    f"\"{self.target}\" filetype:pdf",
                    f"\"{self.target}\" filetype:doc",
                    f"\"{self.target}\" filetype:docx"
                ],

                "social_media": [

                    f"\"{self.target}\" site:linkedin.com",
                    f"\"{self.target}\" site:x.com",
                    f"\"{self.target}\" site:facebook.com",
                    f"\"{self.target}\" site:instagram.com"
                ],

                "developer": [

                    f"\"{self.target}\" site:github.com",
                    f"\"{self.target}\" site:gitlab.com",
                    f"\"{self.target}\" site:bitbucket.org"
                ],

                "leaks": [

                    f"\"{self.target}\" site:pastebin.com",
                    f"\"{self.target}\" site:ghostbin.com",
                    f"\"{self.target}\" password",
                    f"\"{self.target}\" leak"
                ]
            }

        elif self.target_type == "username":

            dorks = {

                "username": [

                    f"\"{self.target}\""
                ],

                "social_media": [

                    f"\"{self.target}\" site:x.com",
                    f"\"{self.target}\" site:facebook.com",
                    f"\"{self.target}\" site:instagram.com",
                    f"\"{self.target}\" site:linkedin.com"
                ],

                "developer": [

                    f"\"{self.target}\" site:github.com",
                    f"\"{self.target}\" site:gitlab.com",
                    f"\"{self.target}\" site:stackoverflow.com"
                ],

                "communities": [

                    f"\"{self.target}\" site:reddit.com",
                    f"\"{self.target}\" site:medium.com",
                    f"\"{self.target}\" site:quora.com"
                ],

                "leaks": [

                    f"\"{self.target}\" site:pastebin.com",
                    f"\"{self.target}\" password",
                    f"\"{self.target}\" leak"
                ]
            }

        elif self.target_type == "ip":

            dorks = {

                "ip": [

                    f"\"{self.target}\""
                ],

                "search_engines": [

                    f"\"{self.target}\" site:shodan.io",
                    f"\"{self.target}\" site:censys.io"
                ],

                "logs": [

                    f"\"{self.target}\" ext:log",
                    f"\"{self.target}\" ext:conf",
                    f"\"{self.target}\" ext:txt"
                ],

                "exposure": [

                    f"\"{self.target}\" \"index of\"",
                    f"\"{self.target}\" password",
                    f"\"{self.target}\" login"
                ]
            }

        return {

            "module": "Dork Generator",

            "target": self.target,

            "target_type": self.target_type,

            "dorks": dorks
        }