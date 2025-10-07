import uuid
import bcrypt
from domain.model.user import User
from domain.model.value_object.email_object import EmailObject
from domain.model.value_object.hashed_password import HashedPassword

class UserRegisterFactory:
    
    @staticmethod
    def create(email: str, hashed_password: str) -> User:
        
        user_id = str(uuid.uuid4())
        email_vo = EmailObject(email)
        
        password_bytes = hashed_password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        hashed_password_str = hashed_password.decode('utf-8')
        hashed_password_vo = HashedPassword(hashed_password_str)
        
        return User(
            user_id=user_id, 
            email=email_vo, 
            hashed_password=hashed_password_vo
        )