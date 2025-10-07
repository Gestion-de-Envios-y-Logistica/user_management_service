from application.ports.UserRepository import UserRepository
from domain.model.user import User
from typing import Dict
from domain.model.exception.business_exception import BusinessNotFoundError, BusinessConflictError



class PostgreSQLUserRepository(UserRepository):
    
    def __init__(self):
        self._session: Dict[str, User] = {}

    async def add(self, user: User) -> None:
        
        user_exists = any(b for b in self._session.values() if b.email == user.email)
        if user_exists:
            raise BusinessConflictError(user.email, "El usuario con este email ya existe")
        self._session[user.user_id] = user
        

    async def find_by_email(self, email: str) -> User:
        
        user = next((b for b in self._session.values() if b.email == email), None)
        if not user:
            raise BusinessNotFoundError(email, "Usuario no encontrado")
        return user

