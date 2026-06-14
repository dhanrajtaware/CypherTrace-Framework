import whois


class DomainLookup:
    def __init__(self, domain):
        self.domain = domain

    def run(self):
        try:
            data = whois.whois(self.domain)

            return {
                "module": "domain_lookup",
                "target": self.domain,
                "registrar": str(data.registrar),
                "creation_date": str(data.creation_date),
                "expiration_date": str(data.expiration_date),
                "name_servers": (
                    list(data.name_servers)
                    if data.name_servers
                    else []
                )
            }

        except Exception as e:
            return {
                "module": "domain_lookup",
                "target": self.domain,
                "error": str(e)
            }