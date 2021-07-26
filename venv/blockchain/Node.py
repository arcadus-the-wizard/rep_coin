import Blockchain, rep_system.Reputation


class Node:
    def __init__(self, User):
        '''
        Nodes for users to interact with the blockchain. Each node is linked with a user so if it behaves dishonestly, the user will lose reputation
        :param User: The user tied with the node
        '''
        self.serial_number = 0
        self.User = User
        self.User.add_node(serial_number)

    def proof_of_stake(self, last_proof):
        '''
        A proof of stake mining model
        '''
        pass

    def mine(self):
        self.last_block = Blockchain.last_block()
        self.last_proof = self.last_block['proof']
        self.proof = self.proof_of_stake(last_proof=self.last_proof)

        #Reward the miner for their contribution
        Blockchain.newTransaction(sender = 0, recipient = self.User, amount = 1, rep_send = 0, rep_rec = self.User.getToken.value, rep_proof = 0)