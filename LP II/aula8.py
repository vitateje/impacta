''' Encapsulamento - Proteção de variaveis - (de informações sensiveis) '''

class Nova():

    def __init__(self):
        self._protected = 0
        self.unprotected = 1

obj = Nova()
print(obj.)