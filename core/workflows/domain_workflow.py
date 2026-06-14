from modules.recon.dns_lookup import DNSLookup
from modules.recon.ip_lookup import IPLookup
from modules.recon.domain_lookup import DomainLookup
from modules.recon.subdomain_lookup import SubdomainLookup
from modules.recon.tech_detect import TechDetect
from modules.recon.panel_discovery import PanelDiscovery
from modules.osint.dork_generator import (
    DorkGenerator
)
from modules.exposure.robots_analyzer import RobotsAnalyzer
from modules.exposure.env_scanner import EnvScanner
from modules.exposure.backup_scanner import BackupScanner
from modules.exposure.git_exposure import GitExposure
from modules.osint.dork_generator import (
    DorkGenerator
)
from modules.osint.email_lookup import EmailLookup


class DomainWorkflow:

    def __init__(self, manager, runner):
        self.manager = manager
        self.runner = runner

    def run(self, investigation_id, target):

        dns = DNSLookup(target)

        dns_results = self.runner.run_module(
            investigation_id,
            dns,
            "DNS Lookup"
        )

        a_records = dns_results["records"].get(
            "A",
            []
        )

        if a_records:

            ip_lookup = IPLookup(
                a_records[0]
            )

            self.runner.run_module(
                investigation_id,
                ip_lookup,
                "IP Lookup"
            )

        self.runner.run_module(
            investigation_id,
            DomainLookup(target),
            "Domain Lookup"
        )

        self.runner.run_module(
            investigation_id,
            EmailLookup(target),
            "Email Lookup"
        )

        self.runner.run_module(
            investigation_id,
            SubdomainLookup(target),
            "Subdomain Lookup"
        )

        self.runner.run_module(
            investigation_id,
            TechDetect(target),
            "Technology Detection"
        )

        self.runner.run_module(
            investigation_id,
            PanelDiscovery(target),
            "Panel Discovery"
        )

        self.runner.run_module(
            investigation_id,
            RobotsAnalyzer(target),
            "Robots Analyzer"
        )

        self.runner.run_module(
            investigation_id,
            EnvScanner(target),
            "ENV Scanner"
        )

        self.runner.run_module(
            investigation_id,
            BackupScanner(target),
            "Backup Scanner"
        )

        self.runner.run_module(
            investigation_id,
            GitExposure(target),
            "Git Exposure"
        )

        self.runner.run_module(
            investigation_id,
            DorkGenerator(target),
            "Dork Generator"
        )
        self.runner.run_module(
            investigation_id,
            DorkGenerator(
                target,
                "domain"
            ),
            "Dork Generator"
        )