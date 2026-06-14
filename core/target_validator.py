import re
import ipaddress
import os

class TargetValidator:

    def detect(self, target):

        # Email
        email_pattern = (
            r"^[a-zA-Z0-9._%+-]+@"
            r"[a-zA-Z0-9.-]+\."
            r"[a-zA-Z]{2,}$"
        )

        if re.match(
            email_pattern,
            target
        ):
            return "email"

        # IP
        try:
            ipaddress.ip_address(
                target
            )
            return "ip"

        except ValueError:
            pass

        # Domain
        domain_pattern = (
            r"^(?!:\/\/)"
            r"([a-zA-Z0-9-]+\.)+"
            r"[a-zA-Z]{2,}$"
        )

        if re.match(
            domain_pattern,
            target
        ):
            return "domain"

        # File
        if os.path.isfile(target):
            return "file"

        # Username
        return "username"