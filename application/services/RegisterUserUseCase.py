from application.ports.UserRepository import UserRepository
from domain.model.user import User
from application.dto.UserDto import UserDto, UserResponseDto
from domain.model.factory.UserRegisterFactory import UserRegisterFactory


class RegisterUserUseCase:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        

    async def execute(self, user_data: UserDto) -> str:
        
        new_user = UserRegisterFactory.create(
            email=user_data.email,
            hashed_password=user_data.hashed_password
        )
        
        await self.user_repository.add(new_user)
        
        return self._build_user_response_dto(new_user)
    
    
    def _build_user_response_dto(self, user: User) -> str:
        
        return UserResponseDto(
            user_id=user.user_id,
            email=user.email.email,
            is_active=user.is_active
        )
        
        
        