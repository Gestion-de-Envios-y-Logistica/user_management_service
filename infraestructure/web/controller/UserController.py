from fastapi import APIRouter, Depends, status
from application.facade.UserFacade import UserFacade
from infraestructure.dependencies import get_user_facade
from infraestructure.models import UserDto, UserResponseDto
from typing import Annotated


router = APIRouter(
    prefix="/register",
    tags=["register"],
)


@router.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseDto
)
async def create_user(
    user_dto: UserDto,
    user_facade: Annotated[UserFacade, Depends(get_user_facade)]
) -> UserResponseDto:
    
    return await user_facade.register_user(user_dto)
    
    
@router.get(
    "/users/{email}",
    status_code=status.HTTP_200_OK,
    response_model=UserResponseDto
)
async def get_user_by_email(
    email: str,
    user_facade: Annotated[UserFacade, Depends(get_user_facade)]
) -> UserResponseDto:
    
    return await user_facade.get_user_by_email(email)
