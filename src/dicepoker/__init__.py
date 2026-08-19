"""DicePoker: A dice poker game with rerolls and hand rankings."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]