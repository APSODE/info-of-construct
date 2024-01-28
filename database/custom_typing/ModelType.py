from typing import Union, Type
from database.models.MaterialInspectHistoryModel import MaterialInspectHistoryModel
from database.models.ConstructAgencyModel import ConstructAgencyModel
from database.models.RefundImplementationModel import RefundImplementationModel


ModelType = Union[
    MaterialInspectHistoryModel,
    ConstructAgencyModel,
    RefundImplementationModel
]

