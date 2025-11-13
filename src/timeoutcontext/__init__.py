import importlib.metadata

from ._timeout import timeout

__version__ = importlib.metadata.version("timeoutcontext")

__all__ = [
    "timeout",
]
