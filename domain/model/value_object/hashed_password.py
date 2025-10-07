from dataclasses import dataclass
from domain.model.exception.business_exception import BusinessNotFoundError
import re

@dataclass(frozen=True)
class HashedPassword:
    
    hashed: str
    
    def __post_init__(self):
        if not self._is_valid_password(self.hashed):
            raise BusinessNotFoundError(self.hashed, "La contraseña no puede estar vacía.")
        
    def __str__(self) -> str:
        return self.hashed
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, HashedPassword):
            return False
        return self.hashed == other.hashed
    
    def __hash__(self) -> int:
        return hash(self.hashed)
    
    @staticmethod
    def _is_valid_password(password: str) -> bool:
        
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'[0-9]', password):
            return False
        return True