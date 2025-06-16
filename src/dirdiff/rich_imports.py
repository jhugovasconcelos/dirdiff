import logging

from rich.logging import RichHandler
from rich.console import Console
from rich.table import Table

FORMAT = "%(asctime)s %(message)s"

logging.basicConfig(
    level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")

console = Console()
table = Table(title="Diretories Diff")