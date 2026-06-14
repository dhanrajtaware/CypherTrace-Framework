from utils.banner import (
    show
)
from config import VERSION
from core.stats import (
    Stats
)
from core.investigation_lister import (
    InvestigationLister
)
from core.investigation_manager import (
    InvestigationManager
)

from core.cli import (
    CLI
)

from core.investigation_search import (
    InvestigationSearch
)

from core.investigation_viewer import (
    InvestigationViewer
)

from core.module_runner import (
    ModuleRunner
)
from modules.correlation.entity_mapper import (
    EntityMapper
)
from modules.correlation.timeline_builder import (
    TimelineBuilder
)
from exports.graphml_exporter import (
    GraphMLExporter
)
from exports.timeline_exporter import (
    TimelineExporter
)
from core.risk_engine import (
    RiskEngine
)

from core.report_generator import (
    ReportGenerator
)

from core.html_report_generator import (
    HTMLReportGenerator
)

from core.target_validator import (
    TargetValidator
)

from core.workflow_factory import (
    WorkflowFactory
)


def main():

    cli = CLI()

    args = cli.parse()

    if args.command == "list":

        InvestigationLister().list_investigations()

        return
    
    elif args.command == "version":

        print(
            f"CypherTrace v{VERSION}"
        )

        return
    
    elif args.command == "report":

        InvestigationViewer().view(
            args.investigation_id
        )

        return

    elif args.command == "search":

        InvestigationSearch().search(
            args.keyword
        )

        return

    elif args.command == "stats":

        Stats().show()
    
        return

    elif args.command == "scan":

        target = args.target

    else:

        print(
            "Use --help"
        )

        return

    show()

    manager = InvestigationManager()

    runner = ModuleRunner(
        manager
    )

    validator = (
        TargetValidator()
    )

    target_type = (
        validator.detect(
            target
        )
    )

    print(
        f"\n[+] Target Type: "
        f"{target_type}"
    )

    investigation_id = (
        manager.create_investigation(
            target,
            target_type
        )
    )

    print(
        f"[+] Investigation Created: "
        f"{investigation_id}"
    )

    workflow = (
        WorkflowFactory.get_workflow(
            target_type,
            manager,
            runner
        )
    )

    workflow.run(
        investigation_id,
        target
    )

    findings = (
        manager.get_findings(
            investigation_id
        )
    )

    mapper = EntityMapper()
    graph_data = mapper.build(findings)

    graph_exporter = (
        GraphMLExporter()
    )

    graph_file = (
        graph_exporter.export(
            graph_data,
            investigation_id
        )
    )

    timeline_builder = (
        TimelineBuilder()
    )

    timeline = (
        timeline_builder.build(
            findings
        )
    )

    timeline_exporter = (
        TimelineExporter()
    )

    timeline_file = (
        timeline_exporter.export(
            timeline,
            investigation_id
        )
    )

    risk_engine = (
        RiskEngine()
    )

    score = (
        risk_engine.calculate_score(
            findings
        )
    )

    severity = (
        risk_engine.get_severity(
            score
        )
    )

    report_generator = (
        ReportGenerator()
    )

    report_path = (
        report_generator.generate(
            investigation_id,
            findings,
            score,
            severity
        )
    )

    html_generator = (
        HTMLReportGenerator()
    )

    html_path = (
        html_generator.generate(
            investigation_id,
            findings,
            score,
            severity
        )
    )

    print(
        f"\n[+] Risk Score: {score}"
    )

    print(
        f"[+] Severity: {severity}"
    )

    print(
        f"[+] JSON Report: "
        f"{report_path}"
    )

    print(
        f"[+] HTML Report: "
        f"{html_path}"
    )

    print(
    f"[+] GraphML Export: "
    f"{graph_file}"
    )

    print(
    f"[+] Timeline Export: "
    f"{timeline_file}"
    )

    print(
        "\n[+] Investigation Complete"
    )


if __name__ == "__main__":
    main()