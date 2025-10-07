from application.ports.UserRepository import UserRepository
from domain.model.user import User
from application.dto.UserDto import UserDto, EmailDto
from application.services.RegisterUserUseCase import RegisterUserUseCase
from typing import Optional


class UserFacade:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = RegisterUserUseCase(user_repository)

    async def register_user(self, user: UserDto) -> str:
        return await self.user_repository.execute(user)
        

    async def get_user_by_email(self, email: EmailDto) -> Optional[User]:
        return await self.user_repository.execute(email)
        