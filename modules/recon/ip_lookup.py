import requests


class IPLookup:
    def __init__(self, ip):
        self.ip = ip

    def run(self):
        try:
            response = requests.get(
                f"http://ip-api.com/json/{self.ip}",
                timeout=10
            )

            data = response.json()

            return {
                "module": "ip_lookup",
                "ip": self.ip,
                "country": data.get("country"),
                "region": data.get("regionName"),
                "city": data.get("city"),
                "isp": data.get("isp"),
                "org": data.get("org"),
                "as": data.get("as")
            }

        except Exception as e:
            return {
                "module": "ip_lookup",
                "ip": self.ip,
                "error": str(e)
            }