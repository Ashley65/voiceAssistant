import importlib
from types import ModuleType


class pluginInterface:

    @staticmethod
    def initialise() -> None:
        """initialise the plugins"""


def importModule(name: str) -> pluginInterface:
    return importlib.import_module(name)


def loadAbilities(plugins: list[str]) -> None:
    for pluginName in plugins:
        plugin = importModule(pluginName)
        plugin.initialise()


def loadPlugin(plugins: list[str]) -> None:
    for pluginName in plugins:
        print(f'Current plugin loading {pluginName}')
        plugin = importModule(pluginName)
        plugin.initialise()
        print(f'loaded and initialised {plugin}')
