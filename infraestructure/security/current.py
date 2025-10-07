# from fastapi.security import OAuth2PasswordBearer
# from typing import Annotated
# from fastapi import HTTPException, status, Depends

# from infraestructure.security.JWTTokenService import JWTTokenService

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(get_db)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Token inválido o expirado",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
    
#     payload = JWTTokenService.decode_access_token(token, credentials_exception)
#     existeng_user: int = payload.get("sub")
#     print(f"\nDatos decodificados: {existeng_user}")
#     if existeng_user is None:
#         raise credentials_exception
    
#     #user = db.query(UserModel).filter(UserModel.username == existeng_user).first()
    
#     if user is None:
#         raise credentials_exception
    
#     return user


