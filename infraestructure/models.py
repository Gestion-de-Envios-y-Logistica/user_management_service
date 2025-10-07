from pydantic import BaseModel, EmailStr


class UserDto(BaseModel):
   
    email: EmailStr
    hashed_password: str
    
class EmailDto(BaseModel):
    
    email: EmailStr
    
class UserResponseDto(BaseModel):
    
    user_id: str
    email: EmailStr
    is_active: bool
    token: str = None