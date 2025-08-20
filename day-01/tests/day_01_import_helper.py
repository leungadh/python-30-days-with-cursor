import importlib.util
import pathlib

def import_from_path(module_name: str, path: str):
    p = pathlib.Path(path).resolve()
    spec = importlib.util.spec_from_file_location(module_name, p)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod
