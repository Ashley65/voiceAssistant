import json
from typing import Protocol


class jsonTypes:
    plugins: []
    abilities: []

    def __init__(self, plugins, abilities):
        self.plugins = plugins
        self.abilities = abilities

    @property
    def get_Plugins(self):
        return self.plugins

    @property
    def get_Abilities(self):
        return self.abilities


class loadJsonData:

    # def __init__(self)

    def loadData(self):
        with open("./abilities/abilities.json") as loadedData:
            data = json.load(loadedData)
            plugins = data["plugins"]

            abilities = data["abilities"]

            jsonData = jsonTypes(plugins, abilities)
            return jsonData
