class Token:

    def __init__(self):
        self.rand_r = binascii.hexlify(os.urandom(32))
        self.key = binascii.hexlify(os.urandom(64))
        self.serial_number = 0
        self.value = 0

    def __init__(self, serial, value):
        self.rand_r = binascii.hexlify(os.urandom(32))
        self.key = binascii.hexlify(os.urandom(64))
        self.serial_number = serial
        self.value = value

    def toString(self):
        return self.random_r + self.key + self.serial_number + self.value

