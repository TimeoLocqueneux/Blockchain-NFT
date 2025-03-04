from helpers import timestamp, cryptography
from CollectionNFT import Collection
from json import dumps

class Tokisen :
    def __init__(self, issuerPublicKey):
        self.issuerPublicKey = issuerPublicKey
        self.timestamp = timestamp.now()

    def build_payload(self):
        payload = {}
        payload['issuerPublicKey'] = self.issuerPublicKey
        payload['timestamp'] = self.timestamp
        return payload
    
    def generate_token_key(self):
        payload = self.build_payload()
        payloadString = dumps(payload, sort_keys=True)
        self.tokenKey = cryptography.hash_string(payloadString)
        return self.tokenKey
    
    def add_token(self, issuerPublicKey, numberoftokens):
        tokenList = []
        for _ in range(numberoftokens):            
            self.tokenKey = self.generate_token_key()
            tokenList.append(self.tokenKey)
        account= {}
        if issuerPublicKey in account:
            account[issuerPublicKey] += tokenList
        else:
            account[issuerPublicKey] = tokenList
        return account
    
    def remove_token(self, issuerPublicKey, numberoftokens):
        account= {}
        if issuerPublicKey in account:
                if account[issuerPublicKey] < numberoftokens:
                    return "Error : Not enough tokens to remove"
                else:                                        
                    account[issuerPublicKey] -= numberoftokens
        else:
            return "Error : No tokens to remove"
        return account
    
    def send_token(self, senderPublicKey, receiverPublicKey, numberoftokens):
        self.remove_token(senderPublicKey, numberoftokens)
        self.add_token(receiverPublicKey, numberoftokens)
        return "Tokens sent successfully"
    


