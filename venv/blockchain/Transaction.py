import blockchain

class Transaction:
    def __init__(self, sender, recipient, amount, rep_send, rep_rec, rep_proof):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.rep_send = rep_send
        self.rep_rec = rep_rec
        self.rep_proof = rep_proof