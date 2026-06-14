import dns.resolver


class DNSLookup:
    def __init__(self, domain):
        self.domain = domain

    def get_records(self, record_type):
        try:
            answers = dns.resolver.resolve(
                self.domain,
                record_type
            )

            return [str(record) for record in answers]

        except Exception:
            return []

    def run(self):
        return {
            "module": "dns_lookup",
            "target": self.domain,
            "records": {
                "A": self.get_records("A"),
                "MX": self.get_records("MX"),
                "NS": self.get_records("NS"),
                "TXT": self.get_records("TXT")
            }
        }