import os, math, time
import random

import User, Registrar, Token

'''
Implemetation of Decentralised Reputation by Tassos Dimitriou by Max Krawiec.
Placeholder values are used for some variables
'''

def __init__(self):
    '''
    :param q: q = O(2Y) where "Y" is a security parameter
    :param G: Group of prime order q
    :param g: order q generator of G
    :param hi: To be used by Pederson commit
    '''
    params = [q, G, g, h, h1, h2]

# Computing
def generators(n):
    s = set(range(1, n))
    results = []
    for a in s:
        g = set()
        for x in s:
            g.add((a ** x) % n)
        if g == s:
            results.append(a)
    return results

def a_xor_b(a,b):
    '''
        Takes in 2 string inputs, converts them to hex values and performs an XOR operation on them
    :param a: First string to xor
    :param b: Second string to xor
    :return: The XOR'd value between a and b in hexadecimal
    '''
    a_hex = int(a,base=16)
    b_hex = int(b,base=16)
    return (a_hex ^ b_hex)

def user_from_nym(nym):
    for i in Registrar.users:
        if (i.getNym == nym):
             return i

def pederson_commit(message, q):
    '''
    :param message: The message to be committed
    :param q: Prime order of Group
    :return: the committed "C-value"
    '''
    rand_r = random.randint(1, 64)
    G = generators(q)
    C = math.pow(G[0], message) * math.pow(G[1], rand_r)
    return C


# Reputation
def register(params, User, Registrar):
    '''
    :param User: User to be registered
    :param Registrar: Registrar the user will be appended to

    Executed between a user and a registrar.
    U generates a secret key and computes I.
    Once R identifies I it signs it.
    Signature Sig_R(I) serves as a registration token.

    output: SK_U, Sig_R(I)
    '''
    # Key used to bind reputation to user-generated pseudonyms
    key = 3
    User.key = key

    # Find generators of group G order q
    q = 5
    gen = generators(q)
    # Compute public identifier "i"
    i = math.pow(gen[0],key)

    # Sign i with the Registrar's key and add them to the Registrar
    sig_r_i = a_xor_b(i, Registrar.key)
    Registrar.addUser(User = User, userSig=sig_r_i)

def nymGen(params, User, sk_u):
    '''
    Run by a user to generate a new pseudonym bound to the secret key. Can be called any number of times.
    output: Nym_U
    '''

    # User nym has form nym_u = g^r(h^sk_u)

    r = random.randint()
    nym = math.pow(params[2], r) * math.pow(params[3], sk_u)
    User.setNym(self.nym)
    toReturn = [self.nym, r]
    return toReturn

def mintRep(params, sk_u, nym_u, aux_u):
    '''
    Executed by a user to bind an initial reputation token to their secret key.
    Outputs the token and a proof Y_M that both the token and pseudonym are issued to the same user.
    output: Rep_U, Y_M
    '''

    # Correct form for rep_u in the paper - NEEDS UPDATING
    rep_u = Token()
    User.setToken(token)

    sig_rep = a_xor_b(User.rep_token.toString(), sk_u)
    sig_nym = a_xor_b(nym_u,sk_u)
    proof = a_xor_b(sig_rep, sig_nym)
    return proof

def mintVerify(self, nym_u, rep_u, v, sig_i_r, y_m):
    '''
    Used to validate reputation value V. Returns 1 if the proof verifies successfully.
    XOR the User's nym and rep with the secret key, if it's the same value as teh proof then it is valid

    output: {0,1}
    '''

    User = user_from_nym(nym_u)
    sig_rep = a_xor_b(rep_u.toString(), User.key)
    sig_nym = a_xor_b(nym_u, User.key)
    proof = a_xor_b(sig_rep, sig_nym)

    if (y_m == proof):
        # Add token to the registrar
        return 1
    else:
        return 0

def showRep(params, nym_v_u, rep_u):
    '''
    Run by user U to prove to user V that U's reputation is captured by Rep_U and was issued to the same user that owns Nym_V_U.
    Proof is given by Y_S and a new reputation Rep_New_U replaces the old one in the ledger.
    output: Rep_New_U, Y_S
    '''

    User = user_from_nym(nym_v_u)
    # 3 is a placement holder for the serial number
    rep_u_new = token(3, User.rep_token.value)
    User.setToken(rep_u_new)


def showVerify(params, nym_u, L_i, s, rep_new_u, y_s):
    '''
    Validates a shown reputation. Returns 1 if the proof Y_S is valid for Nym_V_U and the new reputation token is added to the ledger.
    Checks that new token is in L_i, examines and validates the proof and checks the serial number has not appeared in any previous transaction

    output: {0,1}
    '''
    pass

def updateRep(params, nym_u, nym_v, val, aux_u_v):
    '''
    Same effect as MintRep but value of reputation is updated by Val in Rep_New_U.
    Proof Y_U_PD shows the value was updated correctly and both Rep_U and Rep_New_U are bound to the same secret key.
    output: Rep_New_U, Y_U_PD
    '''

    User_u = user_from_nym(nym_u)
    User_v = user_from_nym(nym_v)

    rep_u_old = User_u.getToken
    # 5 is a placement holder for the serial number
    rep_u_new = token(rep_u_old.serial, rep_u_old.value)

    timestamp_u = time.time()
    tag_u = hash(nym_u + nym_v + timestamp_u + User_u.getKey())

    valid = 0
    # Show that rep_u belongs to committed reputation tokens
    # Show that rep_u, nym_u and tag_u share the same secret keys
    if (showRep(nym_u, User_u.getToken()) == rep_u_new.value):
        valid = 1

    proof = 1

    # V's actions
    rand_r = 5
    c_val = math.pow(params[1], rand_r) * math.pow(params[5], val)

    if(proof == 1):
        rep_u_new_new = rep_u_new * c_val
    else:
        return "Invalid Proof"

    tag_v = hash(nym_u, nym_v, timestamp_u, User_v.getKey())

def updateVerify(params, nym_v_u, val, rep_new_u, aux_u_v, y_u_pd):
    '''
    Verifies value in the new reputation token has been increased by val. If proof Y_U_PD is valid, Rep_New_U is added to the ledger.
    output: {0,1}
    '''

    '''
    Miner checks validity of tag_u for correctness of rep_new_new_u and computes c_val given rand_r, val
    If all tests succeed a transaction updates the reputation of the user in the ledger
    '''

    verified = 0

    return verified