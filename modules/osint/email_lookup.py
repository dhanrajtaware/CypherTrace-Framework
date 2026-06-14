import dns.resolver


class EmailLookup:
    def __init__(self, domain):
        self.domain = domain

    def get_record(self, record_type):
        try:
            answers = dns.resolver.resolve(
                self.domain,
                record_type
            )

            return [
                str(record)
                for record in answers
            ]

        except Exception:
            return []

    def check_spf(self):
        txt_records = self.get_record("TXT")

        for record in txt_records:

            if "v=spf1" in record.lower():
                return True

        return False

    def check_dmarc(self):
        try:

            dns.resolver.resolve(
                f"_dmarc.{self.domain}",
                "TXT"
            )

            return True

        except Exception:
            return False

    def run(self):

        mx_records = self.get_record(
            "MX"
        )

        txt_records = self.get_record(
            "TXT"
        )

        return {
            "module": "email_lookup",
            "target": self.domain,
            "mx_records": mx_records,
            "txt_records": txt_records,
            "spf_enabled":
                self.check_spf(),
            "dmarc_enabled":
                self.check_dmarc()
        }