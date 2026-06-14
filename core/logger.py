from pathlib import Path
import logging


class Logger:

    @staticmethod
    def get_logger():

        logs_dir = Path(
            "logs"
        )

        logs_dir.mkdir(
            exist_ok=True
        )

        logging.basicConfig(
            filename=(
                logs_dir /
                "cyphertrace.log"
            ),
            level=logging.INFO,
            format=(
                "%(asctime)s "
                "[%(levelname)s] "
                "%(message)s"
            )
        )

        return logging.getLogger(
            "CypherTrace"
        )