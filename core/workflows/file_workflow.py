from modules.osint.metadata_extractor import (
    MetadataExtractor
)


class FileWorkflow:

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

        self.runner.run_module(
            investigation_id,
            MetadataExtractor(target),
            "Metadata Extractor"
        )