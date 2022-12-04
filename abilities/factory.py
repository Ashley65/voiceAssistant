from typing import Callable, Any
from abilities.abilities import ability

abilityCreateFunc: dict[str, Callable[..., ability]] = {}


def register(abilityName: str, createFunc: Callable[..., ability]):
    abilityCreateFunc[abilityName] = createFunc
    print(f'register {abilityName}')


def unregister(abilityName: str):
    abilityCreateFunc.pop(abilityName, None)


def create(args: dict[str, Any]) -> ability:
    abilityName = args.copy().pop('name')
    try:
        createFunc = abilityCreateFunc[abilityName]
        return createFunc(**args.copy())
    except KeyError:
        # This will of code will notify the system when an unsupported api/Ability is used
        raise ValueError(f"Ability type not recognise: {abilityName}") from None
