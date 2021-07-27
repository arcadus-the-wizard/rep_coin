import rep_system.User

'''
Byzantine Consensus protocol based off the Algorand Blockchain
https://developer.algorand.org/docs/algorand_consensus/
'''

accounts = [[User, 10], [User, 20], [User, 30]]

def vrf(sk, val):
    '''
        A verifiable random function that produced a pseudorandom output and proof so anyone can verify
    :param sk: User's secret key
    :param val: Value for proof
    :return: Pseudorandom output
    '''
    return 1

def proposal(accounts):
    '''
        Selects an account to propose a block. Uses VRF and amount of coins to select the account
    :return: An array with the user account and VRF output
    '''
    total = 0
    toReturn = []
    for x in accounts:
        total += x[1]

    for x in accounts:
            if (vrf(x[0].getKey(), x[1]) < (x[1]/total)):
                toReturn.append(x[0])
                toReturn.append(vrf(x[0].getKey(), x[1]))
                return toReturn

def softVote(proposals):
    '''
        Iterates through block proposals and calculates the hash of each VRF output, selects the smallest hash
    :param proposals: Array of arrays of proposals in the form [User, VRF]
    :return:
    '''
    smallest = -1
    index = -1
    for x in proposals:
        index += 1
        if(hash(x[1]) < smallest):
            smallest_index = index

    return proposals[smallest_index]

def selectCommittee(accounts, size):
    '''
        Iterates through accounts to see if they've been selected for the soft vote committee
    :param accounts: Accounts to select from
    :param size: the size of the committee
    :return: an array of accounts selected for the committeee
    '''
    total = 0
    toReturn = []
    for x in accounts:
        total += x[1]

    for x in accounts:
        if (vrf(x[0].getKey(), x[1]) < (x[1] / total)):
            toReturn.append(x[0])
            if len(toReturn) >= size:
                return toReturn

