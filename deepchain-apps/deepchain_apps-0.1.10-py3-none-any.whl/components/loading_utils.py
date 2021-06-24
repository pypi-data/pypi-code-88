import importlib.util
import sys
from pathlib import Path
from typing import Dict, Set

from deepchain.components import DeepChainApp


def find_apps(
    apps_directory: str,
    app_ids: Set[int],
) -> Dict[int, Path]:
    """Find apps paths based on app directory and app ids"""
    app_paths_dict = {}
    for app_path in Path(apps_directory).iterdir():
        if app_path.is_dir() and (int(app_path.name) in app_ids):
            app_paths_dict[int(app_path.name)] = app_path / "src/app.py"
    print(f"Found apps: {app_paths_dict}")
    return app_paths_dict


def instanciate_app(app_path: Path) -> DeepChainApp:
    """Instanciate app from path"""
    sys.path.append(str(app_path.parent))
    spec = importlib.util.spec_from_file_location("app", app_path)
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)  # type: ignore
    app = app.App()  # type: ignore
    sys.path.pop(-1)
    return app  # type: ignore
