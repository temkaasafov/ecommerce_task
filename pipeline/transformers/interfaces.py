from abc import ABC, abstractmethod
from typing import Any

class DataTransformer(ABC):
    """interface for data transformation"""
    @abstractmethod
    def transform(self) -> Any:
        pass