import readline

class MyCompleter(object):

    def __init__(self, options):
        self.options = sorted(options)
    def complete(self, text, state):
        options = [i for i in self.options if i.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None
    