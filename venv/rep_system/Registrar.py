class Registrar:

    def __init__(self):
        self.key = binascii.hexlify(os.urandom(64))
        self.users = []
        self.tokens = []
        self.sigs = []

    def addUser(self, User, userSig):
        self.users.append(User)
        self.sigs.append(userSig)

    def addToken(self, token):
        self.tokens.append(token)
