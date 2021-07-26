import blockchain.Blockchain
class User:

    def __init__(self):
        self.nym = -1
        self.key = -1
        self.key_sign = ""

        self.rep_token = Token()

        self.nodes = []

    def __init__(self, nym, key, key_sign, rep_token):
        self.nym = nym
        self.key = key
        self.key_sign = key_sign

        self.rep_token = rep_token

    # Getters
    def getNym(self):
        return self.nym

    def getKey(self):
        return self.key

    def getToken(self):
        return self.rep_token

    # Setters
    def addNode(self, serial_number):
        nodes.append(Blockchain.find_node(serial_number))

    def setNym(self, nym):
        self.nym = nym

    def setToken(self, token):
        self.rep_token = token