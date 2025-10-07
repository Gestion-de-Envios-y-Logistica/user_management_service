from application.ports.UserRepository import UserRepository
from domain.model.user import User
from application.dto.UserDto import EmailDto, UserResponseDto

class GetUserByEmail:
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, email: EmailDto) -> UserResponseDto:
        
        user = await self.user_repository.find_by_email(email)
        return self._build_user_response_dto(user)

    def _build_user_response_dto(self, user: User) -> UserResponseDto:
        
        return UserResponseDto(
            user_id=user.user_id,
            email=user.email.email,
            is_active=user.is_active
        )



