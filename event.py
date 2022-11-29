class eventHandler:
    handlers = []

    # I created an array to store and handle the user request
    def __init__(self):
        self.handlers = []

    # The function here handles the add of new request from the user
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
