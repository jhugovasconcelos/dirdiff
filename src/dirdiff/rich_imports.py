import logging

from rich.logging import RichHandler
from rich.console import Console
from rich.table import Table
from rich.style import Style

FORMAT = "%(asctime)s %(message)s"

logging.basicConfig(
    level="DEBUG", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")

console = Console()
table = Table(title="Directories Diff")
equal = Style(color='white', bgcolor='green')
different = Style(color='white', bgcolor='red', italic=True)