from typing import Optional, Dict, List
from database.DatabaseController import DatabaseController
from database.models.ConstructAgencyModel import ConstructAgencyModel
from database.models.RefundImplementationModel import RefundImplementationModel
from database.models.MaterialInspectHistoryModel import MaterialInspectHistoryModel
from csv import reader


class DataMigrator:
    def __init__(self, row_length: int, column_length: int, csv_file_path: str):
        self._db_controller = DatabaseController.create_object()
        self._row_length = row_length
        self._column_length = column_length
        self._csv_file_path = csv_file_path

    @staticmethod
    def create_object(row_length: int, column_length: int, csv_file_path: str):
        return DataMigrator(row_length, column_length, csv_file_path)

    @staticmethod
    def start():
        migrator = DataMigrator.create_object(row_length = 12, column_length = 7, csv_file_path = ".\\num1_data_2.csv")
        migrator.migrate()

    def migrate(self):
        migrated_models = []
        with open(self._csv_file_path, "r") as csv_file:
            csv_file_reader = reader(csv_file)

            for row in csv_file_reader:
                model = RefundImplementationModel.create_model(*row[1:])
                migrated_models.append(model)

        self._db_controller.add_data(
            model = migrated_models,
            with_commit = True
        )







