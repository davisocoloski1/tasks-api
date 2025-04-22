# routes/__init__.py
from .auth import router as auth_router
from .tasks import router as tasks_router

# Lista todos os routers para importar de uma vez
__all__ = ["auth_router", "tasks_router"]