

from abilities import factory
from core import ai
from event import eventHandler
from jsonData.jsonDaata import loadJsonData


sphinx = ai()

sphinx.start = eventHandler()
sphinx.stop = eventHandler()

command = ""

# loading the json data
jsonData = loadJsonData()
jsonData = jsonData.loadData()

# getting the plugins and abilities
plugins = jsonData.get_Plugins
abilities = jsonData.get_Abilities

# creating a new instance of the factory
factory = factory.factory(plugins, abilities)

# loading the plugins
factory.load_plugins()

# registering the plugins
factory.register_plugins()

# loading the abilities
factory.load_abilities()

# registering the abilities
factory.register_abilities()
jsonData = loadJsonData()
data = jsonData.loadData()


# loading up the ability of the AI



#abilities = [factory.create(item) for item in data["abilities"]]
#print(f'abilities; {abilities}')
#
# with open("./plugins/plugins.json") as p:
#     pluginData = json.load(p)
#     print(f'plugins: {pluginData["plugins"]}')
#
#     #loader.loadPlugin(pluginData["plugins"])
#
plugins = [factory.create(pluginItem) for pluginItem in pluginData["items"]]
#
for pluginItem in plugins:
    pluginItem.register(sphinx)
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
