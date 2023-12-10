from .utils import VALID_DATABASE_TYPES, VALID_OPERATIONS_FILES
import os


class Generate:
    def __init__(self):
        pass

    def generate_create_init_file(self, ifExistsModuleName: str):
        with open(os.path.join(ifExistsModuleName, "__init__.py"), "w") as file:
            pass

    def generate_create_config_database(self, data_base_type: str):
        if data_base_type in VALID_DATABASE_TYPES:
            if not os.path.exists("db"):
                self.generate_create_folder("db")
                self.generate_create_init_file('db')

            if data_base_type == "Pymongo" and not os.path.exists(
                "config_nosql.py"
            ):
                self.generate_create_files(
                    "",
                    "config_nosql.py",
                    "w",
                    "generate/files/db/generate_db_config_NOSQL.txt",
                )

            elif data_base_type == "SQLAlchemy" and not os.path.exists(
                "config.py"
            ):
                self.generate_create_files(
                    "",
                    "config.py",
                    "w",
                    "generate/files/db/generate_db_config_SQL.txt",
                )

                # with open("generate/files/main/generate_main_SQL.txt", "r") as file:
                #     contenido_modificado = file.read()
                # with open("main.py", "w") as file:
                #     file.write(contenido_modificado)

            else:
                print(f"✓----Database config {data_base_type} exists")
                return

            print(f"✓----Database config {data_base_type} created successfully")
            return

    def generate_create_folder(self, folder_name: str):
        os.makedirs(folder_name)

    def generate_create_files(
        self,
        module_name: str,
        file_name: str,
        operation_to_py_file: str,
        file_txt_to_read: str,
    ):
        if operation_to_py_file not in VALID_OPERATIONS_FILES:
            raise ValueError(
                "Invalid operation_to_py_file. Valid options are: {}".format(
                    VALID_OPERATIONS_FILES
                )
            )
        if not file_name:
            raise ValueError("Invalid filename")

        with open(
            os.path.join(module_name or "", file_name), operation_to_py_file
        ) as file:
            file_path = os.path.join(os.getcwd(), os.path.normpath(file_txt_to_read))
            text_file = open(file_path, "r")
            data = text_file.read()
            if module_name:
                data = data.replace("{module_name}", module_name)
            file.write(data)
            text_file.close()
        print(f"✓----File {file_name} created successfully")
