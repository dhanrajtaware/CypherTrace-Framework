from modules.osint.email_lookup import (
    EmailLookup
)

from modules.osint.breach_lookup import (
    BreachLookup
)

from modules.osint.dork_generator import (
    DorkGenerator
)


class EmailWorkflow:

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
            "\n[+] Running Email Lookup..."
        )

        self.runner.run_module(
            investigation_id,
            EmailLookup(
                target
            ),
            "Email Lookup"
        )

        print(
            "[+] Email Lookup Complete"
        )

        print(
            "\n[+] Running Breach Lookup..."
        )

        try:

            self.runner.run_module(
                investigation_id,
                BreachLookup(
                    target
                ),
                "Breach Lookup"
            )

            print(
                "[+] Breach Lookup Complete"
            )

        except Exception as error:

            print(
                f"[!] Breach Lookup Failed: "
                f"{error}"
            )

        print(
            "\n[+] Generating Google Dorks..."
        )

        self.runner.run_module(
            investigation_id,
            DorkGenerator(
                target,
                "email"
            ),
            "Dork Generator"
        )

        print(
            "[+] Dork Generation Complete"
        )