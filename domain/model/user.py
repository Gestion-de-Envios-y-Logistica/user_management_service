from dataclasses import dataclass
from domain.model.value_object.email_object import EmailObject
from domain.model.value_object.hashed_password import HashedPassword
from domain.model.exception.business_exception import BusinessNotFoundError

@dataclass
class User:
    
    user_id: str
    email: EmailObject
    hashed_password: HashedPassword
    is_active: bool = True
    
    def __post_init__(self):
        if not self.user_id or not self.user_id.strip():
            raise BusinessNotFoundError( self.user_id,"El ID de usuario no puede estar vacío.")
        
    def deactivate(self):
        self.is_active = False
        
    def activate(self):
        self.is_active = True
        
    def change_email(self, new_email: str):
        self.email = EmailObject(new_email)
        
    def change_password(self, new_hashed_password: str):
        self.hashed_password = HashedPassword(new_hashed_password)
        
