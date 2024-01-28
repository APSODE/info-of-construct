from typing import Union, List, Type, TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from database.DatabaseCreator import DatabaseCreator
from database.models.BaseModel import BaseModel

if TYPE_CHECKING:
    from dto.RefundImplementationData import RefundImplementationData


class RefundImplementationModel(BaseModel, DatabaseCreator.Model):
    __tablename__ = "refund_implementation"

    id = Column(Integer, primary_key = True)
    year = Column(String(4), nullable = False)
    accident_company = Column(String(32), nullable = False)
    location = Column(String(64), nullable = False)
    site_name = Column(String(64), nullable = False)
    accident_date = Column(String(16), nullable = False)
    implementation_plan = Column(String(64), nullable = False)
    subrogation_amount = Column(String(32), nullable = False)

    def __init__(self,
                 year: str,
                 accident_company: str,
                 location: str,
                 site_name: str,
                 accident_date: str,
                 implementation_plan: str,
                 subrogation_amount: int):

        self.year = year
        self.accident_company = accident_company
        self.location = location
        self.site_name = site_name
        self.accident_date = accident_date
        self.implementation_plan = implementation_plan
        self.subrogation_amount = subrogation_amount

        super().__init__()

    @staticmethod
    def create_model(year: str,
                     accident_company: str,
                     location: str,
                     site_name: str,
                     accident_date: str,
                     implementation_plan: str,
                     subrogation_amount: str) -> "RefundImplementationModel":

        return RefundImplementationModel(
            year = year,
            accident_company = accident_company,
            location = location,
            site_name = site_name,
            accident_date = accident_date,
            implementation_plan = implementation_plan,
            subrogation_amount = subrogation_amount
        )

    @staticmethod
    def convert_to_dto(model: Union["RefundImplementationModel", Type["RefundImplementationModel"], List[Type["RefundImplementationModel"]]]) -> "RefundImplementationData":
        from dto.RefundImplementationData import RefundImplementationData
        dict_model_data = model.get_all_data_by_dict()

        for key in list(dict_model_data.keys()):
            if "model" in key:
                del dict_model_data[key]

            elif key == "_sa_instance_state":
                del dict_model_data[key]

        return RefundImplementationData.create_object(**dict_model_data)

