from abc import ABC, abstractmethod
from typing import Any

class DbExtractor(ABC):
    """interface for extracting data from db"""
    @abstractmethod
    def extract(self) -> Any:
        pass

class FileExtractor(ABC):
    """ interface for extracting data from nested zip structure"""
    def _outer_archives(self) -> Any:
        pass
    def _read_json_bytes(self, b) -> Any:
        pass
    def _iter_events(self) -> Any:
        pass
    def extract(self) -> Any:
        pass