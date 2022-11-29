class eventHandler:
    handlers = []

    def __init__(self):
        self.handlers = []

    def register(self, handler):
        print("registering event")
        self.handlers.append(handler)
        return self

    def unregister(self, handler):
        print("unregistering event")
        self.handlers.remove(handler)
        return self

    def trigger(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)
