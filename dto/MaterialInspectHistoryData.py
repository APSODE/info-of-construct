from typing import TYPE_CHECKING
from dto.BaseDataTransferObject import BaseDataTransferObject

if TYPE_CHECKING:
    from database.models.MaterialInspectHistoryModel import MaterialInspectHistoryModel


class MaterialInspectHistoryData(BaseDataTransferObject):
    def __init__(self,
                 id: int,
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

        self._id = id
        self._year = year
        self._sortation = sortation
        self._reception_number = reception_number
        self._reception_date = reception_date
        self._company_name = company_name
        self._company_location = company_location
        self._product_group = product_group
        self._construct_material_name = construct_material_name
        self._material_model_name = material_model_name
        self._sortation_one = sortation_one
        self._test_inspect_agency_name = test_inspect_agency_name
        self._sample_collect_date = sample_collect_date
        self._test_date = test_date
        self._test_result = test_result
        self._report_issue_date = report_issue_date
        self._total_volatile_organic_compounds = total_volatile_organic_compounds
        self._formaldehyde = formaldehyde
        self._toluene = toluene

        super().__init__()

    @staticmethod
    def create_object(id: int,
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
                      toluene: str) -> "MaterialInspectHistoryData":

        return MaterialInspectHistoryData(
            id = id,
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
    def convert_to_model(data_object: "MaterialInspectHistoryData") -> "MaterialInspectHistoryModel":
        from database.models.MaterialInspectHistoryModel import MaterialInspectHistoryModel
        converted_dict = BaseDataTransferObject.delete_id_dict_key(
            data_object_dict = data_object.get_all_data_by_dict()
        )

        return MaterialInspectHistoryModel.create_model(**converted_dict)

    @property
    def id(self):
        return self._id

    @property
    def year(self):
        return self._year

    @property
    def sortation(self):
        return self._sortation

    @property
    def reception_number(self):
        return self._reception_number

    @property
    def reception_date(self):
        return self._reception_date

    @property
    def company_name(self):
        return self._company_name

    @property
    def company_location(self):
        return self._company_location

    @property
    def product_group(self):
        return self._product_group

    @property
    def construct_material_name(self):
        return self._construct_material_name

    @property
    def material_model_name(self):
        return self._material_model_name

    @property
    def sortation_one(self):
        return self._sortation_one

    @property
    def test_inspect_agency_name(self):
        return self._test_inspect_agency_name

    @property
    def sample_collect_date(self):
        return self._sample_collect_date

    @property
    def test_date(self):
        return self._test_date

    @property
    def test_result(self):
        return self._test_result

    @property
    def report_issue_date(self):
        return self._report_issue_date

    @property
    def total_volatile_organic_compounds(self):
        return self._total_volatile_organic_compounds

    @property
    def formaldehyde(self):
        return self._formaldehyde

    @property
    def toluene(self):
        return self._toluene

