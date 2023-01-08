

from abilities import factory
from core import ai
from event import eventHandler
from jsonData.jsonDaata import loadJsonData


sphinx = ai()

sphinx.start = eventHandler()
sphinx.stop = eventHandler()

command = ""
jsonData = loadJsonData()
data = jsonData.loadData()


# loading up the ability of the AI

    # loads the plugins
    #loader.loadAbilities(data["plugins"])

#abilities = [factory.create(item) for item in data["abilities"]]
#print(f'abilities; {abilities}')
#
# with open("./plugins/plugins.json") as p:
#     pluginData = json.load(p)
#     print(f'plugins: {pluginData["plugins"]}')
#
#     #loader.loadPlugin(pluginData["plugins"])
#
# plugins = [factory.create(pluginItem) for pluginItem in pluginData["items"]]
#
# for pluginItem in plugins:
#     pluginItem.register(sphinx)
#
# sphinx.start.trigger()
# sphinx.say("Hello")
# while command not in ["good bye", 'bye', 'quit', 'exit', 'goodbye', 'see you']:
#     command = ""
#     command = sphinx.listen()
#     if command:
#         command = command.lower()
#         for abilities in abilities:
#             if command in abilities.commands(command):
#                 abilities.handleCommand(command, sphinx)
#
# sphinx.say("goodbye sir")
