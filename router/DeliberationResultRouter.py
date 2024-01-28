from typing import Optional
from fastapi import APIRouter, Request
from sqlalchemy import and_, or_
from starlette.templating import Jinja2Templates
from router.BaseRouter import BaseRouter
from database.DatabaseController import DatabaseController


class DeliberationResultRouter(APIRouter, BaseRouter):
    def __init__(self, db_controller: DatabaseController, template: Jinja2Templates):
        super().__init__(
            prefix = "/deliberation_result",
            tags = ["items"],
            # dependencies = [Depends(get_token_header)],
            responses = {404: {"description": "Not found"}}
        )

        self._template = template
        self._db_controller = db_controller
        self.setup_routes()

    @staticmethod
    def create_router(**kwargs):
        return DeliberationResultRouter(**kwargs)

    def setup_routes(self):
        @self.get("/")
        async def dr_main(request: Request):
            return self._template.TemplateResponse(
                "inquiry.html", {"request": request, "inquiry_type": "dr"}
            )


