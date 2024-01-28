from typing import TYPE_CHECKING
from dto.BaseDataTransferObject import BaseDataTransferObject

if TYPE_CHECKING:
    from database.models.ConstructAgencyModel import ConstructAgencyModel


class ConstructAgencyData(BaseDataTransferObject):
    def __init__(self,
                 id: int,
                 accident_company: str,
                 accident_site_name: str,
                 household_amount: int,
                 accident_date: str,
                 implementation_status: str,
                 implementation_subject: str):

        self._id = id
        self._accident_company = accident_company
        self._accident_site_name = accident_site_name
        self._household_amount = household_amount
        self._accident_date = accident_date
        self._implementation_status = implementation_status
        self._implementation_subject = implementation_subject

        super().__init__()

    @staticmethod
    def create_object(id: int,
                      accident_company: str,
                      accident_site_name: str,
                      household_amount: int,
                      accident_date: str,
                      implementation_status: str,
                      implementation_subject: str) -> "ConstructAgencyData":

        return ConstructAgencyData(
            id = id,
            accident_company = accident_company,
            accident_site_name = accident_site_name,
            household_amount = household_amount,
            accident_date = accident_date,
            implementation_status = implementation_status,
            implementation_subject = implementation_subject
        )

    @staticmethod
    def convert_to_model(data_object: "ConstructAgencyData") -> "ConstructAgencyModel":
        from database.models.ConstructAgencyModel import ConstructAgencyModel
        converted_dict = BaseDataTransferObject.delete_id_dict_key(
            data_object_dict = data_object.get_all_data_by_dict()
        )

        return ConstructAgencyModel.create_model(**converted_dict)

    @property
    def id(self):
        return self._id

    @property
    def accident_company(self):
        return self._accident_company

    @property
    def accident_site_name(self):
        return self._accident_site_name

    @property
    def household_amount(self):
        return self._household_amount

    @property
    def accident_date(self):
        return self._accident_date

    @property
    def implementation_status(self):
        return self._implementation_status

    @property
    def implementation_subject(self):
        return self._implementation_subject

