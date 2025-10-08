import uuid
from domain.model.user import User
from application.ports.UserRepository import UserRepository
from application.ports.TokenService import TokenService
from application.dto.UserDto import UserDto, UserResponseDto
from domain.model.exception.business_exception import BusinessNotFoundError

class AuthenticateUserUseCase:
    
    def __init__(self, user_repository: UserRepository, token_service: TokenService):
        self.user_repository = user_repository
        self.token_service = token_service

    async def execute(self, user_dto: UserDto) -> UserResponseDto:
        
        user = await self.user_repository.find_by_email(user_dto.email)
        
        if not user.check_password(user_dto.hashed_password):
            raise BusinessNotFoundError(user_dto.email, "Credenciales inválidas")
        
        token = self._generate_token_for_user(user)
        self.token_service.add(token, user.user_id)
        
        return self._build_user_response_dto(user, token)


    def _generate_token_for_user(self, user: User) -> str:
        
        return str(uuid.uuid4())
        

    def _build_user_response_dto(self, user: User, token: str) -> UserResponseDto:
        
        return UserResponseDto(
            user_id=user.user_id,
            email=user.email.email,
            is_active=user.is_active,
            token=token
        )

