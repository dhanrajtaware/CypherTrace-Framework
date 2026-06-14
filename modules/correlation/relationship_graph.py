class RelationshipGraph:

    def build(self, findings):

        graph = {
            "nodes": [],
            "edges": []
        }

        added_nodes = set()

        for finding in findings:

            module = finding.get(
                "module"
            )

            if module == "subdomain_lookup":

                target = finding.get(
                    "target"
                )

                if target and target not in added_nodes:

                    graph["nodes"].append({
                        "id": target,
                        "type": "domain"
                    })

                    added_nodes.add(
                        target
                    )

                for subdomain in finding.get(
                    "subdomains",
                    []
                ):

                    if subdomain not in added_nodes:

                        graph["nodes"].append({
                            "id": subdomain,
                            "type": "subdomain"
                        })

                        added_nodes.add(
                            subdomain
                        )

                    graph["edges"].append({
                        "source": target,
                        "target": subdomain,
                        "relation": "contains"
                    })

        return graph