import importlib
from types import ModuleType


class pluginInterface:

    @staticmethod
    def initialise() -> None:
        """initialise the plugins"""


def importModule(name: str) -> ModuleType:
    return importlib.import_module(name)


def importAbilities(plugins: list[str]) -> None:
    for pluginName in plugins:
        plugin = importModule(pluginName)
        plugin.initialise()
