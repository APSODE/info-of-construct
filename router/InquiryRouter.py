from typing import Optional
from fastapi import APIRouter, Request
from sqlalchemy import and_, or_
from starlette.templating import Jinja2Templates

from database.models.ConstructAgencyModel import ConstructAgencyModel
from database.models.MaterialInspectHistoryModel import MaterialInspectHistoryModel
from database.models.RefundImplementationModel import RefundImplementationModel
from dto.ConstructAgencyData import ConstructAgencyData
from router.BaseRouter import BaseRouter
from database.DatabaseController import DatabaseController
from pydantic import BaseModel

from src.DeliberationResultFinder import DeliberationResultFinder


class _InquiryData(BaseModel):
    company_name: str
    page_number: int = 1


class InquiryRouter(APIRouter, BaseRouter):
    def __init__(self, db_controller: DatabaseController, template: Jinja2Templates):
        super().__init__(
            prefix = "/inquiry",
            tags = ["items"],
            # dependencies = [Depends(get_token_header)],
            responses = {404: {"description": "Not found"}}
        )

        self._template = template
        self._db_controller = db_controller
        self.setup_routes()

    @staticmethod
    def create_router(**kwargs):
        return InquiryRouter(**kwargs)

    def setup_routes(self):
        @self.post("/ca_inquiry")
        async def ca_inquiry(request: Request, ajax_payload: _InquiryData):
            inquiried_models = self._db_controller.get_data(
                model_class = ConstructAgencyModel,
                filter = ConstructAgencyModel.accident_company == ajax_payload.company_name
            )

            key_deleted_inquiried_models = [list(ConstructAgencyModel.convert_to_dto(im).get_all_data_by_dict().values()) for im in inquiried_models]

            return {"inquiry_datas": key_deleted_inquiried_models}

        @self.post("/ri_inquiry")
        async def ri_inquiry(request: Request, ajax_payload: _InquiryData):
            inquiried_models = self._db_controller.get_data(
                model_class = RefundImplementationModel,
                filter = RefundImplementationModel.accident_company == ajax_payload.company_name
            )
            print(inquiried_models)

            key_deleted_inquiried_models = [list(RefundImplementationModel.convert_to_dto(im).get_all_data_by_dict().values()) for im in inquiried_models]
            print(key_deleted_inquiried_models)

            return {"inquiry_datas": key_deleted_inquiried_models}

        @self.post("/mih_inquiry")
        async def mih_inquiry(request: Request, ajax_payload: _InquiryData):
            inquiried_models = self._db_controller.get_data(
                model_class = MaterialInspectHistoryModel,
                filter = MaterialInspectHistoryModel.company_name == ajax_payload.company_name
            )

            key_deleted_inquiried_models = [list(MaterialInspectHistoryModel.convert_to_dto(im).get_all_data_by_dict().values()) for im in inquiried_models]


            return {"inquiry_datas": key_deleted_inquiried_models}

        @self.post("/dr_inquiry")
        async def dr_inquiry(request: Request, ajax_payload: _InquiryData):
            dr_finder = DeliberationResultFinder.create_finder()
            search_results = dr_finder.search(search_keyword = ajax_payload.company_name, page_num = ajax_payload.page_number)

            key_deleted_searched_results = [list(sr.get_all_data_by_dict().values())[:-1] for sr in search_results]
            print(key_deleted_searched_results)
            return {"inquiry_datas": key_deleted_searched_results}

