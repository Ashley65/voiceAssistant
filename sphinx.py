from core import ai
from datetime import datetime
import sys
import json
from event import eventHandler
from datetime import datetime
from abilities import loader

sphinx = ai()

sphinx.start = eventHandler()
sphinx.stop = eventHandler()

command = ""

# loading up the ability of the AI
with open(".abilities/abilities.json") as f:
    data = json.load(f)

    #
    loader.load_abilities(data["plugins"])
