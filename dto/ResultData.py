from typing import List

from bs4.element import Tag


class ResultData:
    def __init__(self,
                 technical_material_name: str,
                 design_department: str,
                 deliberation_date: str,
                 construct_type: str,
                 construct_kind_name: str,
                 company_name: str,
                 estimated_cost: str,
                 selection_result: str):

        self._technical_material_name = technical_material_name
        self._design_department = design_department
        self._deliberation_date = deliberation_date
        self._construct_type = construct_type
        self._construct_kind_name = construct_kind_name
        self._company_name = company_name
        self._estimated_cost = estimated_cost
        self._selection_result = selection_result

    @staticmethod
    def create_object(technical_material_name: str,
                      design_department: str,
                      deliberation_date: str,
                      construct_type: str,
                      construct_kind_name: str,
                      company_name: str,
                      estimated_cost: str,
                      selection_result: str) -> "ResultData":

        return ResultData(
            technical_material_name = technical_material_name,
            design_department = design_department,
            deliberation_date = deliberation_date,
            construct_type = construct_type,
            construct_kind_name = construct_kind_name,
            company_name = company_name,
            estimated_cost = estimated_cost,
            selection_result = selection_result
        )

    @staticmethod
    def serialize_data(result_view_html: List[Tag]) -> "ResultData":
        param = [raw_text.text for raw_text in result_view_html[:-1]]
        return ResultData.create_object(
            *param,
            selection_result = ResultData._get_attached_file_href(result_view_html[-1])
        )

    @staticmethod
    def _get_attached_file_href(attached_file_html_element: Tag) -> str:
        attached_file_href = attached_file_html_element.find("a").attrs.get("onclick").replace(
            "goHref('", ""
        ).replace(
            "', '')", ""
        )

        return "https://partner.lh.or.kr" + attached_file_href

    @property
    def technical_material_name(self):
        return self._technical_material_name

    @property
    def design_department(self):
        return self._design_department

    @property
    def deliberation_date(self):
        return self._deliberation_date

    @property
    def construct_type(self):
        return self._construct_type

    @property
    def construct_kind_name(self):
        return self._construct_kind_name

    @property
    def company_name(self):
        return self._company_name

    @property
    def estimated_cost(self):
        return self._estimated_cost

    @property
    def selection_result(self):
        return self._selection_result

    def get_all_data_by_dict(self) -> dict:
        return {key: value for key, value in self.__dict__.items()}

