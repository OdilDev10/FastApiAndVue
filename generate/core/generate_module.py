from .generate_class import Generate
from .utils import VALID_DATABASE_TYPES


class CreateMODULE(Generate):
    def __init__(self, module_name_param, data_base_type_param):
        super().__init__()
        self.module_name = str(module_name_param)
        self.data_base_type = "SQLAlchemy" if data_base_type_param == "1" else "Pymongo"

        # BOOT
        self.create_module()

    def create_module(self):
        try:
            self.generate_create_folder(self.module_name)
            self.generate_create_init_file(self.module_name)
            if self.data_base_type and self.data_base_type in VALID_DATABASE_TYPES:
                if self.data_base_type == "Pymongo":
                    self.create_model_file_NOSQL(self.module_name)
                    self.create_schema_file_NOSQL(self.module_name)
                    self.create_router_file_NOSQL(self.module_name)
                    self.create_controller_file_NOSQL(self.module_name)
                else:
                    self.create_model_file_SQL(self.module_name)
                    self.create_schema_file_SQL(self.module_name)
                    self.create_router_file_SQL(self.module_name)
                    self.create_controller_file_SQL(self.module_name)
                self.generate_create_config_database(self.data_base_type)
        except Exception as error:
            print(f"❌-----------------\n{error}\n-----------------")

    def create_router_file_SQL(self, module_name: str):
        self.generate_create_files(
            module_name=module_name,
            file_name="router.py",
            operation_to_py_file="w",
            file_txt_to_read="generate/files/routers/generate_router_SQL.txt",
        )

    def create_router_file_NOSQL(self, module_name: str):
        self.generate_create_files(
            module_name=module_name,
            file_name="router.py",
            operation_to_py_file="w",
            file_txt_to_read="generate/files/routers/generate_router_NOSQL.txt",
        )

    def create_controller_file_SQL(self, module_name: str):
        self.generate_create_files(
            module_name=module_name,
            file_name="controller.py",
            operation_to_py_file="w",
            file_txt_to_read="generate/files/controllers/generate_controller_SQL.txt",
        )

    def create_controller_file_NOSQL(self, module_name: str):
        self.generate_create_files(
            module_name=module_name,
            file_name="controller.py",
            operation_to_py_file="w",
            file_txt_to_read="generate/files/controllers/generate_controller_NOSQL.txt",
        )

    def create_model_file_SQL(self, module_name: str):
        self.generate_create_files(
            module_name=module_name,
            file_name="models.py",
            operation_to_py_file="w",
            file_txt_to_read="generate/files/models/generate_models_SQL.txt",
        )

    def create_model_file_NOSQL(self, module_name: str):
        self.generate_create_files(
            module_name=module_name,
            file_name="models.py",
            operation_to_py_file="w",
            file_txt_to_read="generate/files/models/generate_models_NOSQL.txt",
        )

    def create_schema_file_SQL(self, module_name: str):
        self.generate_create_files(
            module_name=module_name,
            file_name="schemas.py",
            operation_to_py_file="w",
            file_txt_to_read="generate/files/schemas/generate_schema_SQL.txt",
        )

    def create_schema_file_NOSQL(self, module_name: str):
        self.generate_create_files(
            module_name=module_name,
            file_name="schemas.py",
            operation_to_py_file="w",
            file_txt_to_read="generate/files/schemas/generate_schema_NOSQL.txt",
        )
