import os
import importlib.util
from typing import Any, Dict
from common.constants import DEFAULT

async def import_controllers() -> Dict[str, Any]:
    controllers_directory = os.path.join(
        os.path.dirname(__file__),
        DEFAULT["FILE"]["CONTROLLER"]["FOLDER_PATH"]
    )
    controller_files = [
        f for f in os.listdir(controllers_directory)
        if f.endswith(DEFAULT["FILE"]["CONTROLLER"]["FILE_NAME"])
    ]
    controller_modules = {}
    
    for file in controller_files:
        file_path = os.path.join(controllers_directory, file)
        module_name = os.path.splitext(file)[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        controller_modules[file] = module

    return controller_modules