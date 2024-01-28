from abc import abstractmethod


class BaseModel:
    def __init__(self):
        pass

    def get_all_data_by_dict(self) -> dict:
        return {key: value for key, value in self.__dict__.items()}

    @staticmethod
    @abstractmethod
    def create_model(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def convert_to_dto(model):
        pass
