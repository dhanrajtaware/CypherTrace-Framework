class EntityMapper:

    def build(self, findings):

        nodes = []
        edges = []

        for finding in findings:

            module = finding.get(
                "module"
            )

            if module == "subdomain_lookup":

                domain = finding.get(
                    "target"
                )

                nodes.append({
                    "type": "domain",
                    "value": domain
                })

                for subdomain in (
                    finding.get(
                        "subdomains",
                        []
                    )
                ):

                    nodes.append({
                        "type":
                            "subdomain",
                        "value":
                            subdomain
                    })

                    edges.append({
                        "source":
                            domain,
                        "target":
                            subdomain
                    })

        return {
            "nodes": nodes,
            "edges": edges
        }