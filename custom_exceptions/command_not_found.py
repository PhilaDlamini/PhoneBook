'''Custom exception for when a command is not found'''

class CommandNotFoundException(Exception):
    
    def __init__(self, msg):
        self.msg = msg;