from nsbot import LOGS
from os.path import dirname, basename, isfile

import glob

def list_modules():
    module_path = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in module_path
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_modules

ALL_MODULES = sorted(list_modules())

module_names = ""
for i in ALL_MODULES:
    if i == ALL_MODULES[-1]:
        module_names += i
    else:
        module_names += i+", "
LOGS.info("Loaded Modules: %s", module_names)
