from dataclasses import dataclass

@dataclass(frozen=True)
class UserDto:

    email: str
    hashed_password: str

@dataclass(frozen=True)
class EmailDto:
    
    email: str
    

@dataclass(frozen=True)
class UserResponseDto:
    
    user_id: str
    email: str
    is_active: bool
    token: str = None