from core.workflows.domain_workflow import (
    DomainWorkflow
)

from core.workflows.email_workflow import (
    EmailWorkflow
)

from core.workflows.username_workflow import (
    UsernameWorkflow
)

from core.workflows.file_workflow import (
    FileWorkflow
)


class WorkflowFactory:

    @staticmethod
    def get_workflow(
        target_type,
        manager,
        runner
    ):

        if target_type == "domain":
            return DomainWorkflow(
                manager,
                runner
            )

        elif target_type == "email":
            return EmailWorkflow(
                manager,
                runner
            )

        elif target_type == "username":
            return UsernameWorkflow(
                manager,
                runner
            )
        
        elif target_type == "file":

            return FileWorkflow(
                manager,
                runner
            )

        raise ValueError(
            f"Unsupported target type: "
            f"{target_type}"
        )