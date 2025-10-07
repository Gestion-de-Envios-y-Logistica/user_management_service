import uvicorn
from fastapi import FastAPI
from infraestructure.web.controller import UserController
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from fastapi import Request, status
from domain.model.exception.resource import ResourceNotFoundError, ResourceConflictError

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"\n Iniciando la aplicación...\n") 
    yield
    print(f"\n Finalizando la aplicación...\n")
    
app = FastAPI(
    title="Gestion de Usuarios",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(UserController.router)


@app.exception_handler(ResourceNotFoundError)
async def resource_not_found_exception_handler(request: Request, exc: ResourceNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": str(exc)}
    )
    
@app.exception_handler(ResourceConflictError)
async def resource_conflict_exception_handler(request: Request, exc: ResourceConflictError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"message": str(exc)}
    )
    
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Ocurrió un error inesperado."}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8009, reload=True)