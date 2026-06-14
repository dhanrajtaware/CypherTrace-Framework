from modules.osint.username_lookup import (
    UsernameLookup
)

from modules.osint.social_lookup import (
    SocialLookup
)

from modules.osint.dork_generator import (
    DorkGenerator
)


class UsernameWorkflow:

    def __init__(
        self,
        manager,
        runner
    ):

        self.manager = manager
        self.runner = runner

    def run(
        self,
        investigation_id,
        target
    ):

        print(
            "\n[+] Running Username Lookup..."
        )

        self.runner.run_module(
            investigation_id,
            UsernameLookup(
                target
            ),
            "Username Lookup"
        )

        print(
            "[+] Username Lookup Complete"
        )

        print(
            "\n[+] Running Social Lookup..."
        )

        self.runner.run_module(
            investigation_id,
            SocialLookup(
                target
            ),
            "Social Lookup"
        )

        print(
            "[+] Social Lookup Complete"
        )

        print(
            "\n[+] Generating Google Dorks..."
        )

        self.runner.run_module(
            investigation_id,
            DorkGenerator(
                target,
                "username"
            ),
            "Dork Generator"
        )

        print(
            "[+] Dork Generation Complete"
        )