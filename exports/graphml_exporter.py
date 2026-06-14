from pathlib import Path
import xml.etree.ElementTree as ET


class GraphMLExporter:

    def export(
        self,
        graph_data,
        filename
    ):

        graphml = ET.Element(
            "graphml"
        )

        graph = ET.SubElement(
            graphml,
            "graph",
            edgedefault="directed"
        )

        for node in (
            graph_data["nodes"]
        ):

            ET.SubElement(
                graph,
                "node",
                id=str(
                    node["value"]
                )
            )

        for edge in (
            graph_data["edges"]
        ):

            ET.SubElement(
                graph,
                "edge",
                source=str(
                    edge["source"]
                ),
                target=str(
                    edge["target"]
                )
            )

        exports_dir = Path(
            "exports"
        )

        exports_dir.mkdir(
            exist_ok=True
        )

        output_file = (
            exports_dir /
            f"{filename}.graphml"
        )

        tree = ET.ElementTree(
            graphml
        )

        tree.write(
            output_file,
            encoding="utf-8",
            xml_declaration=True
        )

        return output_file