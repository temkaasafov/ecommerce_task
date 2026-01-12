from abc import ABC, abstractmethod
from typing import Any

class DataLoader(ABC):
    """interface for load the data"""
    @abstractmethod
    def load(self, df) -> Any:
        pass