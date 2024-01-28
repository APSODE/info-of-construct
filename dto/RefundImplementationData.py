from typing import TYPE_CHECKING
from dto.BaseDataTransferObject import BaseDataTransferObject

if TYPE_CHECKING:
    from database.models.RefundImplementationModel import RefundImplementationModel


class RefundImplementationData(BaseDataTransferObject):
    def __init__(self,
                 id: int,
                 year: str,
                 accident_company: str,
                 location: str,
                 site_name: str,
                 accident_date: str,
                 implementation_plan: str,
                 subrogation_amount: int):
        self._id = id
        self._year = year
        self._accident_company = accident_company
        self._location = location
        self._site_name = site_name
        self._accident_date = accident_date
        self._implementation_plan = implementation_plan
        self._subrogation_amount = subrogation_amount

        super().__init__()

    @staticmethod
    def create_object(id: int,
                      year: str,
                      accident_company: str,
                      location: str,
                      site_name: str,
                      accident_date: str,
                      implementation_plan: str,
                      subrogation_amount: int) -> "RefundImplementationData":

        return RefundImplementationData(
            id = id,
            year = year,
            accident_company = accident_company,
            location = location,
            site_name = site_name,
            accident_date = accident_date,
            implementation_plan = implementation_plan,
            subrogation_amount = subrogation_amount
        )

    @staticmethod
    def convert_to_model(data_object: "RefundImplementationData") -> "RefundImplementationModel":
        from database.models.RefundImplementationModel import RefundImplementationModel
        converted_dict = BaseDataTransferObject.delete_id_dict_key(
            data_object_dict = data_object.get_all_data_by_dict()
        )

        return RefundImplementationModel.create_model(**converted_dict)

    @property
    def id(self):
        return self._id

    @property
    def year(self):
        return self._year

    @property
    def accident_company(self):
        return self._accident_company

    @property
    def location(self):
        return self._location

    @property
    def site_name(self):
        return self._site_name

    @property
    def accident_date(self):
        return self._accident_date

    @property
    def implementation_plan(self):
        return self._implementation_plan

    @property
    def subrogation_amount(self):
        return self._subrogation_amount

