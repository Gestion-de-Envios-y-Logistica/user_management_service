from abc import ABC, abstractmethod
from typing import Optional
from domain.model.user import User

class UserRepository(ABC):
    
    @abstractmethod
    async def add(self, user: User) -> None:
        pass
    
    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[User]:
        pass
    
    