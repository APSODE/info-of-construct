from typing import Union, Type, List, TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from database.DatabaseCreator import DatabaseCreator
from database.models.BaseModel import BaseModel

if TYPE_CHECKING:
    from dto.ConstructAgencyData import ConstructAgencyData


class ConstructAgencyModel(BaseModel, DatabaseCreator.Model):
    __tablename__ = "construct_agency"

    id = Column(Integer, primary_key = True)
    accident_company = Column(String(16), nullable = False)
    accident_site_name = Column(String(64), nullable = False)
    household_amount = Column(String(32), nullable = False)
    accident_date = Column(String(16), nullable = False)
    implementation_status = Column(String(16), nullable = False)
    implementation_subject = Column(String(16), nullable = False)

    def __init__(self,
                 accident_company: str,
                 accident_site_name: str,
                 household_amount: int,
                 accident_date: str,
                 implementation_status: str,
                 implementation_subject: str):

        self.accident_company = accident_company
        self.accident_site_name = accident_site_name
        self.household_amount = household_amount
        self.accident_date = accident_date
        self.implementation_status = implementation_status
        self.implementation_subject = implementation_subject

        super().__init__()

    @staticmethod
    def create_model(
                     accident_company: str,
                     accident_site_name: str,
                     household_amount: str,
                     accident_date: str,
                     implementation_status: str,
                     implementation_subject: str) -> "ConstructAgencyModel":

        return ConstructAgencyModel(
            accident_company = accident_company,
            accident_site_name = accident_site_name,
            household_amount = household_amount,
            accident_date = accident_date,
            implementation_status = implementation_status,
            implementation_subject = implementation_subject
        )

    @staticmethod
    def convert_to_dto(model: Union["ConstructAgencyModel", Type["ConstructAgencyModel"], List[Type["ConstructAgencyModel"]]]) -> "ConstructAgencyData":
        from dto.ConstructAgencyData import ConstructAgencyData
        dict_model_data = model.get_all_data_by_dict()

        for key in list(dict_model_data.keys()):
            if "model" in key:
                del dict_model_data[key]

            elif key == "_sa_instance_state":
                del dict_model_data[key]

        return ConstructAgencyData.create_object(**dict_model_data)




