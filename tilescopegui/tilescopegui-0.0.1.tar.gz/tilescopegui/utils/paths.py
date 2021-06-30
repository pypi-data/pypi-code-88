from pathlib import Path


class PathUtil:
    """Helper class for directory paths."""

    _TILESCOPEGUI_ROOT = Path(__file__).parent.parent
    _PROJECT_ROOT = _TILESCOPEGUI_ROOT.parent
    _STATIC_DIR = _TILESCOPEGUI_ROOT.joinpath("static")
    _TEMPLATE_DIR = _TILESCOPEGUI_ROOT.joinpath("static")

    @staticmethod
    def static_dir() -> str:
        """Get path to static directory."""
        return PathUtil._STATIC_DIR.as_posix()

    @staticmethod
    def tempalte_dir() -> str:
        """Get path to tempalte directory."""
        return PathUtil._TEMPLATE_DIR.as_posix()
