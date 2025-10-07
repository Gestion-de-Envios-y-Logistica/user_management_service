from abc import ABC, abstractmethod
from typing import Dict, Any


class TokenService(ABC):
    
    @abstractmethod
    def create_token(self, payload: Dict[str, Any]) -> str:

        pass