import blockchain.Block, blockchain.Transaction

'''
Basic implementation of a blockchain in python to implement a reputation system into
'''


def __init__(self):
    self.chain = []
    self.current_transactions = []
    self.nodes = []

def find_node(self, serial_number):
    for i in nodes:
        if (i.getSerial == serial_number):
            return i

def new_block(self, index, proof, previous_hash):
    #Append blockchain with new block
    self.chain.append(Block(index, proof, previous_hash))

def new_transaction(self, sender, recipient, amount, rep_send, rep_rec, rep_proof):
    #Append transactions list with current transaction
    self.current_transactions.append(Transaction(sender, recipient, amount, rep_send, rep_rec, rep_proof))

def create_genesis(self):
    self.new_block(previous_hash = 1, proof = 100)

@staticmethod
def hash(block):
    block_string = json.dump(block, sort_keys= True).encode()
    return hashlib.sha256(block_string).hexdigest()

@property
def last_block(self):
    #Call the last block in the blockchain
    return self.chain[-1]
