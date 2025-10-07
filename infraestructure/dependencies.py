from application.facade.UserFacade import UserFacade
from infraestructure.persistence.PostgreSQLUserRepository import PostgreSQLUserRepository

class Dependencies:
    
    user_repository = PostgreSQLUserRepository()

depens = Dependencies()

def get_user_facade() -> UserFacade:
    return UserFacade(depens.user_repository)