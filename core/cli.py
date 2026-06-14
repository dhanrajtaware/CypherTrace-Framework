import argparse


class CLI:

    def parse(self):

        parser = argparse.ArgumentParser(
            prog="CypherTrace",
            description=(
                "OSINT • Recon • Investigation Framework"
            ),
            formatter_class=
            argparse.RawTextHelpFormatter
        )

        subparsers = (
            parser.add_subparsers(
                dest="command",
                metavar="COMMAND"
            )
        )

        # Scan Command
        scan = (
            subparsers.add_parser(
                "scan",
                help=(
                    "Run investigation "
                    "against a target"
                )
            )
        )

        scan.add_argument(
            "target",
            help=(
                "Domain, email, "
                "IP or username"
            )
        )

        # List Command
        subparsers.add_parser(
            "list",
            help=(
                "List investigations"
            )
        )

        # Stats Command
        subparsers.add_parser(
            "stats",
            help=(
                "Show framework statistics"
            )
        )

        # Version Command
        subparsers.add_parser(
            "version",
            help=(
                "Show framework version"
            )
        )

        # Report Command
        report = (
            subparsers.add_parser(
                "report",
                help=(
                    "View investigation "
                    "report"
                )
            )
        )

        report.add_argument(
            "investigation_id",
            help=(
                "Investigation ID"
            )
        )

        # Search Command
        search = (
            subparsers.add_parser(
                "search",
                help=(
                    "Search investigations"
                )
            )
        )

        search.add_argument(
            "keyword",
            help=(
                "Search keyword"
            )
        )

        return parser.parse_args()