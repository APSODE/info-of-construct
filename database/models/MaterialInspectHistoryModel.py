from typing import Union, List, Type, TYPE_CHECKING
from sqlalchemy import Column, Integer, String
from database.DatabaseCreator import DatabaseCreator
from database.models.BaseModel import BaseModel

if TYPE_CHECKING:
    from dto.MaterialInspectHistoryData import MaterialInspectHistoryData


class MaterialInspectHistoryModel(BaseModel, DatabaseCreator.Model):
    __tablename__ = "material_inspect_history"

    id = Column(Integer, primary_key = True)
    year = Column(String(4), nullable = False)
    sortation = Column(String(8), nullable = False)
    reception_number = Column(String(64), nullable = False)
    reception_date = Column(String(32), nullable = False)
    company_name = Column(String(32), nullable = False)
    company_location = Column(String(64), nullable = False)
    product_group = Column(String(64), nullable = False)
    construct_material_name = Column(String(128), nullable = False)
    material_model_name = Column(String(128), nullable = False)
    sortation_one = Column(String(16), nullable = False)
    test_inspect_agency_name = Column(String(16), nullable = False)
    sample_collect_date = Column(String(16), nullable = False)
    test_date = Column(String(32), nullable = False)
    test_result = Column(String(4), nullable = False)
    report_issue_date = Column(String(32), nullable = False)
    total_volatile_organic_compounds = Column(String(32), nullable = False)
    formaldehyde = Column(String(32), nullable = False)
    toluene = Column(String(32), nullable = False)

    def __init__(self,
                 year: str,
                 sortation: str,
                 reception_number: str,
                 reception_date: str,
                 company_name: str,
                 company_location: str,
                 product_group: str,
                 construct_material_name: str,
                 material_model_name: str,
                 sortation_one: str,
                 test_inspect_agency_name: str,
                 sample_collect_date: str,
                 test_date: str,
                 test_result: str,
                 report_issue_date: str,
                 total_volatile_organic_compounds: str,
                 formaldehyde: str,
                 toluene: str):

        self.year = year
        self.sortation = sortation
        self.reception_number = reception_number
        self.reception_date = reception_date
        self.company_name = company_name
        self.company_location = company_location
        self.product_group = product_group
        self.construct_material_name = construct_material_name
        self.material_model_name = material_model_name
        self.sortation_one = sortation_one
        self.test_inspect_agency_name = test_inspect_agency_name
        self.sample_collect_date = sample_collect_date
        self.test_date = test_date
        self.test_result = test_result
        self.report_issue_date = report_issue_date
        self.total_volatile_organic_compounds = total_volatile_organic_compounds
        self.formaldehyde = formaldehyde
        self.toluene = toluene

        super().__init__()

    @staticmethod
    def create_model(year: str,
                     sortation: str,
                     reception_number: str,
                     reception_date: str,
                     company_name: str,
                     company_location: str,
                     product_group: str,
                     construct_material_name: str,
                     material_model_name: str,
                     sortation_one: str,
                     test_inspect_agency_name: str,
                     sample_collect_date: str,
                     test_date: str,
                     test_result: str,
                     report_issue_date: str,
                     total_volatile_organic_compounds: str,
                     formaldehyde: str,
                     toluene: str):

        return MaterialInspectHistoryModel(
            year = year,
            sortation = sortation,
            reception_number = reception_number,
            reception_date = reception_date,
            company_name = company_name,
            company_location = company_location,
            product_group = product_group,
            construct_material_name = construct_material_name,
            material_model_name = material_model_name,
            sortation_one = sortation_one,
            test_inspect_agency_name = test_inspect_agency_name,
            sample_collect_date = sample_collect_date,
            test_date = test_date,
            test_result = test_result,
            report_issue_date = report_issue_date,
            total_volatile_organic_compounds = total_volatile_organic_compounds,
            formaldehyde = formaldehyde,
            toluene = toluene
        )

    @staticmethod
    def convert_to_dto(model: Union["MaterialInspectHistoryModel", Type["MaterialInspectHistoryModel"], List[Type["MaterialInspectHistoryModel"]]]) -> "MaterialInspectHistoryData":
        from dto.MaterialInspectHistoryData import MaterialInspectHistoryData
        dict_model_data = model.get_all_data_by_dict()

        for key in list(dict_model_data.keys()):
            if key == "_sa_instance_state":
                del dict_model_data[key]

        return MaterialInspectHistoryData.create_object(**dict_model_data)


