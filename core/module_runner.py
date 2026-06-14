class ModuleRunner:

    def __init__(self, manager):
        self.manager = manager

    def run_module(
        self,
        investigation_id,
        module,
        module_name
    ):
        print(
            f"\n[+] Running {module_name}..."
        )

        results = module.run()

        self.manager.add_finding(
            investigation_id,
            results
        )

        print(
            f"[+] {module_name} Complete"
        )

        return results