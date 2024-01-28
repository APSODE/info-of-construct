from typing import List
from bs4.element import Tag


class SearchData:
    def __init__(self,
                 contract_name: str,
                 design_department: str,
                 deliberation_date: str,
                 technical_material_name: str,
                 company_name: str,
                 data_number: int):

        self._contract_name = contract_name
        self._design_department = design_department
        self._deliberation_date = deliberation_date
        self._technical_material_name = technical_material_name
        self._company_name = company_name
        self._data_number = data_number

    @staticmethod
    def create_object(contract_name: str,
                      design_department: str,
                      deliberation_date: str,
                      technical_material_name: str,
                      company_name: str,
                      data_number: int):

        return SearchData(
            contract_name = contract_name,
            design_department = design_department,
            deliberation_date = deliberation_date,
            technical_material_name = technical_material_name,
            company_name = company_name,
            data_number = data_number
        )

    @staticmethod
    def serialize_data(search_result_html: List[Tag]) -> "SearchData":
        param = [raw_text.text for raw_text in search_result_html[:-1]]
        return SearchData.create_object(*param, data_number = SearchData._get_data_number(search_result_html[-1]))

    @staticmethod
    def _get_data_number(button_element: Tag) -> int:
        data_number = button_element.find("a").attrs.get("onclick").replace(
            "openResultView(", ""
        ).replace(
            ");", ""
        )
        return int(data_number)

    @property
    def contract_name(self):
        return self._contract_name

    @property
    def design_department(self):
        return self._design_department

    @property
    def deliberation_date(self):
        return self._deliberation_date

    @property
    def technical_material_name(self):
        return self._technical_material_name

    @property
    def company_name(self):
        return self._company_name

    def get_all_data_by_dict(self) -> dict:
        return {key: value for key, value in self.__dict__.items()}

