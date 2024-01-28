from abc import abstractmethod
from fastapi.templating import Jinja2Templates
from database.DatabaseController import DatabaseController


class BaseRouter:
    @staticmethod
    @abstractmethod
    def create_router(db_controller: DatabaseController, template: Jinja2Templates):
        pass

    @abstractmethod
    def setup_routes(self):
        pass
