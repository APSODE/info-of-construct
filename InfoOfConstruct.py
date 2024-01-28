import os

from database.DatabaseController import DatabaseController
from router.ConstructAgencyRouter import ConstructAgencyRouter
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from router.DeliberationResultRouter import DeliberationResultRouter
from router.InquiryRouter import InquiryRouter
from router.MaterialInspectHistoryRouter import MaterialInspectHistoryRouter
from router.RefundImplementationRouter import RefundImplementationRouter


class InfoOfConstruct(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._template = Jinja2Templates(directory = "templates")
        self._db_controller = DatabaseController.create_object()
        self._setup_config()
        self._setup_router()
        self._setup_route()

    def _setup_config(self):
        self.mount("/static", StaticFiles(directory = "static"), name = "static")

    def _setup_router(self):
        for router_class in [ConstructAgencyRouter, RefundImplementationRouter, MaterialInspectHistoryRouter, DeliberationResultRouter, InquiryRouter]:
            try:
                self.include_router(
                    getattr(router_class, "create_router")(
                        db_controller = self._db_controller,
                        template = self._template
                    )
                )

            except Exception as e:
                print(f"!! 라우터 등록 실패 !!")
                print(f"예외 : {e}")
                print(f"라우터 : {os.path.basename(router_class.__file__)}")

    def _setup_route(self):
        @self.get("/")
        async def greeting(request: Request):
            return self._template.TemplateResponse("greeting.html", {"request": request})

        @self.get("/main")
        async def main(request: Request):
            return self._template.TemplateResponse("ioc_main_default.html", {"request": request})


IOC = InfoOfConstruct()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("InfoOfConstruct:IOC", host = "0.0.0.0", port = 8000, workers = 8, log_level = "info", reload = True)

