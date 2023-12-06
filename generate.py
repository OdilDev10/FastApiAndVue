from generate.core.generate_app import CreateAPP
from generate.core.generate_module import CreateMODULE

if __name__ == "__main__":
    operation = str(input("1. Modulo, 2. Proyecto: "))
    if operation == "1":
        module_name = str(input("Nombre del módulo: "))
        data_base_type = str(input("Base de datos: 1. SQLAlchemy, 2. Pymongo: "))

        try:
            generate_module = CreateMODULE(
                module_name_param=module_name, data_base_type_param=data_base_type
            )
        except Exception as error:
            print("❌-------------------------ERROR-------------------------❌\n", error)
    elif operation == "2":
        try:
            create_app = CreateAPP()

        except Exception as error:
            print("❌-------------------------ERROR-------------------------❌\n", error)
