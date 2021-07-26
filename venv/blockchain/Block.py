import blockchain

class Block:
    def __init__(self, index, proof, previous_hash):
        self.index = index
        self.timestamp = time()
        self.proof = proof
        self.previous_hash = previous_hash or self.hash(self.chain[-1])