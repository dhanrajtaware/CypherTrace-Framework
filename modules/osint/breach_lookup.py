import hashlib


class BreachLookup:

    def __init__(self, email):
        self.email = email

    def run(self):

        return {
            "module": "breach_lookup",
            "email": self.email,
            "breach_count": 0,
            "breaches": [],
            "risk": "LOW"
        }